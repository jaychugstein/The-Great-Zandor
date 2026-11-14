// THE GREAT ZANDOR - a 21 questions guessing game for the Arduboy FX, in the spirit of the 2000s handheld guessing toys,
// hosted by a creepy fortune teller in his booth.
// Look at something near you. It asks what kind of thing it is (animal, plant, man-made or other), then up to 21 questions, guessing along
// the way when it's sure. If its guess at 21 is wrong it keeps going to 25. by jaychugstein
//
// Controls: the four arrows answer, like the toy's four buttons: up YES, down NO, left SOMETIMES, right UNKNOWN.
// B (the outer button) starts and moves things along. The first question works the same way: up ANIMAL, down VEGETABLE, left MINERAL, right OTHER.
//
// How it thinks: the FX chip holds a table of how every thing answers every question (no, rarely, sometimes, usually, yes;
// built by art/data.py). Each thing gets a score from the answers so far. Every answer adds to the score of the things that agree and
// takes from the ones that don't, so one wrong answer only sets a thing back - it can still win later.
// The next question is picked fresh each time: of all the unasked questions, the one that best splits the
// current leaders into a yes pile and a no pile (the most information).

#include <Arduboy2.h>
#include <ArduboyFX.h>
#include <ArduboyTones.h>
#include "fxdata.h"
#include "font.h"
#include "lines.h"                                             // everything he says, a few dozen ways

Arduboy2Base ab;
ArduboyTones snd(ab.audio.enabled);

// ------------------------------------------------------------------ text (5x7 capitals, straight into the screen)
int16_t tx_, ty_; uint8_t tc_ = WHITE;
void at(int16_t x, int16_t y) { tx_ = x; ty_ = y; }
void pc(char c) {
  if (c >= 'a' && c <= 'z') c -= 32;
  // (the characters after Z: [ is a degree sign, then the up, down, left and right arrows)
  uint8_t g = (c >= 32 && c <= 95) ? c - 32 : 0, gl[5]; memcpy_P(gl, FONT + g * 5, 5);
  uint8_t* buf = ab.getBuffer(); uint8_t sh = ty_ & 7; int16_t pg = ty_ >> 3;
  for (uint8_t i = 0; i < 5; i++) { int16_t x = tx_ + i; if (x < 0 || x > 127) continue; uint16_t m = (uint16_t)gl[i] << sh;
    for (uint8_t k = 0; k < 2; k++) { int16_t p = pg + k; if (p < 0 || p > 7) continue; uint8_t v = m >> (8 * k); if (tc_) buf[p * 128 + x] |= v; else buf[p * 128 + x] &= ~v; } }
  tx_ += 6;
}
void ps(const char* s) { while (*s) pc(*s++); }
void pp(PGM_P s) { char c; while ((c = pgm_read_byte(s++))) pc(c); }
void pn(uint16_t n) { char b[6]; uint8_t i = 0; do { b[i++] = '0' + n % 10; n /= 10; } while (n); while (i) pc(b[--i]); }
void bigc(int16_t x, int16_t y, char c) {                      // one double size letter (the title)
  uint8_t gl[5]; memcpy_P(gl, FONT + (c - 32) * 5, 5);
  for (uint8_t i = 0; i < 5; i++) for (uint8_t j = 0; j < 7; j++) if (gl[i] >> j & 1) ab.fillRect(x + i * 2, y + j * 2, 2, 2, WHITE); }

const uint8_t TINY[] PROGMEM = {   // 3 x 5 capitals for the title screen, A to Z, one byte a column (bit 0 at the top)
  0x1E,0x05,0x1E, 0x1F,0x15,0x0A, 0x0E,0x11,0x11, 0x1F,0x11,0x0E, 0x1F,0x15,0x11, 0x1F,0x05,0x01, 0x0E,0x11,0x1D, 0x1F,0x04,0x1F,
  0x11,0x1F,0x11, 0x08,0x10,0x0F, 0x1F,0x04,0x1B, 0x1F,0x10,0x10, 0x1F,0x06,0x1F, 0x1F,0x01,0x1E, 0x0E,0x11,0x0E, 0x1F,0x05,0x02,
  0x0E,0x19,0x16, 0x1F,0x05,0x1A, 0x12,0x15,0x09, 0x01,0x1F,0x01, 0x1F,0x10,0x1F, 0x0F,0x10,0x0F, 0x1F,0x0C,0x1F, 0x1B,0x04,0x1B,
  0x03,0x1C,0x03, 0x19,0x15,0x13 };
uint8_t tinyW(PGM_P s) { uint8_t w = 0; char c; while ((c = pgm_read_byte(s++))) w += (c == ' ') ? 3 : 4; return w ? w - 1 : 0; }   // width in pixels
void tiny(int16_t x, int16_t y, PGM_P s, uint8_t n = 255) {   // small letters (the first n of them), in the current colour
  char c; while ((c = pgm_read_byte(s++)) && n--) { if (c == ' ') { x += 3; continue; }
    for (uint8_t i = 0; i < 3; i++) { uint8_t b = pgm_read_byte(TINY + (c - 'A') * 3 + i); for (uint8_t j = 0; j < 5; j++) if (b >> j & 1) ab.drawPixel(x + i, y + j, tc_); }
    x += 4; } }

char txt[240];                                                 // the words on the screen right now
uint8_t tl;
void tclear() { tl = 0; txt[0] = 0; }
void tadd(const char* s) { while (*s && tl < 238) txt[tl++] = *s++; txt[tl] = 0; }
void taddP(PGM_P s) { char c; while ((c = pgm_read_byte(s++)) && tl < 238) txt[tl++] = c; txt[tl] = 0; }
void taddN(uint16_t n);
void taddL(PGM_P all, uint8_t n, uint8_t num = 0) {            // adds line n of a list of lines (one per '\n'); a '#' in it becomes num
  while (n) if (pgm_read_byte(all++) == '\n') n--;
  char c; while ((c = pgm_read_byte(all++)) && c != '\n' && tl < 238) { if (c == '#') taddN(num); else txt[tl++] = c; } txt[tl] = 0; }
void taddN(uint16_t n) { char b[6]; uint8_t i = 0; do { b[i++] = '0' + n % 10; n /= 10; } while (n); while (i && tl < 238) txt[tl++] = b[--i]; txt[tl] = 0; }
uint8_t page;                                                  // ('|' in txt splits it into pages, shown one at a time)
uint8_t pages() { uint8_t n = 1; for (const char* p = txt; *p; p++) if (*p == '|') n++; return n; }
uint8_t wrap(int16_t x, int16_t y, uint8_t cols, uint8_t rows, uint8_t pg = 0) {   // draws txt (page pg of it) word-wrapped; returns the lines used
  // Lines break at spaces. Words are never cut in two: a long hyphenated word breaks after a hyphen, a word that only overflows
  // because of the dots after it lets the dots start the next line, and only a word too long for a whole line is split, with a hyphen.
  const char* s = txt; uint8_t line = 0;
  for (uint8_t k = pg; k && *s; s++) if (*s == '|') k--;
  while (*s && *s != '|' && line < rows) {
    while (*s == ' ') s++;
    if (!*s || *s == '|') break;
    const char *brk = 0, *dots = 0; uint8_t n = 0;
    while (s[n] && s[n] != '|' && n < cols) {
      if (s[n] == ' ') brk = s + n;                              // (break at a space...)
      else if (s[n] == '-' && n + 1 < cols) brk = s + n + 1;     // (...or just after a hyphen)
      else if (s[n] == '.' && n && s[n - 1] != '.' && s[n - 1] != ' ') dots = s + n;   // (...or, failing those, before a run of dots)
      n++; }
    const char* end; bool hy = false;
    if (!s[n] || s[n] == '|' || s[n] == ' ') end = s + n;        // it all fits, or the line ends exactly at a space
    else if (s[n] == '.' && s[n - 1] != '.' && s[n - 1] != ' ' && !brk) end = s + n;   // a word that fills the line exactly, its dots to follow
    else if (brk) end = brk; else if (dots) end = dots;
    else { end = s + cols - 1; hy = true; }                      // one word longer than the line: split it with a hyphen
    at(x, y + line * 9); for (const char* p = s; p < end; p++) pc(*p); if (hy) pc('-');
    s = end; line++;
  }
  return line;
}

// ------------------------------------------------------------------ the brain
// No score is kept for each thing (there are too many for the Arduboy's memory). Instead the answers so far are remembered,
// and the scores are worked out fresh from them each time, a slice of the table at a time, keeping only the leaders.
uint8_t asked[(NQ + 7) / 8];                                   // the questions already asked
bool wasAsked(uint8_t q) { return asked[q >> 3] >> (q & 7) & 1; }
const int8_t DELTA[4][5] PROGMEM = {                           // how an answer moves a thing's score, by how that thing answers (no, rarely, sometimes, usually, yes)
  { -4, 0, 0, 3, 4 },                                          // YES (a "rarely" thing is not punished: people often say yes to those)
  { 4, 3, 0, 0, -4 },                                          // NO
  { -2, -2, 2, -2, -2 },                                       // UNKNOWN (people say it when a thing is neither one nor the other)
  { -5, 0, 3, 0, -5 } };                                       // SOMETIMES (tuned in art/fastsim.py)
const uint8_t MAXH = 26, MAXW = 16;
uint8_t hq[MAXH], ha[MAXH], nh;                                // the questions answered so far, and the answers
uint16_t wrong[MAXW]; bool wrongOut[MAXW]; uint8_t nw;         // things he guessed wrongly (ruled out, or just doubted)
uint8_t cat;                                                   // the group picked at the start (0 animal .. 3 other)
const uint8_t K = 48;                                          // how many leaders a question is judged on
const uint8_t WGT[19] PROGMEM = { 64, 51, 40, 32, 25, 20, 16, 13, 10, 8, 6, 5, 4, 3, 3, 2, 2, 2, 1 };   // a leader's say in picking the question: it halves for every 3 points it trails the best (tuned in art/fastsim.py)
uint16_t top[K]; int16_t tops[K]; uint8_t nTop;

void leaders() {                                               // the K best scoring things, best first
  const uint8_t CH = 128; int16_t buf[CH];
  nTop = 0;
  for (uint16_t base = 0; base < NOBJ; base += CH) {
    uint8_t n = (NOBJ - base < CH) ? NOBJ - base : CH;
    FX::seekData(CATS + base);                                 // start: in the picked group or not, less a little for thin entries
    for (uint8_t i = 0; i < n; i++) { uint8_t c = (i == n - 1) ? FX::readEnd() : FX::readPendingUInt8(); buf[i] = ((c >> cat & 1) ? 5 : -5) - (c >> 4) * 2; }
    for (uint8_t h = 0; h < nh; h++) {                         // then every answer so far
      FX::seekData(MATQ + (uint24_t)hq[h] * NOBJ + base); const int8_t* d = DELTA[ha[h]];
      for (uint8_t i = 0; i < n; i++) { uint8_t v = (i == n - 1) ? FX::readEnd() : FX::readPendingUInt8(); buf[i] += (int8_t)pgm_read_byte(d + v); }
    }
    for (uint8_t w = 0; w < nw; w++) if (wrong[w] >= base && wrong[w] < base + n) { if (wrongOut[w]) buf[wrong[w] - base] = -30000; else buf[wrong[w] - base] -= 40; }
    for (uint8_t i = 0; i < n; i++) {
      int16_t s = buf[i]; uint8_t p = nTop;
      while (p > 0 && tops[p - 1] < s) p--;
      if (p >= K) continue;
      for (uint8_t j = (nTop < K ? nTop : K - 1); j > p; j--) { top[j] = top[j - 1]; tops[j] = tops[j - 1]; }
      top[p] = base + i; tops[p] = s; if (nTop < K) nTop++;
    }
  }
}

uint8_t answerOf(uint16_t obj, uint8_t q) { FX::seekData(MATQ + (uint24_t)q * NOBJ + obj); return FX::readEnd(); }

uint8_t pickQuestion() {                                       // the unasked question that best splits the leaders
  int16_t t = tops[0]; uint8_t w[K];
  for (uint8_t k = 0; k < nTop; k++) { int16_t d = t - tops[k]; w[k] = d > 18 ? 1 : pgm_read_byte(WGT + d); }
  uint32_t best[3] = { 0, 0, 0 }; uint8_t bq[3] = { 255, 255, 255 };
  for (uint8_t q = 0; q < NQ; q++) {
    if (wasAsked(q)) continue;
    uint16_t y = 0, n = 0, s = 0;
    for (uint8_t k = 0; k < nTop; k++) { uint8_t v = answerOf(top[k], q); if (v >= 3) y += w[k]; else if (v <= 1) n += w[k]; else s += w[k]; }
    uint32_t tot = y + n + s, g = tot * tot - (uint32_t)y * y - (uint32_t)n * n - (uint32_t)s * s;   // how evenly it splits them
    FX::seekData(QWT + q); g = g * FX::readEnd() / 8;            // (some questions, like colours, are saved for later: they feel random early on)
    for (uint8_t j = 0; j < 3; j++) if (g > best[j] || bq[j] == 255) { for (uint8_t m = 2; m > j; m--) { best[m] = best[m - 1]; bq[m] = bq[m - 1]; } best[j] = g; bq[j] = q; break; }
  }
  uint8_t c = 1; while (c < 3 && bq[c] != 255 && best[c] >= best[0] - best[0] / 10) c++;   // a little variety among near-equal best ones
  return bq[random(c)];
}

bool isWrong(uint16_t o) { for (uint8_t w = 0; w < nw; w++) if (wrong[w] == o) return true; return false; }
void apply(uint8_t q, uint8_t ans) { if (nh < MAXH) { hq[nh] = q; ha[nh] = ans; nh++; } }   // an answer: remembered

// ------------------------------------------------------------------ the game: THE GREAT ZANDOR, the fortune teller in the booth
enum { S_TITLE, S_THINK, S_CAT, S_ASK, S_GUESS, S_MORE, S_WIN, S_LOSE, S_PONDER, S_SAY, S_OFFER, S_FUTURE };
uint8_t tmr, line_, line2_, lastMutter = 255;                  // frames in this screen; which of its lines he says
uint8_t st = S_TITLE, sel, qn, curQ; uint16_t guessObj; bool finalGuess;
char nm[NAMELEN];

void beep() { snd.tone(1200, 15); }
void blip() { snd.tone(880, 30, 1320, 40); }
void eerie() { snd.tone(233, 120, 220, 120, 208, 300); }       // a low, creepy slide down

uint8_t fKind; uint16_t fIdx, lastFort = 0xFFFF;              // the future he tells: 0 a fortune (number fIdx), 1 the lucky number, 2 the unlucky one
void offer() { st = S_OFFER; tmr = 0; page = 0; sel = 0; line_ = random(N_OFFERS); eerie(); }   // after the game: would you like to hear your future?
void newGame() { line_ = random(N_INTROS); tmr = 0; page = 0; nh = 0; nw = 0; cat = 0; memset(asked, 0, sizeof asked); qn = 1; sel = 0; st = S_THINK; }

void next() {                                                  // after an answer: ask another question, or guess
  leaders();
  int16_t m = tops[0] - tops[1];
  if (qn >= 25) { st = S_LOSE; tmr = 0; page = 0; line_ = random(N_LOSES); snd.tone(523, 150, 392, 150, 262, 300); return; }
  bool guess = (qn == 20) || (qn >= 10 && m >= 20) || (qn > 21 && m >= 10) || qn == 24;   // (21 questions, then four more, 25 in all; tuned in art/fastsim.py)
  qn++; sel = 0;                                                // (the YES box lit to start)
  if (guess) { uint8_t g = 0; while (g + 1 < nTop && isWrong(top[g])) g++; guessObj = top[g];   // (never the same wrong guess twice)
    finalGuess = (qn == 21 || qn == 25); FX::readDataBytes(NAMES + (uint24_t)guessObj * NAMELEN, (uint8_t*)nm, NAMELEN); st = S_PONDER; tmr = 0; page = 0;
    line_ = random(finalGuess ? N_PONDERF : N_PONDERS); }
  else { curQ = pickQuestion(); asked[curQ >> 3] |= 1 << (curQ & 7); st = S_ASK;
    if (qn == 6 || qn == 11 || qn == 16) { st = S_SAY; tmr = 0; page = 0; uint8_t l; do l = random(N_MUTTERS); while (l == lastMutter); lastMutter = line_ = l; line2_ = random(2); } }   // now and then he mutters something first (never the same one twice in a row)
}

// the four answers in four boxes, two by two: the arrows move the highlight between them, B answers.
void choices(PGM_P const* L) {
  for (uint8_t i = 0; i < 4; i++) {
    int16_t x = (i & 1) ? 65 : 0, y = (i & 2) ? 51 : 37;
    if (i == sel) { ab.fillRoundRect(x, y, 63, 13, 3, WHITE); tc_ = BLACK; }
    else ab.drawRoundRect(x, y, 63, 13, 3, WHITE);
    at(x + 32 - (int16_t)strlen_P(L[i]) * 3, y + 3); pp(L[i]); tc_ = WHITE;
  }
}
bool picked(uint8_t ar) {                                      // arrows move between the boxes; B picks the lit one
  if (ar == 0 || ar == 1) { sel ^= 2; beep(); }                // up / down: the other row
  if (ar == 2 || ar == 3) { sel ^= 1; beep(); }                // left / right: the other column
  return ab.justPressed(B_BUTTON);
}
uint8_t arrowPressed() {                                       // which arrow was just pressed (255: none)
  if (ab.justPressed(UP_BUTTON)) return 0; if (ab.justPressed(DOWN_BUTTON)) return 1;
  if (ab.justPressed(LEFT_BUTTON)) return 2; if (ab.justPressed(RIGHT_BUTTON)) return 3; return 255; }
void frame(uint8_t h = 50) { ab.drawRoundRect(0, 0, 128, h, 4, WHITE); ab.drawRoundRect(1, 1, 126, h - 2, 3, WHITE); }   // the question card (2 pixels thick)
void qlabel(uint8_t y = 30) { at(110 - (qn >= 10 ? 6 : 0), y); pc('Q'); pn(qn); }
uint8_t blinkT = 90;                                           // frames until his next blink (he blinks wherever he is shown)
uint8_t squintT;                                               // frames left of a squint (his eyes narrowed to slits)
uint8_t eyes() {                                               // which picture of him: 0 eyes open, 1 shut (a blink, every few seconds), 2 narrowed
  if (blinkT) blinkT--; else blinkT = 70 + random(110); if (squintT) squintT--;
  return blinkT < 4 ? 1 : (squintT ? 2 : 0); }
uint8_t luckyN, unluckyN;                                      // today's lucky and unlucky numbers, 1 to 99 (picked once when you first start, then kept)
const uint8_t GLINT[] PROGMEM = { 20, 50, 28, 56, 22, 57, 27, 49, 19, 54, 25, 53 };   // spots inside the crystal ball where a twinkle can appear
uint8_t glintAt, glintT;
void drawZandor(int16_t x) {                                    // the fortune teller at x, his crystal ball twinkling now and then
  FX::drawBitmap(x, 0, ZANDOR, eyes(), dbmNormal);
  if (glintT) glintT--; else if (!random(50)) { glintT = 9; glintAt = random(6); }
  if (glintT) { int16_t gx = x + pgm_read_byte(GLINT + glintAt * 2), gy = pgm_read_byte(GLINT + glintAt * 2 + 1); uint8_t r = glintT > 6 ? 9 - glintT : (glintT > 3 ? 2 : glintT - 1);
    ab.drawPixel(gx, gy, WHITE); for (uint8_t k = 1; k <= r; k++) { ab.drawPixel(gx - k, gy, WHITE); ab.drawPixel(gx + k, gy, WHITE); ab.drawPixel(gx, gy - k, WHITE); ab.drawPixel(gx, gy + k, WHITE); } } }
void zandor() { drawZandor(0); }                               // the fortune teller, on the left
bool speak(PGM_P prompt) {                                     // what he says, beside him, a page at a time; true once the last page is up
  ab.drawRoundRect(50, 0, 78, 64, 4, WHITE); ab.drawRoundRect(51, 1, 76, 62, 3, WHITE);
  uint8_t n = pages(); bool last = page >= n - 1;
  wrap(54, 5, 12, (prompt && last) ? 5 : 6, page);         // (12 letters a line, x 54 to 125, inside the bubble's border)
  if (!last) { if (tmr > 100 || (ab.justPressed(B_BUTTON) && tmr > 6)) { page++; tmr = 0; } return false; }   // the next page comes by itself after a little over 3 seconds (or on B)
  if (prompt) { at(124 - strlen_P(prompt) * 6, 53); pp(prompt); }
  return true;
}

const char S_YES[] PROGMEM = "YES", S_NO[] PROGMEM = "NO", S_UNK[] PROGMEM = "UNKNOWN", S_SOME[] PROGMEM = "SOMETIMES";
const char S_AN[] PROGMEM = "ANIMAL", S_VEG[] PROGMEM = "PLANT", S_MIN[] PROGMEM = "MAN-MADE", S_OTH[] PROGMEM = "OTHER";
PGM_P const CATL[4] = { S_AN, S_VEG, S_MIN, S_OTH };
PGM_P const ANS[4] = { S_YES, S_NO, S_SOME, S_UNK };          // (box order: top left, top right, bottom left, bottom right)
const uint8_t ANSV[4] = { 0, 1, 3, 2 };                        // box -> answer: yes, no, sometimes, unknown

void setup() {
  ab.boot(); ab.display(); FX::begin(FX_DATA_PAGE); ab.flashlight(); ab.systemButtons(); ab.audio.begin(); ab.setFrameRate(30); ab.waitNoButtons();
}

void loop() {
  if (!ab.nextFrame()) return;
  ab.pollButtons(); if (tmr < 255) tmr++;
  bool B = ab.justPressed(B_BUTTON); uint8_t ar = arrowPressed();
  switch (st) {
    case S_TITLE:
      // Zandor in his booth on the right: a framed cabinet window with a curtain swag in each top corner, each pinned with a jewel,
      // a jewel hanging from a cord below it, and now and then one of them glints
      if (!random(240)) squintT = 30;                          // (now and then he narrows his eyes at you)
      drawZandor(78);
      ab.drawRect(76, 0, 52, 64, WHITE); ab.drawRect(77, 1, 50, 62, WHITE);
      for (uint8_t i = 0; i < 9; i++) { uint8_t h = 11 - i - (i > 5 ? i - 5 : 0); ab.drawFastVLine(78 + i, 2, h, WHITE); ab.drawFastVLine(125 - i, 2, h, WHITE); }
      for (uint8_t sd = 0; sd < 2; sd++) {
        int16_t x = sd ? 123 : 80;                             // (the middle of each corner's decorations)
        ab.drawPixel(x, 4, BLACK); ab.drawPixel(x - 1, 5, BLACK); ab.drawPixel(x + 1, 5, BLACK); ab.drawPixel(x, 6, BLACK);   // the brooch pinning the swag
        ab.drawPixel(x, 14, WHITE); ab.drawPixel(x, 16, WHITE);   // the cord
        for (uint8_t j = 0; j < 3; j++) { ab.drawFastHLine(x - j, 18 + j, j * 2 + 1, WHITE); ab.drawFastHLine(x - j, 22 - j, j * 2 + 1, WHITE); }   // a jewel: a diamond...
        ab.drawPixel(x, 20, BLACK);                            // ...with a dark heart
        ab.drawPixel(x, 24, WHITE); ab.drawPixel(x, 26, WHITE); ab.drawPixel(x, 28, WHITE);   // and a tassel of beads under it
      }
      { uint8_t g = ab.frameCount & 127;                         // a glint: every four seconds or so, a sparkle crosses one of the jewels
        if (g < 8) { int16_t x = (ab.frameCount & 128) ? 123 : 80, r = g < 4 ? g : 8 - g;
          ab.drawPixel(x - 3 - r, 20, WHITE); ab.drawPixel(x + 3 + r, 20, WHITE); ab.drawPixel(x, 20, WHITE); } }   // (and its dark heart flashes white)
      // the words, each line centred in the column (76 wide); ZANDOR's letters ripple gently, like a sign under water
      at(11, 3); pp(PSTR("THE GREAT"));
      for (uint8_t i = 0; i < 6; i++) { uint8_t ph = ((ab.frameCount >> 3) + 8 - i) & 7;
        int8_t dy = (ph == 1 || ph == 2) ? -1 : ((ph == 5 || ph == 6) ? 1 : 0); bigc(2 + i * 12, 14 + dy, pgm_read_byte(PSTR("ZANDOR") + i)); }
      tiny(38 - tinyW(PSTR("SEES ALL")) / 2, 32, PSTR("SEES ALL"), tmr < 40 ? 0 : (tmr - 40) / 4);   // (spelled out a letter at a time, then stays)
      // sound: two boxes, ON and OFF. Left / right picks one (the lit box is how it is set)
      { bool on = ab.audio.enabled();                           // (small boxes, low down, a good gap under SEES ALL)
        tiny(14, 46, PSTR("SOUND"));
        if (on) { ab.fillRect(36, 44, 11, 9, WHITE); tc_ = BLACK; } else ab.drawRect(36, 44, 11, 9, WHITE);
        tiny(38, 46, PSTR("ON")); tc_ = WHITE;
        if (!on) { ab.fillRect(48, 44, 15, 9, WHITE); tc_ = BLACK; } else ab.drawRect(48, 44, 15, 9, WHITE);
        tiny(50, 46, PSTR("OFF")); tc_ = WHITE;
        if (ab.justPressed(LEFT_BUTTON) && !on) { ab.audio.on(); ab.audio.saveOnOff(); beep(); }
        if (ab.justPressed(RIGHT_BUTTON) && on) { ab.audio.off(); ab.audio.saveOnOff(); } }
      // along the bottom: PRESS (a round button, like the real ones, gently pulsing) TO ENTER
      tiny(8, 56, PSTR("PRESS"));
      ab.drawCircle(33, 58, 3, WHITE); if ((ab.frameCount & 31) < 16) ab.fillCircle(33, 58, 2, WHITE);
      tiny(40, 56, PSTR("TO ENTER"));
      if (B || ab.justPressed(A_BUTTON)) { randomSeed(micros()); if (!luckyN) { luckyN = 1 + random(99); do unluckyN = 1 + random(99); while (unluckyN == luckyN); } newGame(); eerie(); }   // (either button starts)
      break;
    case S_THINK:
      zandor(); tclear();
      taddL(INTROS, line_ % N_INTROS);
      if (speak(PSTR("B: YES")) && B && tmr > 6) { st = S_CAT; sel = 0; blip(); }
      break;
    case S_SAY:                                                // a mutter between questions
      zandor(); tclear();
      taddL(MUTTERS, line_ % N_MUTTERS);
      if (line2_) squintT = 2;                                  // (half the time he narrows his eyes as he says it)
      speak(0);
      if (tmr == 2) snd.tone(196, 200, 185, 300);
      if (tmr > 105 || (B && tmr > 8)) { st = S_ASK; sel = 0; }
      break;
    case S_PONDER:                                             // a moment's thought before a guess (the dots appear one by one)
      zandor(); tclear();
      if (finalGuess) taddL(PONDERF, line_ % N_PONDERF); else taddL(PONDERS, line_ % N_PONDERS);
      squintT = 2;                                             // (he squints into the crystal)
      for (uint8_t d = 0; d < 3 && tmr > 10 + d * 12; d++) tadd(".");
      speak(0);
      if (tmr == 12 || tmr == 24 || tmr == 36) snd.tone(220 - (tmr / 12) * 12, 60);
      if (tmr > 90) { st = S_GUESS; sel = 0; }
      break;
    case S_CAT:                                                // question 1: what kind of thing are you looking at? Four boxes.
      frame(35); tclear(); taddP(PSTR("WHAT HOLDS YOUR GAZE? IS IT...")); wrap(5, 4, 19, 3); qlabel(26);
      choices(CATL);
      if (picked(ar)) { cat = sel; blip(); next(); }           // (the boxes are bits 0 animal, 1 plant, 2 man-made, 3 other in the table; a few things sit in two)
      break;
    case S_ASK:
      frame(35); tclear(); { char q[QLEN]; FX::readDataBytes(QTEXT + (uint24_t)curQ * QLEN, (uint8_t*)q, QLEN); tadd(q); } wrap(5, 4, 19, 3); qlabel(26);
      choices(ANS);
      if (picked(ar)) { apply(curQ, ANSV[sel]); blip(); next(); }
      break;
    case S_GUESS:
      tclear(); if (finalGuess) taddP(PSTR("I SEE IT CLEARLY... IT IS ")); else taddP(PSTR("YOUR EYES SAY... IS IT "));
      tadd(nm); tadd("?"); frame(35); wrap(5, 4, 19, 3); qlabel(26);
      choices(ANS);
      if (picked(ar)) {
        if (sel == 0) { st = S_WIN; tmr = 0; page = 0; line_ = random(N_WINS); line2_ = random(N_WINEND); snd.tone(330, 90, 311, 90, 494, 300); }
        else { if (nw < MAXW) { wrong[nw] = guessObj; wrongOut[nw] = sel == 1; nw++; } blip(); if (qn == 21) { st = S_MORE; tmr = 0; page = 0; line_ = random(N_MOREA); } else next(); }   // (sometimes / unknown: not ruled out, just doubted)
      }
      break;
    case S_MORE:                                               // wrong at 21: it keeps going
      zandor(); tclear(); taddL(MOREA, line_); if (page > 0 || tmr > 40) { taddL(MOREB, line_); if (!page) squintT = 2; } taddP(PSTR("|")); taddL(MOREC, line_);
      if (tmr == 41 && !page) snd.tone(392, 60, 370, 60, 349, 200);
      if (speak(PSTR("B: GO ON")) && B && tmr > 6) { blip(); next(); }
      break;
    case S_WIN:
      zandor(); tclear();
      taddL(WINS, line_ % N_WINS);
      taddP(PSTR("|IT IS ")); tadd(nm); taddL(WINEND, line2_ % N_WINEND);   // (every ending fits the longest names)
      if (page) squintT = 2;                                   // (a smug squint as he names it)
      if (speak(PSTR("B: GO ON")) && B && tmr > 6) offer();
      break;
    case S_LOSE:
      zandor(); tclear(); taddL(LOSES, line_ % N_LOSES);
      if (speak(PSTR("B: GO ON")) && B && tmr > 6) offer();
      break;
    case S_OFFER:                                              // after the game: would you like to hear your future? YES or NO
      zandor(); tclear(); taddL(OFFERS, line_ % N_OFFERS); speak(0);
      for (uint8_t i = 0; i < 2; i++) { int16_t x = 56 + i * 34;
        if (i == sel) { ab.fillRoundRect(x, 49, 30, 11, 2, WHITE); tc_ = BLACK; } else ab.drawRoundRect(x, 49, 30, 11, 2, WHITE);
        at(x + (i ? 9 : 6), 51); pp(i ? PSTR("NO") : PSTR("YES")); tc_ = WHITE; }
      if (ar == 2 || ar == 3) { sel ^= 1; beep(); }
      if (B && tmr > 6) {
        if (sel) { st = S_TITLE; tmr = 0; blip(); }           // NO: back to the home screen
        else {                                                 // YES: about one time in four, a number for today; otherwise a fortune
          st = S_FUTURE; tmr = 0; page = 0; snd.tone(196, 150, 247, 150, 294, 300);
          uint8_t r = random(8); fKind = r == 0 ? 1 : (r == 1 ? 2 : 0); line_ = random(N_LUCKY);
          uint16_t f; do f = random(NFORT); while (f == lastFort && NFORT > 1); lastFort = fIdx = f; } }
      break;
    case S_FUTURE:                                             // the mists swirl for a moment, then his fortune for your next 24 hours
      zandor(); tclear(); squintT = 2;
      if (tmr < 50) { taddP(PSTR("THE MISTS SWIRL")); for (uint8_t d = 0; d < 3 && tmr > 5 + d * 12; d++) tadd("."); speak(0); break; }
      if (tmr == 50) snd.tone(988, 60, 1319, 120);
      if (fKind == 1) { taddP(PSTR("TODAY YOUR LUCKY NUMBER IS ")); taddN(luckyN); taddP(PSTR(".|")); taddL(LUCKY, line_ % N_LUCKY); }
      else if (fKind == 2) { taddP(PSTR("TODAY YOUR UNLUCKY NUMBER IS ")); taddN(unluckyN); taddP(PSTR(".|")); taddL(UNLUCKY, line_ % N_UNLUCKY); }
      else { char f[FORTLEN]; FX::readDataBytes(FORTS + (uint24_t)fIdx * FORTLEN, (uint8_t*)f, FORTLEN); tadd(f); }
      if (speak(PSTR("B: OK")) && B && tmr > 56) { st = S_TITLE; tmr = 0; blip(); }   // back to the home screen
      break;
  }
  FX::display(true);                                           // (show the screen and clear it for the next frame)
}
