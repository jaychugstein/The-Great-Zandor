// THE GREAT ZANDOR - a 21 questions guessing game for the Arduboy FX, in the spirit of the 2000s handheld guessing toys,
// hosted by a creepy fortune teller in his booth.
// Think of something. It asks "Animal, Vegetable or Other?", then up to 21 yes / no questions, guessing along
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
void big(int16_t x, int16_t y, PGM_P s) {                     // double size letters (the title)
  char c; while ((c = pgm_read_byte(s++))) { uint8_t g = c - 32, gl[5]; memcpy_P(gl, FONT + g * 5, 5);
    for (uint8_t i = 0; i < 5; i++) for (uint8_t j = 0; j < 7; j++) if (gl[i] >> j & 1) ab.fillRect(x + i * 2, y + j * 2, 2, 2, WHITE);
    x += 12; } }

char txt[140];                                                 // the words on the screen right now
uint8_t tl;
void tclear() { tl = 0; txt[0] = 0; }
void tadd(const char* s) { while (*s && tl < 138) txt[tl++] = *s++; txt[tl] = 0; }
void taddP(PGM_P s) { char c; while ((c = pgm_read_byte(s++)) && tl < 138) txt[tl++] = c; txt[tl] = 0; }
void taddN(uint16_t n) { char b[6]; uint8_t i = 0; do { b[i++] = '0' + n % 10; n /= 10; } while (n); while (i && tl < 138) txt[tl++] = b[--i]; txt[tl] = 0; }
uint8_t page;                                                  // ('|' in txt splits it into pages, shown one at a time)
uint8_t pages() { uint8_t n = 1; for (const char* p = txt; *p; p++) if (*p == '|') n++; return n; }
uint8_t wrap(int16_t x, int16_t y, uint8_t cols, uint8_t rows, uint8_t pg = 0) {   // draws txt (page pg of it) word-wrapped; returns the lines used
  const char* s = txt; uint8_t line = 0;
  for (uint8_t k = pg; k && *s; s++) if (*s == '|') k--;
  while (*s && *s != '|' && line < rows) {
    while (*s == ' ') s++;
    const char* e = s; const char* cut = 0; uint8_t n = 0;
    while (e[n] && e[n] != '|' && n < cols) { if (e[n] == ' ') cut = e + n; n++; }
    const char* end = (e[n] == 0 || e[n] == '|') ? e + n : (e[n] == ' ' ? e + n : (cut ? cut : e + n));
    at(x, y + line * 9); for (const char* p = s; p < end; p++) pc(*p);
    s = end; line++;
  }
  return line;
}

// ------------------------------------------------------------------ the brain
// No score is kept for each thing (there are too many for the Arduboy's memory). Instead the answers so far are remembered,
// and the scores are worked out fresh from them each time, a slice of the table at a time, keeping only the leaders.
uint8_t asked[(NQ + 7) / 8];                                   // the questions already asked
bool wasAsked(uint8_t q) { return asked[q >> 3] >> (q & 7) & 1; }
const int8_t DELTA[4][5] PROGMEM = {                           // how an answer moves a thing's score, by how that thing answers (no .. yes)
  { -4, -2, 1, 2, 4 },                                         // YES
  { 4, 2, 1, -2, -4 },                                         // NO
  { 0, 0, 0, 0, 0 },                                           // UNKNOWN
  { -3, 1, 4, 1, -3 } };                                       // SOMETIMES
const uint8_t MAXH = 26, MAXW = 10;
uint8_t hq[MAXH], ha[MAXH], nh;                                // the questions answered so far, and the answers
uint16_t wrong[MAXW]; bool wrongOut[MAXW]; uint8_t nw;         // things he guessed wrongly (ruled out, or just doubted)
uint8_t cat;                                                   // the group picked at the start (0 animal .. 3 other)
const uint8_t K = 32;                                          // how many leaders a question is judged on
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

void apply(uint8_t q, uint8_t ans) { if (nh < MAXH) { hq[nh] = q; ha[nh] = ans; nh++; } }   // an answer: remembered

// ------------------------------------------------------------------ the game: THE GREAT ZANDOR, the fortune teller in the booth
enum { S_TITLE, S_THINK, S_CAT, S_ASK, S_GUESS, S_MORE, S_WIN, S_LOSE, S_PONDER, S_SAY };
uint8_t tmr, line_;                                            // frames in this screen; which of its lines he says
uint8_t st = S_TITLE, sel, qn, curQ; uint16_t guessObj; bool finalGuess;
char nm[NAMELEN];

void beep() { snd.tone(1200, 15); }
void blip() { snd.tone(880, 30, 1320, 40); }
void eerie() { snd.tone(233, 120, 220, 120, 208, 300); }       // a low, creepy slide down

void newGame() { line_ = random(4); tmr = 0; page = 0; nh = 0; nw = 0; cat = 0; memset(asked, 0, sizeof asked); qn = 1; sel = 0; st = S_THINK; }

void next() {                                                  // after an answer: ask another question, or guess
  leaders();
  int16_t m = tops[0] - tops[1];
  if (qn >= 25) { st = S_LOSE; tmr = 0; page = 0; snd.tone(523, 150, 392, 150, 262, 300); return; }
  bool guess = (qn == 20) || (qn >= 10 && m >= 20) || (qn > 21 && m >= 10) || qn == 24;   // (21 questions, then four more, 25 in all; tuned in art/fastsim.py)
  qn++; sel = 0;                                                // (the YES box lit to start)
  if (guess) { guessObj = top[0]; finalGuess = (qn == 21 || qn == 25); FX::readDataBytes(NAMES + (uint24_t)guessObj * NAMELEN, (uint8_t*)nm, NAMELEN); st = S_PONDER; tmr = 0; page = 0; }
  else { curQ = pickQuestion(); asked[curQ >> 3] |= 1 << (curQ & 7); st = S_ASK;
    if (qn == 6 || qn == 11 || qn == 16) { st = S_SAY; tmr = 0; page = 0; uint8_t l; do l = random(12); while (l == line_); line_ = l; } }   // now and then he mutters something first
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
void frame(uint8_t h = 50) { ab.drawRoundRect(0, 0, 128, h, 4, WHITE); ab.drawRoundRect(1, 1, 126, h - 2, 3, WHITE); }   // the question card (2 pixels thick)   // the question card (2 pixels thick)
void qlabel(uint8_t y = 30) { at(110 - (qn >= 10 ? 6 : 0), y); pc('Q'); pn(qn); }
uint8_t blinkT = 90;                                           // frames until his next blink (he blinks wherever he is shown)
uint8_t eyes() { if (blinkT) blinkT--; else blinkT = 70 + random(110); return blinkT < 4 ? 1 : 0; }   // 1 while his eyes are shut (a few frames, every few seconds)
void zandor() { FX::drawBitmap(0, 0, ZANDOR, eyes(), dbmNormal); }   // the fortune teller, on the left
bool speak(PGM_P prompt) {                                     // what he says, beside him, a page at a time; true once the last page is up
  ab.drawRoundRect(50, 0, 78, 64, 4, WHITE); ab.drawRoundRect(51, 1, 76, 62, 3, WHITE);
  uint8_t n = pages(); bool last = page >= n - 1;
  wrap(56, 5, 11, (prompt && last) ? 5 : 6, page);
  if (!last) { if (tmr > 70 || (ab.justPressed(B_BUTTON) && tmr > 6)) { page++; tmr = 0; } return false; }   // the next page comes by itself (or on B)
  if (prompt) { at(124 - strlen_P(prompt) * 6, 53); pp(prompt); }
  return true;
}

const char S_YES[] PROGMEM = "YES", S_NO[] PROGMEM = "NO", S_UNK[] PROGMEM = "UNKNOWN", S_SOME[] PROGMEM = "SOMETIMES";
const char S_AN[] PROGMEM = "ANIMAL", S_VEG[] PROGMEM = "VEGETABLE", S_OTH[] PROGMEM = "OTHER";
PGM_P const ANS[4] = { S_YES, S_NO, S_SOME, S_UNK };          // (in arrow order: up, down, left, right)
const uint8_t ANSV[4] = { 0, 1, 3, 2 };                        // arrow -> answer: yes, no, sometimes, unknown

void setup() {
  ab.boot(); ab.display(); FX::begin(FX_DATA_PAGE); ab.flashlight(); ab.systemButtons(); ab.audio.begin(); ab.setFrameRate(30); ab.waitNoButtons();
}

void loop() {
  if (!ab.nextFrame()) return;
  ab.pollButtons(); if (tmr < 255) tmr++;
  bool B = ab.justPressed(B_BUTTON); uint8_t ar = arrowPressed();
  switch (st) {
    case S_TITLE:
      // Zandor in his booth on the right: a framed cabinet window with a curtain swag in each top corner
      FX::drawBitmap(78, 0, ZANDOR, eyes(), dbmNormal);
      ab.drawRect(76, 0, 52, 64, WHITE); ab.drawRect(77, 1, 50, 62, WHITE);
      for (uint8_t i = 0; i < 9; i++) { uint8_t h = 11 - i - (i > 5 ? i - 5 : 0); ab.drawFastVLine(78 + i, 2, h, WHITE); ab.drawFastVLine(125 - i, 2, h, WHITE); }
      ab.drawPixel(79, 14, WHITE); ab.drawPixel(79, 16, WHITE); ab.drawPixel(124, 14, WHITE); ab.drawPixel(124, 16, WHITE);   // (the curtain cords)
      // the words, each line centred under the last (the column is 76 wide)
      at(11, 3); pp(PSTR("THE GREAT")); big(2, 13, PSTR("ZANDOR")); at(14, 31); pp(PSTR("SEES ALL"));
      if (ab.audio.enabled()) { at(14, 45); pp(PSTR("SOUND ON")); } else { at(11, 45); pp(PSTR("SOUND OFF")); }
      at(14, 55); pp(PSTR("B: ENTER"));
      if (ab.justPressed(UP_BUTTON) || ab.justPressed(DOWN_BUTTON)) { if (ab.audio.enabled()) ab.audio.off(); else ab.audio.on(); ab.audio.saveOnOff(); }
      if (B) { randomSeed(micros()); newGame(); eerie(); }
      break;
    case S_THINK:
      zandor(); tclear();
      if (line_ & 1) taddP(PSTR("AH... A VISITOR. COME CLOSER. CLOSER.|I HAVE BEEN EXPECTING YOU.|THINK OF SOMETHING. DO NOT TRY TO HIDE IT."));
      else taddP(PSTR("THE BOOTH IS COLD TONIGHT...|HOLD A THOUGHT IN YOUR MIND, MORTAL.|I WILL TAKE IT FROM YOU."));
      if (speak(PSTR("B: YES")) && B && tmr > 6) { st = S_CAT; sel = 0; blip(); }
      break;
    case S_SAY:                                                // a mutter between questions
      zandor(); tclear();
      { const char* const L[12] = { PSTR("YOUR MIND IS A HOUSE WITH THE DOOR LEFT OPEN..."), PSTR("I CAN HEAR YOUR THOUGHTS SCRATCHING AT THE GLASS..."),
          PSTR("DON'T LOOK BEHIND YOU. JUST ANSWER."), PSTR("THE SPIRITS ARE LAUGHING AT YOU..."), PSTR("YOUR SECRETS ARE SO... DELICIOUS."),
          PSTR("A HUNDRED YEARS IN THIS BOX. I KNOW EVERYTHING."), PSTR("THE LAST ONE WHO LIED TO ME... IS STILL HERE."),
          PSTR("SOMETHING IN THE DARK JUST SAID YOUR NAME."), PSTR("KEEP STILL. I AM COUNTING YOUR HEARTBEATS."),
          PSTR("THE CANDLE BENDS TOWARD YOU. IT LIKES YOU."), PSTR("I HAVE WORN FACES LIKE YOURS BEFORE."),
          PSTR("YOUR COIN WAS COLD. SO WERE YOUR HANDS.") }; taddP(L[line_ % 12]); }
      speak(0);
      if (tmr == 2) snd.tone(196, 200, 185, 300);
      if (tmr > 75 || (B && tmr > 8)) { st = S_ASK; sel = 0; }
      break;
    case S_PONDER:                                             // a moment's thought before a guess (the dots appear one by one)
      zandor(); tclear();
      if (finalGuess) taddP(PSTR("THE GLASS GROWS COLD... I SEE IT")); else if (qn & 1) taddP(PSTR("I AM INSIDE YOUR HEAD NOW")); else taddP(PSTR("SOMETHING STIRS IN THE CRYSTAL"));
      for (uint8_t d = 0; d < 3 && tmr > 10 + d * 12; d++) tadd(".");
      speak(0);
      if (tmr == 12 || tmr == 24 || tmr == 36) snd.tone(220 - (tmr / 12) * 12, 60);
      if (tmr > 60) { st = S_GUESS; sel = 0; }
      break;
    case S_CAT:                                                // question 1: which group. Three boxes: two on top, OTHER wide underneath.
      frame(35); tclear(); taddP(PSTR("TELL ME... ANIMAL, VEGETABLE, OR OTHER?")); wrap(5, 4, 19, 3); qlabel(26);
      { PGM_P const L[3] = { S_AN, S_VEG, S_OTH };
        for (uint8_t i = 0; i < 3; i++) {
          int16_t x = (i == 1) ? 65 : 0, y = (i == 2) ? 51 : 37, w = (i == 2) ? 128 : 63;
          if (i == sel) { ab.fillRoundRect(x, y, w, 13, 3, WHITE); tc_ = BLACK; } else ab.drawRoundRect(x, y, w, 13, 3, WHITE);
          at(x + w / 2 - (int16_t)strlen_P(L[i]) * 3, y + 3); pp(L[i]); tc_ = WHITE;
        } }
      if (ar == 0 || ar == 1) { sel = (sel == 2) ? 0 : 2; beep(); }             // up / down: between the top row and OTHER
      if ((ar == 2 || ar == 3) && sel < 2) { sel ^= 1; beep(); }                 // left / right: along the top row
      if (B) { cat = (sel == 2) ? 3 : sel; blip(); next(); }                     // (the groups are bits 0 animal, 1 vegetable, 3 other in the table)
      break;
    case S_ASK:
      frame(35); tclear(); { char q[QLEN]; FX::readDataBytes(QTEXT + (uint24_t)curQ * QLEN, (uint8_t*)q, QLEN); tadd(q); } wrap(5, 4, 19, 3); qlabel(26);
      choices(ANS);
      if (picked(ar)) { apply(curQ, ANSV[sel]); blip(); next(); }
      break;
    case S_GUESS:
      tclear(); if (finalGuess) taddP(PSTR("I SEE IT CLEARLY... IT IS ")); else taddP(PSTR("THE SPIRITS WHISPER... IS IT "));
      tadd(nm); tadd("?"); frame(35); wrap(5, 4, 19, 3); qlabel(26);
      choices(ANS);
      if (picked(ar)) {
        if (sel == 0) { st = S_WIN; tmr = 0; page = 0; line_ = random(7); snd.tone(330, 90, 311, 90, 494, 300); }
        else { if (nw < MAXW) { wrong[nw] = guessObj; wrongOut[nw] = sel == 1; nw++; } blip(); if (qn == 21) { st = S_MORE; tmr = 0; page = 0; } else next(); }   // (sometimes / unknown: not ruled out, just doubted)
      }
      break;
    case S_MORE:                                               // wrong at 21: it keeps going
      zandor(); tclear(); taddP(PSTR("NO? THEN YOU MAY GO.")); if (page > 0 || tmr > 40) taddP(PSTR(" ...SIT BACK DOWN. HEH HEH HEH.")); taddP(PSTR("|THE SPIRITS DEMAND FOUR MORE. THE DOOR IS LOCKED."));
      if (tmr == 41 && !page) snd.tone(392, 60, 370, 60, 349, 200);
      if (speak(PSTR("B: GO ON")) && B && tmr > 6) { blip(); next(); }
      break;
    case S_WIN:
      zandor(); tclear();
      { const char* const L[7] = { PSTR("YOU CANNOT HIDE A THOUGHT FROM THE DEAD..."), PSTR("NOTHING ESCAPES ZANDOR."), PSTR("I SAW IT BEFORE YOU DID."),
          PSTR("DID YOU REALLY THINK YOU COULD HIDE IT FROM ME?"), PSTR("DELICIOUS. ANOTHER MIND READ."), PSTR("IT WAS WRITTEN ON THE INSIDE OF YOUR SKULL."),
          PSTR("THE GLASS NEVER LIES. NEITHER DO I.") }; taddP(L[line_ % 7]); }
      taddP(PSTR("|IT IS ")); tadd(nm); taddP(PSTR("... HEH HEH HEH."));
      if (speak(PSTR("B: AGAIN")) && B && tmr > 6) { newGame(); eerie(); }
      break;
    case S_LOSE:
      zandor(); tclear(); if (line_ & 1) taddP(PSTR("IMPOSSIBLE! THE MISTS HAVE BETRAYED ME.|YOU WIN... THIS TIME. I WILL REMEMBER YOUR FACE.")); else taddP(PSTR("THE GLASS HAS GONE DARK. YOU HID IT WELL.|COME BACK SOON. I AM ALWAYS WAITING."));
      if (speak(PSTR("B: AGAIN")) && B && tmr > 6) { newGame(); eerie(); }
      break;
  }
  FX::display(true);                                           // (show the screen and clear it for the next frame)
}
