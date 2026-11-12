# 230-odd more things, taking Zandor to 1000. Same tag format as data.py; grp() shares a set of tags across a group.
def grp(cat, base, items):
    key = lambda w: w.lstrip('+~-')
    out = []
    for n, s, x in items:
        over = set(key(w) for w in x.split())                  # (a thing's own tags replace the group's)
        out.append((n, cat, s, ' '.join([w for w in base.split() if key(w) not in over] + x.split())))
    return out

MORE2 = []
# ---- animals
MAM = 'mammal fur four_legs tail teeth'
MORE2 += grp('A', MAM + ' wild', [
 ('a chimpanzee', 3, 'zoo africa jungle climbs black eats_plants ~meat -tail two_legs cute noise'),
 ('an orangutan', 3, 'zoo jungle climbs orange eats_plants -tail ~two_legs'),
 ('a meerkat', 1, 'zoo africa hot_place brown meat cute two_legs underground'),
 ('an armadillo', 2, 'shell hot_place brown meat night underground -fur ~rolls round'),
 ('an anteater', 3, 'zoo jungle long meat claws brown'),
 ('a platypus', 2, 'water swims eggs brown meat $beak ~zoo $livewater'),
 ('an opossum', 2, 'night climbs white ~black meat ~eats_plants forest'),
 ('a coyote', 3, 'meat noise night brown fast dangerous bites forest ~hot_place'),
 ('a cougar', 3, 'meat fast dangerous bites climbs jumps brown claws forest'),
 ('a reindeer', 4, 'horns cold_place eats_plants holiday brown fast forest songs ~farm'),
 ('an antelope', 3, 'horns africa eats_plants fast jumps brown hot_place'),
 ('a wild boar', 3, 'forest meat eats_plants dangerous brown horns_x bites'),
 ('a weasel', 1, 'meat brown long fast forest bites'),
 ('an orca', 6, 'ocean water swims meat black white dangerous fast $livewater -fur -four_legs smooth'),
 ('a narwhal', 5, 'ocean water swims meat cold_place horns white $livewater -fur -four_legs'),
 ('an alligator_x', 4, ''),
])
MORE2 += grp('A', MAM + ' pet cute', [
 ('a gerbil', 0, 'brown eats_plants $indoors pocket'),
 ('a chinchilla', 1, 'soft eats_plants $indoors jumps night'),
])
MORE2 += grp('A', MAM + ' farm cute', [
 ('a calf', 3, 'eats_plants brown ~white ~black noise'),
 ('a piglet', 2, 'eats_plants noise smell -fur'),
 ('a foal', 3, 'eats_plants brown fast'),
])
BIRD = 'bird feathers wings two_legs eggs $beak tail'
MORE2 += grp('A', BIRD + ' wild flies', [
 ('a robin', 0, 'red brown noise songs cute tree_grow_x eats_plants ~meat'),
 ('a sparrow', 0, 'brown noise cute eats_plants'),
 ('a cardinal', 0, 'red noise cute eats_plants colorful'),
 ('a dove', 1, 'white noise cute eats_plants ~pet'),
 ('a falcon', 1, 'meat fast claws brown dangerous'),
 ('a raven', 1, 'black noise meat night_x scary'),
 ('a loon', 2, 'water swims black white noise meat $livewater'),
 ('a Canada goose', 2, 'water swims black white brown noise eats_plants bites'),
 ('a stork', 3, 'water white long meat'),
 ('a heron', 3, 'water long meat'),
 ('a puffin', 1, 'ocean water swims black white orange cute cold_place meat'),
])
MORE2 += grp('A', BIRD, [
 ('an emu', 3, 'wild zoo fast brown eats_plants -flies'),
 ('a chick', 0, 'farm yellow cute noise soft eats_plants -flies pocket'),
 ('a duckling', 0, 'farm yellow cute noise soft water swims eats_plants -flies'),
])
FISH = 'fish tail water swims scales eggs wild $livewater'
MORE2 += grp('A', FISH, [
 ('an eel', 2, 'long ocean meat dangerous_x ~eat -scales smooth'),
 ('a swordfish', 4, 'ocean meat fast sharp long eat'),
 ('a pufferfish', 1, 'ocean round dangerous thorns ~eat'),
 ('an angelfish', 0, 'pet colorful ~ocean flat $indoors'),
 ('a minnow', 0, 'pocket shiny eats_plants'),
 ('a bass', 2, 'eat meat green sport'),
 ('a cod', 2, 'ocean eat meat cold_place'),
])
MORE2 += grp('A', 'wild water', [
 ('a clam', 0, 'shell ocean eat $livewater -moves -face $hard round'),
 ('a mussel', 0, 'shell ocean eat $livewater -moves -face $hard black'),
 ('a sea urchin', 1, 'ocean thorns sharp round $livewater black -face'),
 ('a sea turtle', 3, 'reptile shell ocean swims eggs four_legs tail green $livewater eats_plants'),
 ('coral', 3, 'ocean colorful $hard $livewater -moves -face sharp'),
 ('a leech', 0, 'bites long black $livewater -face scary'),
 ('a toad', 0, 'four_legs jumps brown eggs meat night ~pet'),
 ('an alligator', 4, 'reptile scales four_legs tail teeth meat dangerous bites swims green eggs zoo hot_place'),
])
MORE2 += grp('A', 'reptile scales tail wild eggs', [
 ('a tortoise', 2, 'shell four_legs eats_plants ~pet zoo hot_place brown $hard'),
 ('a komodo dragon', 4, 'four_legs teeth meat dangerous bites zoo hot_place'),
 ('an anaconda', 4, 'long meat dangerous jungle swims water green teeth bites'),
 ('a garter snake', 1, 'long meat stripes green ~pet teeth'),
])
BUG = 'insect many_legs wild eggs'
MORE2 += grp('A', BUG, [
 ('a flea', 0, 'jumps bites black pocket pet_x'),
 ('a bedbug', 0, 'bites night bedroom brown pocket $indoors scary'),
 ('a termite', 0, 'white wood bites pocket'),
 ('a hornet', 0, 'wings flies bites dangerous stripes yellow black noise pocket'),
 ('a bumblebee', 0, 'wings flies bites stripes yellow black noise pocket flower cute soft'),
 ('a praying mantis', 0, 'wings green meat long ~flies pocket'),
 ('a maggot', 0, 'white smell -many_legs pocket soft'),
 ('a millipede', 0, 'long brown pocket'),
 ('a black widow', 0, 'black red dangerous bites scary pocket -insect'),
 ('a daddy longlegs', 0, 'long brown pocket -insect $indoors'),
])
# ---- parts of the body (20Q counts these as Animal)
MORE2 += grp('A', 'body', [
 ('a beard', 1, 'onhead soft ~brown ~black ~white washable -face'), ('a mustache', 0, 'onhead soft ~brown ~black'),
 ('a wrist', 1, 'pairs moves wear_x'), ('an ankle', 1, 'pairs moves'), ('a heel', 1, 'pairs'),
 ('a cheek', 1, 'onhead pairs soft ~red'), ('a chin', 1, 'onhead'), ('a forehead', 1, 'onhead flat'),
 ('eyelashes', 0, 'onhead pairs black long soft'), ('a lung', 1, 'insidebody pairs soft moves'),
 ('a kidney', 1, 'insidebody pairs soft'), ('a liver', 1, 'insidebody soft brown'), ('a muscle', 1, 'insidebody red moves ~$hard'),
 ('a vein', 0, 'insidebody long hasliquid'), ('a skull', 2, 'onhead insidebody white $hard round scary holiday face teeth'),
 ('a rib', 1, 'insidebody white $hard long'), ('the spine', 2, 'insidebody white $hard long'), ('a freckle', 0, 'brown round spots_x'),
])
# ---- things that come from animals
MORE2 += grp('A', 'eat kitchen $made', [
 ('ham', 1, 'cooked ~breakfast holiday sliced farm ~red smell'),
 ('a chicken wing', 0, 'cooked snack smell farm brown'),
 ('a meatball', 0, 'cooked round brown smell rolls'),
 ('a pork chop', 1, 'cooked farm brown flat'),
 ('whipped cream', 1, 'sweet white soft dessert cold farm'),
 ('sour cream', 1, 'white soft cold farm'),
 ('mayonnaise', 1, 'white soft cold ~hasliquid'),
 ('an omelette', 1, 'cooked breakfast yellow soft flat hot'),
 ('pepperoni', 0, 'red round flat sliced snack smell'),
 ('gravy', 1, 'cooked liquid brown hot holiday'),
 ('beef jerky', 0, 'snack brown long -cold smell $hard_x'),
])
MORE2 += grp('A', '', [
 ('leather', 2, 'product $made wear brown ~black smooth smell expensive -eat'),
 ('wool', 2, 'product soft white farm cloth wear ~$made'),
 ('a feather', 0, 'product feathers soft long ~white pocket ~write'),
 ('a nest', 1, 'product tree_grow_x brown round container eggs_x -alive -moves -face wild'),
 ('a beehive', 2, 'product dangerous sweet_x yellow container noise -alive -moves -face wild'),
 ('a spider web', 1, 'product white scary holiday ~$indoors -alive -moves -face fragile'),
 ('a cocoon', 0, 'product white soft tree_grow_x -moves -face ~alive'),
 ('a pearl', 0, 'product round white shiny expensive gift wear ocean pocket $hard rolls smooth -alive -moves -face'),
])
# ---- fruit, vegetables, nuts
FR = 'fruit eat sweet juicy'
MORE2 += grp('V', FR, [
 ('a mango', 1, 'seeds peel tree_grow orange yellow hot_place'), ('a nectarine', 1, 'seeds tree_grow orange red round smooth'),
 ('a tangerine', 0, 'seeds peel tree_grow orange round snack'), ('a pomegranate', 1, 'seeds peel tree_grow red round'),
 ('a blackberry', 0, 'seeds black pocket snack ~forest thorns_x'), ('a honeydew melon', 2, 'seeds green round sliced breakfast'),
 ('an olive', 0, '-sweet seeds tree_grow green ~black round pocket salad'),
])
VG = 'veg eat ~cooked kitchen'
MORE2 += grp('V', VG, [
 ('kale', 1, 'green leaves salad rabbits'), ('brussels sprouts', 0, 'green round leaves'), ('a leek', 1, 'green white long'),
 ('a turnip', 1, 'underground white round'), ('a squash', 2, 'seeds yellow ~orange ~green'), ('ginger', 0, 'underground brown smell'),
 ('beans', 0, 'brown ~green ~black pocket_x seeds'), ('rhubarb', 1, 'red long ~sweet dessert_x'),
])
MORE2 += grp('V', 'eat snack tree_grow shell brown pocket', [
 ('a pecan', 0, ''), ('a cashew', 0, '-shell white'), ('a pistachio', 0, 'green'), ('a hazelnut', 0, 'round'), ('a chestnut', 0, 'round holiday cooked'),
])
# ---- made food and drink
MORE2 += grp('V', 'eat $madefood kitchen', [
 ('noodles', 1, 'cooked long soft white ~yellow hot'), ('lasagna', 2, 'cooked hot red flat'), ('a baguette', 1, 'long brown ~$hard breakfast_x'),
 ('a croissant', 0, 'breakfast brown soft ~sweet'), ('a tortilla', 0, 'flat round white soft'), ('a cracker', 0, 'snack flat fragile pocket white ~brown'),
 ('a granola bar', 0, 'snack sweet pocket long breakfast brown'), ('nachos', 1, 'snack yellow hot fragile'), ('salsa', 1, 'red snack ~hasliquid'),
 ('mustard', 1, 'yellow ~hasliquid smell'), ('tofu', 1, 'white soft ~cooked'), ('french toast', 1, 'breakfast cooked sweet brown flat hot'),
 ('a cinnamon bun', 1, 'sweet breakfast round brown soft smell dessert'), ('apple pie', 2, 'sweet dessert round cooked holiday brown hot'),
 ('pudding', 1, 'sweet dessert soft cold brown'), ('jello', 1, 'sweet dessert soft cold colorful red'), ('a popsicle', 0, 'sweet dessert cold colorful long hot_place_x watery'),
 ('cotton candy', 1, 'sweet soft colorful snack'), ('a candy cane', 0, 'sweet holiday red white stripes long ~$hard pocket'),
 ('a chocolate bar', 0, 'sweet snack brown flat pocket gift addictive'), ('jelly beans', 0, 'sweet snack colorful pocket holiday'),
 ('a marshmallow', 0, 'sweet snack white soft pocket'), ('a gingerbread man', 0, 'sweet holiday brown flat face cooked'),
 ('poutine', 1, 'cooked hot brown snack'), ('garlic bread', 1, 'cooked hot smell brown'),
])
MORE2 += grp('V', 'drink liquid $madefood', [
 ('a smoothie', 1, 'sweet cold breakfast colorful'), ('apple juice', 1, 'sweet cold breakfast yellow'), ('iced tea', 1, 'sweet cold brown'),
 ('whiskey', 1, 'brown smell addictive expensive'), ('champagne', 1, 'yellow holiday expensive gift'), ('vinegar', 1, 'smell kitchen -drink'),
 ('olive oil', 1, 'yellow kitchen cook -drink'), ('soy sauce', 1, 'black kitchen -drink'), ('hot sauce', 1, 'red kitchen hot -drink'),
])
MORE2 += grp('V', 'eat kitchen smell', [
 ('pepper', 0, 'black cook'), ('cinnamon', 0, 'brown sweet cook tree_grow'), ('mint', 0, 'plant green leaves sweet'), ('basil', 0, 'plant green leaves cook'),
])
# ---- plants
MORE2 += grp('V', 'plant alive green leaves', [
 ('a fern', 2, 'forest ~$indoors'), ('a vine', 3, 'long climbs_x'), ('a lily', 1, 'flower white smell gift'), ('an orchid', 1, 'flower colorful gift expensive $indoors'),
 ('a daffodil', 1, 'flower yellow'), ('lavender', 1, 'flower smell -green'), ('a poppy', 1, 'flower red holiday'), ('clover', 0, 'rabbits pocket'),
 ('a weed', 1, '~flower'), ('a maple tree', 6, 'tree_grow_x wood red orange sweet_x'), ('an oak tree', 6, 'wood old'), ('a birch tree', 6, 'wood white'),
 ('a willow tree', 6, 'wood water long'), ('a venus flytrap', 1, 'meat bites scary $indoors'), ('wheat', 2, 'farm yellow eat long -green'),
 ('a lily pad', 1, 'water flat round $livewater'), ('poison ivy', 2, 'dangerous forest'), ('mistletoe', 1, 'holiday'), ('holly', 1, 'holiday red sharp thorns'),
])
MORE2 += grp('V', '', [
 ('a branch', 3, 'wood long brown tree_grow_x larger'), ('bark', 1, 'wood brown ~$hard larger'), ('a seed', 0, 'seeds pocket brown ~eat'),
 ('a tree stump', 3, 'wood brown round forest ~furniture_x'), ('a root', 2, 'underground long brown'), ('a tumbleweed', 3, 'round rolls brown hot_place'),
])
# ---- things made from wood, paper and cloth
MORE2 += grp('V', '$made wood', [
 ('a toothpick', 0, 'sharp long pocket eatwith_x kitchen'), ('a match', 0, 'hot long pocket dangerous light'), ('a popsicle stick', 0, 'flat long pocket'),
 ('a clothespin', 0, 'pocket ~plastic clean_x'), ('a barrel', 3, 'container round hasliquid rolls brown old'), ('a cork', 0, 'round pocket brown soft'),
 ('a stool', 3, 'furniture four_legs_x kitchen round'), ('a rocking chair', 3, 'furniture moves_x comfort old'), ('a crib', 4, 'furniture bedroom container'),
 ('a nightstand', 3, 'furniture bedroom opens container'), ('a coffee table', 3, 'furniture flat'), ('a picnic table', 4, 'furniture $outdoors flat'),
 ('a cabinet', 4, 'furniture kitchen opens container'), ('a shelf', 3, 'furniture flat long'), ('a gate', 4, 'opens $outdoors ~metal'),
 ('a treehouse', 5, 'building_x place_x $outdoors toy'), ('a birdhouse', 2, 'container $outdoors'), ('a doghouse', 3, 'container $outdoors pet_x'),
 ('a toboggan', 3, 'vehicle cold_place sport $outdoors long flat toy'), ('a paddle', 3, 'long flat water sport'), ('a drumstick', 1, 'long music pairs'),
 ('a ukulele', 2, 'music played ~toy'), ('a cello', 3, 'music played expensive'), ('a banjo', 2, 'music played round'), ('a clarinet', 2, 'music played long black'),
 ('a xylophone', 2, 'music played ~metal colorful toy'),
])
MORE2 += grp('V', '$made paper flat', [
 ('a tissue', 0, 'white soft pocket clean bathroom fragile'), ('a paper bag', 1, 'container brown opens kitchen'), ('a paper plate', 1, 'round white eatwith kitchen'),
 ('a paper airplane', 0, 'toy flies white -flat'), ('a greeting card', 0, 'gift holiday read opens writing colorful envelope'),
 ('a ticket', 0, 'pocket writing read travel envelope payuse'), ('a receipt', 0, 'pocket writing read white long envelope'),
 ('a poster', 2, 'colorful bedroom writing ~read'), ('a postcard', 0, 'gift travel writing read envelope colorful'),
 ('a letter', 0, 'writing read write envelope white'), ('a diary', 1, 'write read writing opens bedroom info'),
 ('a dictionary', 1, 'read writing opens info heavy_x office'), ('a comic book', 1, 'read writing opens colorful enjoy'),
 ('a menu', 1, 'read writing opens foodthere_x'), ('wrapping paper', 1, 'gift holiday colorful -flat'), ('confetti', 0, 'colorful holiday pocket'),
 ('a tea bag', 0, 'drink_x kitchen pocket smell -flat'), ('a cigarette', 0, 'long white smell addictive dangerous pocket hot -flat'),
])
MORE2 += grp('V', '$made cloth soft washable', [
 ('a pillowcase', 1, 'bedroom white container'), ('a bed sheet', 2, 'bedroom white flat'), ('a quilt', 2, 'bedroom colorful comfort gift'),
 ('a tablecloth', 2, 'kitchen flat'), ('a washcloth', 0, 'bathroom clean wet flat'), ('an apron', 1, 'wear kitchen cook'),
 ('a bib', 0, 'wear kitchen'), ('a diaper', 0, 'wear smell white'), ('a bandana', 0, 'wear onhead_x colorful flat pocket'),
 ('a vest', 1, 'wear clothes buttons ~office ~cold_place'), ('a suit', 2, 'wear clothes expensive office black'), ('a robe', 2, 'wear clothes bathroom comfort'),
 ('leggings', 1, 'wear clothes black long pairs_x'), ('a tank top', 1, 'wear clothes ~sport ~colorful everyday'), ('overalls', 2, 'wear clothes farm_x'),
 ('a cape', 2, 'wear pretend_x red holiday'), ('a costume', 2, 'wear holiday colorful pretend_x scary'), ('a toque', 0, 'wear onhead cold_place clothes'),
 ('a headband', 0, 'wear onhead sport'), ('a shoelace', 0, 'long pairs pocket'), ('a sleeping bag', 2, 'bedroom_x $outdoors comfort container travel'),
 ('a hammock', 3, '$outdoors comfort furniture_x'), ('a rope', 2, 'long -soft tool ~sport'), ('string', 0, 'long white pocket'),
 ('yarn', 1, 'long colorful round'), ('thread', 0, 'long pocket'), ('a parachute', 3, 'flies_x sky travel_x colorful -washable'),
])
# ---- rocks, metals and other natural minerals
MORE2 += grp('M', '', [
 ('a brick', 1, 'red $heavy long building_x'), ('concrete', 3, '$heavy $outdoors flat'), ('a pebble', 0, 'round pocket smooth water rolls'),
 ('a boulder', 4, '$heavy round $outdoors old'), ('a crystal', 0, 'shiny pocket sharp colorful glass_x gift'), ('a ruby', 0, 'red shiny expensive gift wear pocket'),
 ('an emerald', 0, 'green shiny expensive gift wear pocket'), ('silver', 0, 'metal shiny expensive wear pocket white_x'), ('copper', 0, 'metal shiny orange brown'),
 ('iron', 1, 'metal $heavy black'), ('steel', 1, 'metal $heavy shiny'), ('a fossil', 1, 'old $outdoors underground'), ('coal', 1, 'black underground hot holiday_x'),
 ('oil', 1, 'liquid black underground smell expensive'), ('gasoline', 1, 'liquid smell dangerous garage expensive'), ('clay', 1, 'soft brown wet paint'),
 ('chalk', 0, 'white write long pocket fragile'),
])
# ---- school and office
MORE2 += grp('M', 'office desk', [
 ('a chalkboard', 4, 'black flat write writing -desk'), ('a whiteboard', 4, 'white flat write writing -desk'), ('a marker', 0, 'write long colorful pocket plastic smell'),
 ('a highlighter', 0, 'write long yellow pocket plastic'), ('an eraser', 0, 'soft pocket ~write'), ('a pencil sharpener', 0, 'sharp pocket tool'),
 ('a binder', 1, 'plastic opens container paper_x'), ('a folder', 1, 'flat opens container paper'), ('a clipboard', 1, 'flat write_x'),
 ('a telephone', 1, 'electric talk noise rings buttons plastic old'), ('a monitor', 2, 'electric screen flat withpc plugin'),
 ('a $hard drive', 1, 'electric info withpc metal'), ('a router', 1, 'electric internet withpc light plugin'), ('a globe', 2, 'round map_x colorful info rolls_x'),
])
# ---- electronics and gadgets
MORE2 += grp('M', 'electric', [
 ('a game controller', 1, 'battery buttons toy played plastic withpc_x enjoy'), ('a drone', 2, 'battery flies toy noise expensive camera_x'),
 ('a record player', 2, 'music noise old round_x plugin'), ('earbuds', 0, 'battery music noise pairs pocket wear plastic everyday'),
 ('a projector', 2, 'light screen_x plugin'), ('a walkie-talkie', 1, 'battery talk noise pairs buttons'), ('a GPS', 1, 'battery screen travel info'),
 ('a metal detector', 3, 'battery noise long tool $outdoors'), ('a jukebox', 4, 'music noise light colorful old payuse plugin'),
 ('a pinball machine', 4, 'toy played noise light colorful payuse plugin enjoy'), ('a slot machine', 4, 'played noise light payuse addictive plugin'),
 ('a disco ball', 2, 'round shiny light glass -electric'),
])
MORE2 += grp('M', '', [
 ('a CD', 0, 'round flat shiny music info plastic'), ('a telescope', 3, 'long glass sky space expensive'), ('a microscope', 2, 'glass office_x expensive tool'),
 ('binoculars', 1, 'glass pairs_x $outdoors travel'), ('a magnifying glass', 1, 'glass round handle tool'), ('a compass', 0, 'round travel pocket $outdoors info metal'),
 ('a thermometer', 0, 'long glass ~electric hospital info'), ('a stethoscope', 1, 'hospital wear long metal tool'), ('a syringe', 0, 'hospital sharp long plastic dangerous_x scary'),
 ('a pill', 0, 'eat_x hospital pocket round white bathroom'), ('a crutch', 3, 'hospital long pairs metal'), ('a wheelchair', 3, 'hospital wheels vehicle metal'),
 ('braces', 0, 'metal wear teeth_x hospital_x expensive'), ('contact lenses', 0, 'wear pairs round pocket plastic everyday'),
])
# ---- around the house
MORE2 += grp('M', 'bathroom', [
 ('a faucet', 1, 'metal water wet shiny kitchen everyday'), ('a shower curtain', 3, 'plastic wet flat'), ('a Q-tip', 0, 'long white soft pocket clean'),
 ('tweezers', 0, 'metal sharp pocket tool long shiny'), ('nail clippers', 0, 'metal sharp pocket tool noise handle ~everyday'), ('a hair tie', 0, 'round wear pocket onhead_x'),
 ('a curling iron', 1, 'electric hot long plugin'), ('deodorant', 1, 'smell everyday plastic'), ('sunscreen', 1, 'liquid white hot_place_x smell $outdoors'),
 ('lipstick', 0, 'red wear pocket'), ('mouthwash', 1, 'liquid clean smell hasliquid'), ('a hot tub', 5, 'water hot wet $outdoors comfort electric -bathroom'),
])
MORE2 += grp('M', '', [
 ('a laundry basket', 2, 'container plastic bedroom'), ('an iron', 1, 'electric hot heavy_x metal clean_x plugin'), ('a dryer', 4, 'electric appliance hot noise clean opens plugin'),
 ('a dustpan', 1, 'clean plastic flat handle'), ('a fire extinguisher', 2, 'red metal $heavy kitchen dangerous_x'), ('an extension cord', 1, 'electric long plugin orange'),
 ('a chandelier', 3, 'light glass electric expensive fragile shiny'), ('a lantern', 1, 'light handle $outdoors ~battery glass'), ('a fireplace', 4, 'hot light comfort holiday'),
 ('a chimney', 5, 'smoke_x long holiday $outdoors'), ('a doorknob', 0, 'round metal shiny opens handle everyday'), ('a doormat', 2, 'flat $outdoors ~cloth'),
 ('a staircase', 5, 'wood_x long'), ('an escalator', 5, 'electric moves public'), ('a shed', 5, 'building garage_x $outdoors container'),
 ('a wine glass', 0, 'glass eatwith fragile kitchen hasliquid'), ('a pitcher', 1, 'container hasliquid kitchen handle ~glass'), ('a corkscrew', 0, 'metal sharp tool kitchen'),
 ('a bottle opener', 0, 'metal tool kitchen pocket'), ('a bottle cap', 0, 'round metal pocket flat'), ('a pop can', 0, 'metal container hasliquid round'),
 ('a salt shaker', 0, 'kitchen container ~glass eatwith pairs'), ('a pizza cutter', 1, 'kitchen sharp round metal handle tool rolls'),
 ('an ice cream scoop', 1, 'kitchen metal handle round tool'), ('a funnel', 1, 'kitchen plastic tool hasliquid'), ('a baking sheet', 1, 'kitchen metal flat cook hot'),
 ('a wok', 2, 'kitchen metal cook round hot handle'), ('a toaster oven', 2, 'kitchen electric appliance cook hot plugin opens'),
 ('an ice cube tray', 1, 'kitchen plastic cold container flat'), ('a coaster', 0, 'flat round kitchen_x'), ('an oven', 4, 'kitchen electric appliance cook hot opens'),
 ('a water bottle', 1, 'container hasliquid plastic everyday sport travel'), ('a baby bottle', 0, 'container hasliquid plastic'), ('a pacifier', 0, 'plastic pocket comfort'),
 ('a high chair', 3, 'furniture kitchen four_legs_x plastic'),
])
# ---- outdoors, the street, the playground
MORE2 += grp('M', '$outdoors', [
 ('a sidewalk', 6, 'flat long public'), ('a road', 6, 'flat long black public travel'), ('a stop sign', 3, 'red metal writing public flat'),
 ('a street light', 5, 'light electric long metal night public'), ('a fire hydrant', 3, 'red metal water $heavy public'), ('a parking meter', 3, 'metal payuse public long'),
 ('a billboard', 5, 'writing flat public colorful'), ('a fountain', 4, 'water wet public ~drink'), ('a sprinkler', 1, 'water wet'), ('a sandbox', 4, 'toy container'),
 ('a seesaw', 4, 'toy long played'), ('a ferris wheel', 6, 'round vehicle payuse light enjoy electric'), ('a roller coaster', 6, 'vehicle fast payuse scary enjoy noise'),
 ('a barbecue', 3, 'cook hot metal smell'), ('a cooler', 2, 'container cold plastic travel opens handle'), ('a lawn chair', 3, 'furniture'),
 ('a campfire', 3, 'hot light smell cook dangerous -$made'), ('a net', 2, 'sport ~cloth'), ('a fishing hook', 0, 'metal sharp pocket water'),
 ('a horseshoe', 1, 'metal farm heavy_x'), ('a saddle', 2, 'farm vehicle_x'), ('a leash', 1, 'long pet_x handle'), ('a mousetrap', 0, 'dangerous wood_x $indoors'),
 ('a birdcage', 2, 'metal container pet_x $indoors'), ('a fish tank', 2, 'glass container water hasliquid pet_x $indoors'),
])
# ---- things that go
VEH = 'vehicle wheels engine metal travel'
MORE2 += grp('M', VEH, [
 ('a go-kart', 3, 'fast toy_x enjoy payuse'), ('a snowmobile', 4, 'cold_place fast noise -wheels'), ('an ATV', 4, 'fast noise $outdoors'),
 ('a van', 5, ''), ('a convertible', 4, 'fast expensive opens'), ('a sports car', 4, 'fast expensive red'), ('a tank', 5, 'weapon dangerous $heavy green -travel'),
 ('a jet', 6, 'flies fast noise sky wings -wheels'), ('a zamboni', 5, 'cold_place sport clean -travel'), ('a snowplow', 5, 'cold_place clean -travel'),
 ('a garbage truck', 5, 'smell clean noise -travel'), ('a tow truck', 5, ''), ('a dump truck', 5, '$heavy'), ('an excavator', 5, 'tool $heavy yellow -travel'),
 ('a subway', 6, 'underground public payuse electric'), ('a streetcar', 6, 'public payuse electric'), ('a ferry', 6, 'water public payuse -wheels'),
 ('a speedboat', 4, 'water fast -wheels'), ('a camper', 5, 'bedroom_x container'), ('a trailer', 4, '-engine container'),
])
MORE2 += grp('M', 'vehicle', [
 ('a unicycle', 3, 'wheels metal sport'), ('a tricycle', 2, 'wheels metal toy'), ('a stroller', 3, 'wheels travel'), ('a wagon', 3, 'wheels toy red container'),
 ('a shopping cart', 3, 'wheels metal container public'), ('a kayak', 4, 'water sport plastic long'), ('a rowboat', 4, 'water wood'), ('a yacht', 6, 'water expensive engine'),
 ('a blimp', 6, 'flies sky slow_x'), ('a snowboard', 3, 'cold_place sport flat long'), ('ice skates', 1, 'cold_place sport pairs sharp wear feet metal'),
])
MORE2 += grp('M', 'metal', [
 ('an anchor', 3, '$heavy water ocean'), ('a steering wheel', 2, 'round handle_x garage_x'), ('a seatbelt', 1, 'long ~cloth wear_x'), ('a license plate', 1, 'flat writing'),
 ('an engine', 3, 'engine $heavy noise hot garage'), ('a siren', 1, 'noise electric light red'),
])
# ---- music, sport, toys, parties
MORE2 += grp('M', 'music played noise', [
 ('a cymbal', 2, 'metal round flat shiny'), ('a tambourine', 1, 'round metal ~toy'), ('maracas', 1, 'pairs ~toy ~wood'), ('a saxophone', 2, 'metal shiny expensive'),
 ('a trombone', 3, 'metal shiny long'), ('a tuba', 3, 'metal shiny $heavy'), ('an accordion', 2, 'buttons opens_x'), ('bagpipes', 2, 'cloth_x'),
 ('a harp', 4, 'wood expensive long'), ('an electric guitar', 3, 'electric wood long'), ('a gong', 3, 'metal round flat'), ('a kazoo', 0, 'toy pocket plastic'),
])
MORE2 += grp('M', 'sport', [
 ('a hockey puck', 0, 'black round flat cold_place pocket $hard'), ('a hockey net', 4, 'cold_place red container_x'), ('a dart', 0, 'sharp long pocket toy'),
 ('a dartboard', 2, 'round flat toy'), ('a bowling pin', 1, 'white ~wood'), ('a pool table', 5, 'furniture green flat played four_legs_x'), ('a ski pole', 3, 'long pairs cold_place'),
 ('a hula hoop', 3, 'round toy plastic colorful rolls'), ('a pogo stick', 3, 'toy long jumps_x'), ('a punching bag', 3, '$heavy soft_x'),
 ('a life jacket', 2, 'wear water orange'), ('a golf ball', 0, 'ball round white pocket $hard rolls'),
])
MORE2 += grp('M', 'toy enjoy', [
 ('a slinky', 0, 'metal round'), ("a Rubik's cube", 0, 'plastic colorful puzzle_x'), ('a spinning top', 0, 'round'), ('a water gun', 1, 'plastic water wet weapon_x colorful'),
 ('a toy train', 1, 'wheels plastic'), ('a dollhouse', 3, 'container opens'), ('an action figure', 0, 'plastic face pocket'), ('a puppet', 1, 'cloth face soft'),
 ('a board game', 2, 'played box set paper_x'), ('a chess set', 2, 'played set black white box'), ('dominoes', 0, 'played set black white spots flat pocket'),
 ('a pinwheel', 1, 'colorful plastic'), ('a piñata_x', 2, ''),
])
MORE2 += grp('M', 'holiday', [
 ('fireworks', 2, 'light noise colorful sky dangerous hot night'), ('a sparkler', 0, 'light hot long'), ('a party hat', 0, 'wear onhead colorful paper'),
 ('a present', 2, 'gift box container colorful opens enjoy'), ('a ribbon', 0, 'long colorful cloth gift'), ('an ornament', 0, 'round shiny colorful fragile glass'),
 ('Christmas lights', 1, 'light electric colorful long plugin'), ('a stocking', 1, 'cloth container red wear_x'), ('an Easter egg', 0, 'round colorful ~eat'),
 ('a mask', 1, 'wear onhead face scary'), ('a magic wand', 1, 'long pretend toy'), ('a coffin', 4, 'wood container scary opens'), ('a tombstone', 3, '$heavy writing scary $outdoors old'),
])
# ---- people, creatures, places, weather and ideas
PEO = 'person alive face teeth moves talk two_legs'
MORE2 += grp('O', PEO + ' job', [
 ('a lawyer', 3, 'office read write expensive_x'), ('a judge', 3, 'office uniform'), ('a magician', 3, 'enjoy pretend_x'), ('a singer', 3, 'music noise enjoy songs'),
 ('an actor', 3, 'enjoy'), ('a hockey player', 3, 'sport uniform cold_place fast'), ('a referee', 3, 'sport uniform stripes noise'), ('a coach', 3, 'sport'),
 ('a waiter', 3, 'foodthere uniform'), ('a cashier', 3, 'uniform'), ('a plumber', 3, 'tool water tasks'), ('a mechanic', 3, 'tool garage tasks'),
 ('a carpenter', 3, 'tool wood_x tasks'), ('a janitor', 3, 'clean uniform tasks'), ('a librarian', 3, 'read'), ('a scientist', 3, 'office uniform_x'),
 ('an artist', 3, 'paint'), ('a bus driver', 3, 'vehicle_x uniform travel'), ('a lifeguard', 3, 'water swims uniform red'), ('a babysitter', 3, ''),
 ('a president', 3, 'office royal_x'), ('a cowboy', 3, 'farm hot_place old'), ('a ninja', 3, 'weapon black fast dangerous ~pretend'), ('a knight', 3, 'weapon metal old royal_x uniform'),
])
MORE2 += grp('O', PEO, [
 ('a dad', 3, 'comfort everyday'), ('a grandma', 3, 'comfort old'), ('a grandpa', 3, 'comfort old'), ('a brother', 3, ''), ('a sister', 3, ''),
 ('a child', 2, 'cute toy_x'), ('a neighbor', 3, ''), ('a stranger', 3, 'scary'), ('a princess', 3, 'royal ~pretend'), ('a prince', 3, 'royal ~pretend'),
 ('a thief', 3, 'dangerous night'), ('a superhero', 3, 'pretend flies fast uniform'), ('a bride', 3, 'white holiday_x'),
])
MORE2 += grp('O', 'pretend alive face moves', [
 ('a giant', 5, 'person_x scary two_legs dangerous'), ('a troll', 3, 'scary two_legs'), ('an elf', 2, 'holiday two_legs cute green'), ('a leprechaun', 2, 'holiday two_legs green'),
 ('a goblin', 2, 'scary two_legs green'), ('an angel', 3, 'wings flies white sky two_legs holiday'), ('the devil', 3, 'scary red horns tail hot dangerous two_legs'),
 ('a gnome', 1, 'two_legs $outdoors red'), ('a cyclops', 5, 'scary two_legs dangerous'), ('a phoenix', 3, 'bird wings flies hot red feathers'),
 ('a centaur', 4, 'four_legs tail'), ('the Loch Ness Monster', 6, 'water swims scary long'),
])
MORE2 += grp('O', 'weather', [
 ('a snowflake', 0, 'cold white sky watery fragile cold_place'), ('hail', 0, 'cold white sky watery round $hard dangerous_x'), ('an icicle', 1, 'cold watery sharp long -sky cold_place'),
 ('a hurricane', 6, 'sky dangerous wet noise scary'), ('a flood', 6, 'water watery wet dangerous -sky'), ('an earthquake', 6, 'dangerous scary noise -sky'),
 ('a sunset', 6, 'sky orange red colorful enjoy'), ('the northern lights', 6, 'sky night colorful green cold_place light'),
])
MORE2 += grp('O', 'place', [
 ('a glacier', 6, 'cold watery white cold_place old'), ('an iceberg', 6, 'cold watery white cold_place ocean water'), ('the sky', 6, 'sky -place'),
 ('outer space', 6, 'sky space cold black -place'), ('a black hole', 6, 'sky space black scary dangerous -place'), ('a galaxy', 6, 'sky space -place'),
 ('Mars', 6, 'sky space red round -place'), ('a canyon', 6, 'hot_place old'), ('a cliff', 6, 'dangerous'), ('a hill', 6, 'green'), ('a swamp', 6, 'water wet smell green'),
 ('a pond', 5, 'water watery wet'), ('a jungle', 6, 'jungle hot_place green forest_x'), ('a field', 6, 'green flat farm'), ('a garden', 5, 'green ~flower $made ~eat_x ~smell tasks ~farm'),
 ('a backyard', 5, 'green $made enjoy ~toy_x everyday comfort'), ('a cemetery', 6, 'scary $made old'), ('the North Pole', 6, 'cold cold_place white holiday'),
])
MORE2 += grp('O', 'place building', [
 ('a museum', 6, 'old payuse public'), ('a bank', 5, 'office public'), ('a store', 5, 'public'), ('a grocery store', 5, 'foodthere public'),
 ('a gas station', 5, 'public smell_x'), ('a bakery', 5, 'foodthere smell public'), ('a hotel', 6, 'payuse public travel bedroom_x'), ('a jail', 6, 'scary'),
 ('a fire station', 5, 'red'), ('a stadium', 6, 'sport noise payuse public'), ('a hockey rink', 6, 'sport cold payuse public'), ('a gym', 5, 'sport payuse public'),
 ('a bowling alley', 5, 'sport payuse public noise'), ('a casino', 6, 'payuse public addictive light noise'), ('a circus', 6, 'payuse enjoy colorful'),
 ('an amusement park', 6, 'payuse enjoy noise -building'), ('a factory', 6, 'noise tasks'), ('a garage', 5, 'garage_x container'), ('a basement', 5, 'underground cold'),
 ('an attic', 5, 'old'), ('a kitchen', 5, 'kitchen_x foodthere_x cook_x'), ('a bathroom', 4, 'bathroom_x water wet'), ('a bedroom', 5, 'bedroom_x comfort'),
 ('a closet', 4, 'bedroom container opens'), ('an apartment', 5, ''), ('an igloo', 5, 'cold cold_place white watery round'), ('a pyramid', 6, 'old hot_place africa'),
 ('a windmill', 6, 'moves farm'), ('a tunnel', 6, 'underground long -building'), ('a train station', 6, 'public travel'),
])
MORE2 += grp('O', 'abstract', [
 ('a wedding', 'x', 'holiday enjoy'), ('a parade', 'x', 'holiday enjoy noise colorful public'), ('a concert', 'x', 'music noise enjoy payuse'),
 ('a movie', 'x', 'enjoy screen_x payuse $made'), ('a cartoon', 'x', 'enjoy pretend colorful $made'), ('a video game', 'x', 'enjoy played addictive toy $made electric'),
 ('a joke', 'x', 'enjoy'), ('a story', 'x', 'enjoy read pretend'), ('a lie', 'x', '~dangerous ~scary'), ('an idea', 'x', ''), ('a memory', 'x', 'old'), ('happiness', 'x', 'enjoy comfort'),
 ('sadness', 'x', '~wet ~songs'), ('anger', 'x', '~dangerous ~hot red noise'), ('fear', 'x', 'scary'), ('pain', 'x', 'scary_x'), ('a hug', 'x', 'comfort enjoy gift_x'), ('a kiss', 'x', 'enjoy'),
 ('a sneeze', 'x', 'noise'), ('a yawn', 'x', 'noise'), ('a hiccup', 'x', 'noise'), ('a smile', 'x', 'enjoy face_x'), ('an echo', 'x', 'noise'), ('a fart', 'x', 'noise smell'),
 ('luck', 'x', ''), ('magic', 'x', 'pretend enjoy'), ('a birthday', 'x', 'holiday enjoy gift'), ('summer', 'x', 'hot hot_place_x enjoy'), ('winter', 'x', 'cold cold_place_x holiday'),
 ('night', 'x', 'night black sky_x'), ('hockey', 'x', 'sport cold_place enjoy played'), ('a war', 'x', 'dangerous scary weapon_x'), ('a name', 'x', 'writing everyday ~read ~gift old'),
 ('gravity', 'x', ''), ('electricity', 'x', 'electric dangerous payuse'), ('a hole', 'x', 'round underground_x'), ('air', 'x', 'sky_x everyday'),
])
MORE2 += grp('O', '', [
 ('steam', 3, 'hot watery wet weather_x white'), ('dust', 0, '$indoors_x'), ('dirt', 1, 'brown $outdoors underground'), ('a germ', 0, 'alive dangerous_x pocket_x'),
 ('a photo', 0, 'flat colorful gift paper $made envelope'), ('a painting', 2, 'flat colorful paint expensive gift $made old'), ('a tear', 0, 'watery wet liquid body_x'),
])
MORE2 += [
 ('a boomerang', 'V', 1, '$made wood toy sport flat $outdoors flies_x'), ('a volleyball', 'M', 2, 'ball round sport white soft_x water_x'),
 ('caramel', 'V', 0, 'eat sweet snack brown soft $madefood dessert'), ('a rattle', 'M', 0, 'toy noise plastic colorful handle'),
 ('lip balm', 'M', 0, 'pocket bathroom_x smell everyday plastic'), ('trail mix', 'V', 1, 'eat snack $madefood ~sweet brown travel'),
 ('a recorder', 'M', 1, 'music played noise long plastic toy'), ('a sunflower seed', 'V', 0, 'eat snack seeds pocket black shell'),
 ('a boss', 'O', 3, 'person alive face teeth moves talk two_legs job office'), ('a car seat', 'M', 2, 'vehicle_x plastic cloth travel container'),
 ('a sippy cup', 'M', 0, 'plastic container hasliquid eatwith colorful handle'), ('a poker chip', 'M', 0, 'round flat plastic pocket played set colorful'),
 ('a lottery ticket', 'V', 0, '$made paper flat pocket writing read payuse addictive envelope'), ('a jackhammer', 'M', 3, 'tool electric_x noise $heavy metal $outdoors tasks'),
 ('a butter knife', 'M', 0, 'metal kitchen eatwith long shiny -sharp'), ('a coat rack', 'V', 3, '$made wood furniture long'),
 ('a massage', 'O', 'x', 'abstract comfort enjoy payuse'),
]
MORE2 = [m for m in MORE2 if not m[0].endswith('_x')]
