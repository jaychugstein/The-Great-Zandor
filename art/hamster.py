# Nov 14 (Jordan): a hot dog weighs about 1.6 oz (45 g). A hamster is 13-18 cm long and 110-200 g.
# "Is it lighter than a hot dog?" is about WEIGHT. "Is it bigger than a hamster?" is about SIZE only, never weight
# (a small lump of metal outweighs a hamster but is not bigger). Values: 0 no, 1 rarely, 2 sometimes, 3 usually, 4 yes.
# Names are the ones shown on screen. Anything not listed keeps the rule from its size class.

def _t(s):
    out = {}
    for part in s.split(';'):
        part = part.strip()
        if part:
            n, v = part.rsplit(':', 1); out[n.strip()] = int(v)
    return out

# lighter than a hot dog (45 g)?
LIGHT = _t('''
a glass of water:0; a baby bottle:1; a bottle of glue:2; a juice box:0; a pop can:0; a sippy cup:1; a wine glass:0; a salt shaker:1;
a Rubik's cube:0; a compass:2; a corkscrew:1; a diaper:3; a doorknob:0; a tennis ball:1; a toy car:2; a tub of play dough:0;
a stress ball:2; a rubber duck:2; a slinky:1; a kitchen timer:1; a webcam:1; a medal:1; a nightlight:2; a doorbell:2; an egg:2;
a brownie:2; a croissant:2; a cupcake:2; a chocolate bar:2; a kiwi:1; a piece of ginger:2; a popsicle:2; a toque:1; a sewing kit:1;
safety goggles:1; an action figure:2; a yo-yo:2; an inhaler:2; a roll of tape:1; a bottle of nail polish:2; a pill bottle:3;
a battery:3; a glow stick:3; a hockey puck:0; a baseball:0; a pocket knife:0;
a pen:3; a pencil:4; a crayon:4; a toothbrush:3; a comb:3; chopsticks:3; a paintbrush:3; a fork:2; a spoon:2; glasses:3; sunglasses:3;
a ruler:2; a hanger:2; a stick:2; a stalk of wheat:4; a tulip:3; a rose:3; a flower:3; a pinwheel:3; a spider web:4; a nest:2;
a stalk of asparagus:3; a stalk of celery:2; a sponge:3; a loofah:3; a shower cap:3; a baseball cap:1; a balloon:4; a pine cone:2;
a seashell:2; a goldfish:4; a frog:2; a starfish:2; a mouse:3; a hamster:0; a bird:2; a bat:3; a chipmunk:1; a lizard:2; a crab:1;
a jellyfish:1; a hedgehog:0; a guinea pig:0; a rat:0; a squirrel:0; a fish:1;
socks:3; underwear:3; a tie:3; a tank top:2; a T-shirt:1; a swimsuit:2; a bra:2; gloves:2; mittens:2; a hat:2; a scarf:1;
leggings:1; shorts:1; a skirt:1; a vest:1; an apron:1; an oven mitt:1; slippers:1; a pillowcase:1; a Christmas stocking:2;
a sheet of sandpaper:4; a paper towel:4; a paper plate:3; a paper bag:3; a map:3; a menu:3; a magazine:0; a newspaper:1;
a notebook:1; a book:0; a diary:1; a dictionary:0; a comic book:2; a coloring book:1; a calendar:1; a folder:2; a puzzle:0;
a photo album:0; a roll of gift wrap:1; a roll of toilet paper:1; an egg carton:2; a lint roller:1; a puppet:1; a ball of yarn:1;
a pretzel:2; a stick of cotton candy:3; a donut:2; a power bar:2; a slice of garlic bread:2; a hot dog:2; a stick of butter:0;
a dreamcatcher:3; a fly swatter:2; a mask:2; a razor:2; a stick of deodorant:0; a peeler:2; a wooden spoon:2; a necklace:2;
a seatbelt:0; a drumstick:2; a flute:0; a game controller:0; a light bulb:2; an icicle:2; an ice pack:0; a frisbee:0; a placemat:1;
a straw:4; a napkin:4; a leaf:4; bubble wrap:3; a harmonica:1; a TV remote:1; a mug:0; a phone:0; a camera:0; a wallet:1;
a bowling pin:0; a dumbbell:0; a gold bar:0; a brick:0; a rock:0; a lock:0; a stapler:0; a scale:0; an iron:0; a drill:0;
''')

# bigger than a hamster (about a 15 cm, palm-sized lump)?
BIG = _t('''
a candy cane:2; a bandana:2; a bib:2; a diaper:2; a sheet of paper:2; a letter:2; a lanyard:2; a ribbon:2; a shoelace:2;
a piece of string:2; a tortilla:2; a strip of bacon:2; a washcloth:2; a toque:2; a party hat:2; a baby bottle:1; a wine glass:2;
a glass of water:1; a pop can:1; a juice box:1; an incense stick:2; a glow stick:1; a letter opener:1; a zip-top bag:2;
a dryer sheet:1; a postcard:1; an envelope:1; a paper airplane:2; a feather:1; a sippy cup:1; a rattle:1; a butter knife:2;
a slinky:1; a headband:1; a greeting card:1; a strip of beef jerky:1;
a pen:2; a pencil:2; a crayon:2; a toothbrush:2; a comb:1; chopsticks:2; a straw:2; a goldfish:0; a mouse:0; a hamster:2;
a bat:1; a frog:1; a chipmunk:2; a lizard:2; a crab:2; a bird:2; a starfish:2; a seashell:1; a pine cone:1;
a lime:0; a lemon:0; a plum:0; a peach:0; an apple:0; an orange:0; a tomato:0; an onion:0; a potato:1; an avocado:0; a mango:1;
a grapefruit:1; a beet:0; a bagel:1; a donut:1; a muffin:0; a pretzel:1; a taco:2; a hot dog:2; a sausage:1; a pickle:0;
a carrot:2; a banana:2; a cucumber:3; a zucchini:3; an eggplant:3; a cob of corn:3; a stalk of celery:3; a stalk of asparagus:2;
a scoop of ice cream:0; a stick of butter:0; a block of cheese:1; a block of tofu:1; a bar of soap:0; a sponge:0; a loofah:1;
a bath bomb:0; a light bulb:0; a lock:0; a magnet:0; a candle:1; glasses:1; sunglasses:1; a necklace:2; a stick of deodorant:0;
a tube of toothpaste:2; a razor:1; a computer mouse:0; a TV remote:2; a phone:2; a wallet:0; a calculator:1; a stapler:1;
a tape measure:0; a harmonica:0; a magnifying glass:1; a smoke alarm:2; a thermostat:1; an hourglass:1; a snow globe:1;
a music box:1; a jewelry box:2; a mug:1; a glass:1; a cup of coffee:1; a cup of tea:1; a cup of pudding:0; a cup of yogurt:0;
a can:1; a jar:1; a jar of honey:1; a jar of jam:1; a jar of salsa:1; a jar of mayonnaise:1; a jar of peanut butter:1;
a glass of milk:1; a glass of orange juice:1; a glass of apple juice:1; a glass of lemonade:1; a glass of soda:1; a glass of iced tea:1;
a peeler:1; a garlic press:2; a pizza cutter:1; a can opener:1; a measuring cup:1; an ice cream scoop:2; a rock:2; a nest:2;
a flower:2; a tulip:2; a bell:1; a gold bar:2; a doorstop:1; a hard drive:1; a seashell:1; a cinnamon bun:1; a hamburger:1;
an omelette:2; a pancake:2; a waffle:2; a slice of french toast:1; a pork chop:2; a power bar:0; a lint roller:2; a ball of yarn:1;
a bowl of jello:1; a cup of pudding:0; a game controller:2; a walkie-talkie:2; a camera:1; a tire pump:3; a bottle of hot sauce:1;
a bottle of soy sauce:1; a bottle of nail polish:0; a bottle of perfume:1; hand sanitizer:1; a stick:3;
a wind chime:3; a loofah:1; an ice pack:2; a pine cone:1; a whistle:0; a hockey puck:0; a baseball:0; a tennis ball:0; a golf ball:0;
''')

# bigger than a hearse? (Jordan: SIZE not weight. A hearse is about 20 ft long and 80 in wide, about 6 ft tall.)
HEARSE = _t('''
a horse:0; a cow:0; a deer:0; a moose:0; a bear:0; a polar bear:0; a panda:0; a gorilla:0; a zebra:0; a lion:0; a tiger:0;
a cheetah:0; a camel:0; a dolphin:0; a shark:1; an ostrich:0; a door:0; a refrigerator:0; a stove:0; a bathtub:0; a car:1;
a motorcycle:0; a boat:2; a helicopter:3; a ladder:1; a piano:0; a window:0; a traffic light:0; a bed:0; a couch:0; a donkey:0;
a llama:0; a canoe:0; a bookshelf:0; a dresser:0; a rug:1; a tent:1; a surfboard:0; a statue:2; a fence:2; a slide:0;
a trampoline:1; a tractor:1; a taxi:1; a police car:1; an elevator:0; a freezer:0; a shower:0; a pickup truck:2; a sailboat:2;
a forklift:0; a bush:0; an alligator:0; a crib:0; a picnic table:0; a cabinet:0; a gate:0; a boulder:1; a chalkboard:0;
a whiteboard:0; a dryer:0; a fireplace:0; an oven:0; a fountain:1; a sandbox:0; a seesaw:0; a snowmobile:0; an ATV:0;
a trailer:2; a kayak:0; a hockey net:0; a closet:0; a vending machine:0; a handrail:1; a mattress:0; a treadmill:0;
a water heater:0; a furnace:0; a workbench:0; a kiddie pool:0;
an elephant:1; a giraffe:1; a hippo:0; a rhino:0; a buffalo:0; a walrus:0; a hot tub:0; a pool table:0; a Christmas tree:1;
a van:2; a zamboni:1; an ambulance:2; a bulldozer:2; a bus stop:1; a shed:2; a staircase:2; an escalator:3; a pole:2;
a garbage truck:3; a camper:3; a pond:3; a dock:3; a wave:2; a treehouse:2; a chimney:2; a street light:2;
a tree:3; a wall:3;
''')
