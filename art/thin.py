# Nov 14: the things with the fewest answers filled in, checked one by one for obvious answers they were missing.
# Names as shown on screen. 0 no, 1 rarely, 2 sometimes, 3 usually, 4 yes. Survey answers still win over these.
RAW = '''
a shadow: moves:2 $touch:1 selfsee:3 $hold:0 $pickup:0 light:0 flat:4 night:1
smoke: smell:4 hot:2 seethrough:2 white:2 moves:3 dangerous:3 camping:3 sky:3 flies:3
a clothesline: strings:2 plastic:3 wall:2 clean:2 cloth:1 wet:3 long:4
a puddle: liquid:4 weather:3 brown:2 drink:0 swimin:0 water:4 fallsky:1
dirt: soft:2 smell:2 hardware:2 rabbits:0 underground:0 brown:4 grows:0 farm:3
a shoe rack: metal:2 wood:2 plastic:2 bedroom:2 floor:4 container:3 feet:1
a swing: vehicle:3 metal:2 wood:2 plastic:2 strings:2 school:3 moves:1 toy:3 parts:3
a doorstop: plastic:2 wood:2 floor:4 wall:1
a park: leaves:3 flower:3 grows:3 payuse:0 foodthere:1 sport:2 wild:1 green:4 place:4
an ashtray: glass:2 hot:1 smell:4 $indoors:2 $outdoors:2 container:4
a boulder: brown:2 rock:4 round:2 wild:2
a bus stop: glass:2 payuse:1 everyday:1 travel:3 writing:3
a fountain: money:2 drink:2 rock:2 swimin:0 decor:3 liquid:2 noise:3
a gnome: colorful:3 plastic:2 cute:2 toy:1 decor:4 face:4 moves:0
a hill: leaves:2 flower:2 grows:1 climbs:0 green:3 winter:3 place:4
a napkin holder: metal:2 plastic:2 wood:2 eatwith:1 kitchen:4 container:3
a sandbox: toy:3 school:2 baby:2 beach:0 wet:2 lid:2 yellow:2 brown:2
a scratching post: toy:3 cloth:3 floor:4
a seed: eat:2 tree_grow:2 rabbits:1 grocery:2 round:2 grows:4 plant:3
a treehouse: leaves:2 sky:3 place:3 building:2 livein:1 toy:3 wood:4
fog: seethrough:2 moves:2 sky:1 dangerous:2 smell:0 white:4 weather:4
sand: rock:2 brown:2 pocket:2 $hard:2 beach:4 hot_place:3 yellow:3
a bird feeder: plastic:3 metal:2 wall:1 decor:1 hang:1
a birdhouse: hang:2 decor:2 wood:3 hole:4
a bowl of oatmeal: fingers:0 sweet:2 brown:2 white:2 liquid:1 dairy:2 breakfast:4 cooked:4
a chess set: flat:2 school:2 gift:3 toy:2 game:4 played:4 set:4
a church: rings:3 noise:2 sky:2 wood:2 rock:2 music:2 shop:0 livein:0 building:4 holiday:3
a dog bed: comfort:3 bedroom:2 soft:4 floor:4
a fire hydrant: yellow:2 hasliquid:3 opens:2 wall:0 red:3 metal:4
a magnet: toy:2 decor:2 school:2 flat:2 sticky:2 metal:4
a nest: feathers:2 wood:2 forest:3 burn:4 sky:2 tree_grow:1
a parking lot: everyday:2 writing:2 white:2 shop:0 place:4 payuse:2
a pinata: container:4 sweet:2 gift:1 wall:2 scary:0 holiday:2 hit:4 colorful:4
a pole: sky:3 cord:2 long:4
a pond: swimin:2 liquid:3 green:2 cold:2 winter:2 wild:2 water:4
a rock: round:2 forest:2 smooth:2 water:2 rock:4 $hard:4
a rocking chair: parts:3 moves:1 comfort:2 $outdoors:2 baby:2 furniture:4
a seashell: decor:2 round:2 colorful:2 fragile:2 smooth:2 gift:1 noise:1 beach:4
a spinning top: moves:2 wood:2 plastic:2 metal:2 game:2 toy:4 round:3
a star: yellow:2 holiday:2 everyday:0 flies:0 dangerous:0 shiny:4 sky:4 night:4
a statue: rock:3 metal:2 two_legs:2 expensive:3 moves:0 decor:4
a tree stump: leaves:0 tree_grow:0 grows:1 wild:2 alive:1 wood:4 forest:3
a trophy: yellow:3 gift:1 school:2 plastic:2 writing:3 shiny:4 sport:4
a wave: sport:2 swimin:3 white:2 loud:2 dangerous:2 water:4 ocean:3
an hourglass: wood:2 game:2 moves:2 glass:4
lightning: white:3 yellow:2 flat:0 fallsky:4 sky:4 weather:4 dangerous:4
the sky: flies:0 everyday:2 weather:3 sky:4 place:2
a backyard: leaves:3 flower:2 grows:3 green:4
a baseball bat: metal:2 weapon:1 dangerous:2 throw:0 hit:4 sport:4 team:4
a basket: cloth:1 plastic:2 holiday:2 gift:2 container:4 handle:3
a beehive: sweet:2 insect:2 wood:2 tree_grow:1 bites:3 dangerous:3 noise:4
a bench: school:2 everyday:1 furniture:3 $outdoors:3
a birdcage: hang:2 bedroom:1 pet:1 container:4 metal:4
a bowl of mac & cheese: dairy:4 salty:3 soft:3 fingers:0 cooked:4 eat:4
a briefcase: money:2 cloth:1 traveller:2 office2:4 handle:4 opens:4
a chimney: smell:2 rock:2 hot:2 black:2 red:2 holiday:3 winter:3
a closet: handle:3 scary:2 opens:4 bedroom:4 container:4
a clothespin: clean:2 metal:2 plastic:2 pairs:0 sharp:0 parts:3
a cookie jar: sweet:2 cute:2 decor:2 plastic:2 kitchen:4 lid:4 container:4
a crowbar: weapon:1 red:2 black:2 dangerous:2 opens:2 metal:4 tool:4
a cup of tea: hot:2 cooked:2 green:2 hasliquid:3 eatwith:0 container:2 sweet:1 winter:3 comfort:3
a cutting board: sharp:0 eatwith:1 cook:4 kitchen:4
a doghouse: pet:0 livein:0 building:2 red:2 wood:4
a door chain: opens:2 parts:2 wall:4
a dumbbell: metal:4 sport:4 $heavy:2 inhand:4
a fence: wall:0 white:2 farm:3 long:4 $outdoors:4
a floor: wood:2 rock:2 floor:2 clean:1 washable:4
a globe: round:4 school:3 info:4 rolls:2 parts:2
a hammock: strings:3 hang:1 comfort:3 bedroom:0 $outdoors:4
a litter box: pet:0 smell:4 container:4 floor:4 clean:1
a mailbox: metal:3 plastic:2 writing:2 info:1 container:4 opens:4 lid:3
a mud puddle: liquid:3 weather:2 brown:4 soft:3 drink:0
a puppet: talk:2 played:1 toy:4 cute:2 colorful:3
a scarecrow: two_legs:2 farm:4 holiday:2 scary:3 face:4 decor:2 cloth:3 wood:2
a seatbelt: wear:3 metal:2 plastic:2 carpart:4 parts:2 everyday:3
a serving tray: metal:2 plastic:2 wood:2 container:3 eatwith:1 kitchen:4 flat:4
a shed: garage:2 container:4 opens:4 building:4
a sidewalk: rock:2 white:1 everyday:3 travel:3 $outdoors:4
a slide: school:3 vehicle:2 toy:4 $outdoors:4 parts:0
a slinky: metal:2 colorful:2 toy:4 moves:2 bounce:2 parts:1
a sprinkler: water:4 wet:4 noise:2 parts:3 liquid:0 hasliquid:2 winter:0
a staircase: wood:3 metal:1 rock:2 handle:2 everyday:3 $indoors:3
a steak: meat:0 ismeat:4 cooked:4 sliced:4 eat:4 farm:2 expensive:1 salty:2 fingers:0
a stethoscope: hospital:4 wear:3 tool:4 plastic:2 metal:3 cord:2
a sunset: orange:4 red:3 yellow:3 colorful:4 night:2 sky:4 weather:1
a tablecloth: cloth:4 kitchen:3 washable:4 fold:4 flat:4
a tennis racket: sport:4 strings:4 hit:3 plastic:2 metal:2 inhand:4
a watering can: water:4 metal:2 plastic:3 garage:2 hasliquid:3 container:4 handle:4 $outdoors:3
a workbench: tool:1 fix:3 garage:4 wood:3 metal:2
a yoga mat: sport:3 fold:4 floor:4 plastic:3 soft:3 flat:4
an incense stick: smell:4 burn:4 hot:2 long:4 decor:1
earplugs: wear:3 soft:4 pairs:4 plastic:2 drugstore:4 onhead:2 disposable:2
fire: hot:4 moves:3 dangerous:4 burn:2 smell:3 light:4 noise:2
moss: green:4 soft:4 wet:3 forest:4 rock:0 plant:4 alive:4 grows:4
roller skates: wheels:4 feet:4 wear:4 sport:3 pairs:4 parts:3
the moon: round:4 night:4 sky:4 rock:3 white:4 light:3 shiny:3
the sun: hot:4 light:4 yellow:4 round:4 sky:4 dangerous:2 everyday:0 weather:3
a bag of flour: white:4 cook:4 baked:1 paper:3 grocery:4 kitchen:4 soft:3
a barn: farm:4 red:2 building:4 wood:3 place:4 container:3
a bath mat: bathroom:4 floor:4 wet:4 soft:4 washable:4 cloth:3
a beach: water:4 hot_place:3 swimin:4 foodthere:1 place:4 yellow:2
a bed sheet: bedroom:4 cloth:4 washable:4 soft:4 fold:4 white:2 comfort:3
a block of tofu: white:4 soft:4 cooked:3 eat:4 grocery:4
a boxing glove: sport:4 hit:4 red:3 pairs:4 wear:4 soft:2 handle:0
a burrito: eat:4 cooked:4 long:3 ismeat:2 fingers:4 hot:2 rolls:1
a bush: green:4 leaves:4 plant:4 alive:4 grows:4 flower:2 wild:3 $outdoors:4
a butter dish: kitchen:4 lid:4 container:4 dairy:1 glass:2 plastic:2
a button: round:3 flat:3 hole:4 plastic:3 metal:2 wear:2 clothes:0
a car seat: baby:4 carpart:3 plastic:3 cloth:3 handle:3
a chip clip: plastic:4 kitchen:4 parts:2 colorful:3
a coaster: flat:4 round:3 kitchen:3 set:3 drink:0 wood:2 rock:1
a coat rack: wood:3 metal:2 furniture:3 $legs:3 floor:4 $indoors:4
a coffee table: furniture:4 wood:3 glass:2 $legs:4 flat:4 four_legs:3 floor:4
a colander: hole:4 kitchen:4 cook:4 metal:3 plastic:2 handle:3 water:2 wet:3
a feather duster: feathers:4 clean:4 handle:4 long:3 soft:3
a field: green:4 flat:4 grows:4 farm:3 sport:3 place:4 $outdoors:4
a filing cabinet: office2:4 metal:4 container:4 opens:4 paper:1 info:2 floor:4
a garage: building:4 place:3 opens:4 container:4 garage:4
a grilled cheese: dairy:4 cooked:4 fingers:4 hot:2 eat:4 yellow:2 brown:2 flat:4
a hamster wheel: pet:0 round:4 wheels:3 noise:3 plastic:3 metal:2 parts:4
a helmet: wear:4 onhead:4 plastic:3 sport:3 $hard:4 round:3
a jack-o-lantern: orange:4 face:4 holiday:4 light:3 night:3 scary:3 decor:3 seeds:3
a jewelry box: container:4 lid:4 opens:4 bedroom:4 wood:3 gift:3 music:1
a leash: pet:0 long:4 cloth:2 plastic:2 handle:4 inhand:4
a level: tool:4 yellow:3 long:4 flat:3 glass:2 liquid:1 hasliquid:3 hardware:4
a license plate: metal:4 flat:4 writing:4 carpart:4 info:3
a locker: metal:4 school:4 opens:4 container:4
a net: strings:4 sport:3 hole:4 seethrough:3 fold:4
a painting: decor:4 colorful:3 wall:3 hang:4 expensive:2 cloth:2 wood:2
a peephole: glass:4 hole:4 seethrough:4 wall:4 round:4
a picnic table: $legs:4 eatwith:2 $outdoors:4 camping:4 four_legs:2
a piece of bark: forest:4 wood:4 brown:4 tree_grow:4
a piece of sushi: ismeat:2 fish:0 ocean:0 fingers:3 eat:4 white:2 cooked:1 expensive:0
a pillow: soft:4 bedroom:4 comfort:4 everyday:4 cloth:4
a pizza box: paper:4 container:4 opens:4 disposable:3 writing:3 lid:3 hot:1 brown:2
a plant: green:4 leaves:4 grows:4 alive:4 decor:3 flower:2
a plate of poutine: salty:4 dairy:3 hot:2 cooked:4 brown:3 fingers:1
a plate of spaghetti: cooked:4 long:3 red:2 hot:2 fingers:0 sauce:0
a pool noodle: float:4 water:4 toy:4 colorful:4 soft:4 swimin:0 long:4 hole:4
a potato masher: cook:4 kitchen:4 metal:3 plastic:2 handle:4 inhand:4
a present: gift:4 holiday:4 paper:3 box:2 container:4 colorful:4 opens:4
a quilt: cloth:4 bedroom:4 comfort:4 winter:3 washable:4 soft:4 colorful:3
a road: black:4 travel:4 $outdoors:4 long:4 rock:1 everyday:3 place:4 flat:4
a robe: wear:4 clothes:4 soft:4 bathroom:3 bedroom:4 comfort:3
a rolling pin: wood:4 kitchen:4 cook:4 baked:0 round:3 long:3 rolls:4
a rope: long:4 strings:2 cloth:3 plastic:2 camping:3 hardware:4
a scale: bathroom:3 kitchen:2 floor:3 metal:2 plastic:2 glass:2 screen:2 battery:2 info:1
a school: building:4 place:4 foodthere:2 shop:0 everyday:2 school:4
a sign: writing:4 read:4 metal:3 flat:4 info:3 $outdoors:3
a sleeping bag: camping:4 zipper:4 cloth:4 soft:4 comfort:3 fold:4 winter:2
a stick of chalk: white:3 write:4 school:4 colorful:2 fragile:3 rock:1
a stop sign: red:4 writing:4 read:4 metal:4 flat:4 $outdoors:4 white:2
a trampoline: bounce:4 jumps:0 toy:4 $outdoors:4 round:3 metal:3 cloth:2 played:1
a tripod: $legs:4 metal:3 plastic:2 fold:4 parts:3 black:3
a tub of play dough: toy:4 soft:4 colorful:4 lid:4 smell:3 container:3 school:2
a tunnel: travel:4 long:4 place:3 $outdoors:3 rock:2 underground:0
a urinal: bathroom:4 wall:4 white:4 water:4 smell:3
a vase: decor:4 flower:3 fragile:3 glass:3 container:4 water:2
a vent: wall:3 floor:2 metal:4 hole:4 $indoors:4 dangerous:0 cold:2 hot:1
a violin: music:4 played:4 strings:4 wood:4 noise:4 expensive:3
a waffle: breakfast:4 sweet:3 cooked:4 baked:2 flat:4 hole:0 yellow:2 brown:2 fingers:2
a wheel: round:4 rolls:4 wheels:4 black:3 metal:3 carpart:3
a whoopee cushion: toy:4 noise:4 blow:4 soft:3 plastic:3 flat:3 smell:0
a wind chime: noise:4 hang:3 metal:3 $outdoors:4 decor:3 music:2 rings:2
an ice bucket: cold:3 container:4 handle:3 metal:2 plastic:3 wet:3
rain: water:4 liquid:4 fallsky:4 weather:4 wet:4 sky:3 drink:1 cold:2
a baking sheet: metal:4 flat:4 cook:4 kitchen:4 baked:2 hot:2 dangerous:1
a ball of yarn: round:4 soft:4 cloth:3 strings:3 long:3 colorful:3
a bell: noise:4 rings:4 metal:4 music:3 school:3 holiday:2 hit:2
a birdbath: water:4 rock:3 $outdoors:4 decor:3 container:4 round:3
a bookshelf: furniture:4 wood:4 floor:4 container:3 bedroom:3 office2:3
a bottle cap: lid:4 metal:3 plastic:2 round:4 disposable:4 flat:3 pocket:4
a bowl: round:4 container:4 kitchen:4 eatwith:4 everyday:3 glass:2 plastic:2
a bowling pin: sport:4 white:4 red:3 set:3 played:2 throw:0 hit:2
a bridge: travel:4 long:4 water:4 metal:3 rock:2 place:4
a bulletin board: wall:4 hang:4 flat:4 school:4 office2:4 paper:2 read:3 writing:2
a bungee cord: long:4 metal:2 colorful:3 hardware:4
a buoy: float:4 water:4 ocean:3 red:2 orange:2 round:3 plastic:3
a cactus: thorns:4 sharp:3 green:4 hot_place:4 plant:4 alive:4 flower:2
a cake: sweet:4 dessert:4 baked:4 gift:2 holiday:3 sliced:4 soft:3 colorful:3
a can of paint: liquid:0 hasliquid:4 metal:4 lid:4 hardware:4 smell:4 colorful:3
a cardboard box: paper:4 container:4 brown:4 opens:4 fold:4 box:2
a cattail: plant:4 water:4 brown:4 long:4 wild:4 grows:4
a ceiling: $indoors:4 white:4 flat:4 sky:3 everyday:4 wall:2
a cereal box: paper:4 container:4 writing:4 colorful:4 kitchen:4 breakfast:2 grocery:4
a chain: metal:4 long:4 noise:2 hardware:4 strings:0
a cloud: sky:4 white:4 weather:4 soft:2 flies:2 fallsky:0 watery:3 seethrough:1
a coloring book: paper:4 colorful:3 write:4 read:2 school:3 toy:2
a compass: round:3 metal:2 travel:4 camping:4 info:2 glass:2
a cooler: cold:3 container:4 camping:4 beach:4 lid:4 handle:4 plastic:4
a crate: wood:4 container:4 farm:3 brown:3 garage:3 carry:3
a dartboard: round:4 game:4 played:4 wall:4 hang:4 sport:3
a dollhouse: toy:4 container:3 opens:3 colorful:3 wood:3 plastic:3 decor:2
a doormat: floor:4 flat:4 $outdoors:3 brown:3 writing:2 everyday:3
a dress: wear:4 clothes:4 cloth:4 colorful:3 lower:2 bedroom:3
a dresser: furniture:4 wood:4 container:4 opens:4 bedroom:4 floor:4 drawer:0
a feather: feathers:4 soft:4 white:2 float:4 light:0 $light:4 long:3
a fireplace: hot:3 winter:4 holiday:3 wall:4 floor:4 comfort:3 rock:2 burn:2
a flower pot: flower:3 container:4 plant:1 brown:3 decor:3 fragile:2 hole:3
a forest: leaves:4 green:4 wild:4 place:4 grows:4 forest:2 scary:2 camping:4
a Do Not Disturb sign: writing:4 read:4 hang:4 paper:2 plastic:2 traveller:4 flat:4
a dock: water:4 wood:3 long:4 $outdoors:4 place:3 swimin:0
a gold bar: metal:4 yellow:4 shiny:4 money:4 expensive:4 $steal:4 rock:0
a hanger: bedroom:4 hang:3 clothes:1 metal:2 plastic:3 wood:2
a jump rope: toy:4 sport:3 long:4 strings:2 handle:4 school:3 jumps:0
a lake: water:4 swimin:4 fish:0 wild:2 cold:2 liquid:3 place:4 winter:2
a mannequin: face:3 two_legs:2 $legs:3 scary:3 plastic:4 wear:1 shop:0
a microphone: talk:3 music:4 electric:3 cord:3 speaker:0 inhand:4 noise:2
a mouse pad: withpc:4 desk:4 office2:4 flat:4 soft:3
a pacifier: baby:4 mouth:4 plastic:3 drugstore:4 comfort:3
a parking meter: money:4 payuse:4 metal:4 $outdoors:4 screen:2 buttons:2
a photo album: info:3 gift:3 paper:3 opens:4 read:1 decor:1
a sandwich: eat:4 fingers:4 snack:3 sliced:3 flat:3 baked:2 breakfast:1
a spider web: sticky:4 white:3 fragile:3 seethrough:4 scary:2 holiday:2
a thimble: metal:4 wear:2 drawer:3 shiny:3
a toy block: toy:4 colorful:4 baby:4 wood:2 plastic:3 set:4
a wall: flat:4 everyday:4 $indoors:3 $outdoors:2 white:3 rock:2 wood:2 floor:0
a water gun: toy:4 water:4 plastic:4 wet:4 colorful:4 hasliquid:3 beach:3 weapon:1
a waterfall: water:4 loud:3 noise:4 rock:3 wet:4 place:4 wild:3 $livewater:2
a windshield: glass:4 carpart:4 seethrough:4 fragile:3 wet:3 flat:3
an air freshener: smell:4 bathroom:3 plastic:3 grocery:4 tube:2
an eraser: write:3 school:4 desk:4 soft:3 pocket:4
a baby gate: baby:4 opens:4 plastic:3 metal:2 wood:2 hardware:4
a bag of trail mix: snack:4 salty:3 sweet:2 crunchy:4 camping:4 fingers:4
a barrel: wood:3 metal:2 plastic:2 round:4 container:4 rolls:4 lid:3 farm:2
a billboard: writing:4 read:4 sky:3 colorful:3 $outdoors:4 flat:4
a bottle opener: metal:4 kitchen:4 drawer:4 tool:3 opens:2
a brick: red:3 rock:3 hardware:4 $hard:4 set:2 baked:2
a car jack: tool:4 metal:4 garage:4 carpart:3 carry:4 fix:4
a chalkboard: write:4 school:4 black:3 green:2 wall:4 flat:4
a clipboard: write:3 paper:2 plastic:3 office2:4 hospital:3 school:3 flat:4
a conveyor belt: moves:3 electric:4 long:4 flat:3 parts:4 shop:0 carry:3
a cork: wood:4 brown:4 float:4 lid:3 round:3 soft:2
a couch: furniture:4 soft:4 comfort:4 withtv:4 cloth:3 everyday:4 floor:4
a crane (machine): metal:4 yellow:3 sky:4 long:4 carry:4 engine:3 vehicle:2
a dog bowl: pet:0 round:4 container:4 floor:4 metal:3 plastic:3 kitchen:3
a drumstick: wood:4 music:4 hit:4 pairs:4 long:4 played:2
a gas station: payuse:4 shop:4 foodthere:4 smell:3 travel:4 building:4 place:4
a gate: opens:4 metal:3 wood:3 farm:3 $outdoors:4 hardware:3 parts:3
a glow stick: light:4 colorful:4 plastic:4 night:3 disposable:4 toy:3
a hamburger: eat:4 cooked:4 ismeat:4 fingers:4 round:3 hot:2 brown:3
a handrail: handle:3 long:4 metal:3 wood:3 wall:4 inhand:3
a harmonica: music:4 played:4 metal:3 mouth:4 blow:4 noise:4 pocket:4
a hot dog: eat:4 ismeat:4 cooked:4 long:4 fingers:4 salty:3 camping:3
a house: building:4 livein:4 place:4 expensive:4 everyday:4 comfort:3
a life jacket: water:4 float:4 orange:4 wear:4 swimin:1 beach:3 sport:2
a magnifying glass: glass:4 seethrough:4 round:3 handle:4 tool:3 school:2
a marble: glass:4 round:4 rolls:4 toy:4 colorful:3 shiny:3 game:3
a mask: wear:4 face:4 onhead:4 holiday:3 scary:3 hole:4 plastic:3 cloth:2
a mattress: bedroom:4 soft:4 comfort:4 flat:4 floor:3 cloth:3
a measuring cup: kitchen:4 cook:4 container:4 handle:3 glass:2 plastic:3 metal:2
a medicine cabinet: bathroom:4 wall:4 opens:4 container:4 glass:3
a menu: read:4 writing:4 paper:3 flat:3 money:2 foodthere:0
a milkshake: drink:4 sweet:4 cold:4 dairy:4 dessert:3 liquid:3
a mint leaf: green:4 smell:4 leaves:2 plant:4 eat:3 grows:4 sweet:0
a mountain: rock:4 sky:4 place:4 cold_place:3 winter:3 forest:3 wild:3 $hard:4
a mouthguard: mouth:4 sport:4 plastic:4 team:3 wear:3 played:0
a nightstand: furniture:4 bedroom:4 wood:3 opens:3 floor:4 drawer:0
a paddle: water:4 sport:3 long:4 wood:2 plastic:2 metal:2 inhand:4 camping:3
a parachute: cloth:4 strings:4 fallsky:4 sky:3 fold:4 sport:2 colorful:3
a party hat: wear:4 onhead:4 paper:4 holiday:3 colorful:4 disposable:3
a pebble: rock:4 round:3 smooth:3 beach:4 throw:3 water:3 pocket:4
a pillowcase: bedroom:4 cloth:4 washable:4 soft:4 fold:4
a pinwheel: blow:4 toy:4 colorful:4 parts:3 moves:2 plastic:3 paper:2
a placemat: eatwith:2 kitchen:4 flat:4 cloth:2 plastic:2 set:3
a popsicle stick: wood:4 flat:4 long:3 disposable:4 mouth:2 school:2
a pork chop: ismeat:4 eat:4 cooked:4 farm:3 sliced:2 fingers:1
a price tag: paper:4 writing:4 read:4 money:4 flat:4 shop:0
a puzzle: game:4 played:4 toy:3 set:3 paper:3 colorful:3 box:4
a rainbow: colorful:4 sky:4 weather:4 seethrough:3 light:2
a restaurant: foodthere:4 payuse:4 building:4 place:4 shop:2 smell:3
a safe: metal:4 money:4 container:4 opens:4 expensive:3 $hard:4
a seesaw: toy:4 school:3 vehicle:3 parts:4 long:4 $outdoors:4
a sheet of sandpaper: hardware:4 fix:3 paper:4 flat:4 garage:3 smooth:0
a skyscraper: building:4 sky:4 glass:4 metal:3 office2:4 place:4 livein:2
a stool: furniture:4 wood:3 metal:2 plastic:2 $legs:4 kitchen:3 round:3
a stylus: withpc:3 write:3 long:4 plastic:3 metal:2 pocket:4
a taco: eat:4 fingers:4 ismeat:3 crunchy:2 fold:3 spicy:2 cooked:4
a tarp: plastic:4 fold:4 camping:4 wet:3 $outdoors:4 hardware:4 flat:3
a tent: camping:4 cloth:3 zipper:4 fold:4 container:3 opens:4 $outdoors:4
a thermometer: hospital:4 info:3 glass:2 plastic:3 battery:2 mouth:2 drugstore:4
a tire: carpart:4 round:4 rolls:4 black:4 wheels:4 smell:2
a vest: wear:4 clothes:4 cloth:4 buttons:2 zipper:2
a zipper: metal:3 plastic:3 parts:4 clothes:0 wear:2
an action figure: toy:4 face:4 two_legs:3 plastic:4 $legs:4 set:2 gift:3
an egg carton: container:4 paper:3 plastic:2 kitchen:4 grocery:4 eggs:0 lid:3
an omelette: eat:4 cooked:4 breakfast:4 yellow:3 hot:2 eggs:0 fingers:0
an oven mitt: kitchen:4 cook:4 cloth:4 wear:3 hot:0 bedroom:0
binoculars: glass:4 pairs:4 camping:3 sky:1 seethrough:2 black:3
bubble wrap: plastic:4 noise:3 soft:3 seethrough:3 fold:4 disposable:3
glasses: glass:3 wear:4 onhead:4 seethrough:4 fragile:3 everyday:4 plastic:3 metal:2
gloves: wear:4 pairs:4 winter:3 clothes:4 cloth:3 feet:0
a Rubik's cube: toy:4 game:4 played:4 colorful:4 plastic:4 parts:4
a bagel: eat:4 breakfast:4 round:4 hole:4 baked:4 sliced:3 fingers:4
a baguette: eat:4 baked:4 long:4 brown:3 crunchy:3 sliced:3
a baseball cap: wear:4 onhead:4 clothes:4 sport:3 cloth:4
a bath bomb: bathroom:4 smell:4 round:3 colorful:3 wet:3 disposable:4
a bean bag chair: furniture:4 soft:4 comfort:4 floor:4 bedroom:3
a boat: vehicle:4 water:4 float:4 travel:4 expensive:4 engine:2
a bookmark: paper:3 flat:4 read:2 long:3 school:2
a bottle of mustard: yellow:4 sauce:4 tube:4 plastic:3 lid:4 grocery:4 spicy:1
a bow tie: wear:4 clothes:4 cloth:4 black:2 decor:2
a bowl of cereal: breakfast:4 crunchy:3 dairy:2 sweet:2 eat:4 fingers:0
a bowl of jello: dessert:4 sweet:4 cold:3 soft:4 colorful:3
a bowling ball: ball:4 round:4 rolls:4 sport:4 hole:4 throw:2
a branch: wood:4 tree_grow:4 long:4 brown:4 leaves:2 burn:4 forest:4
a brownie: sweet:4 dessert:4 baked:4 brown:4 fingers:4 snack:3
a bubble: round:4 fragile:4 blow:4 seethrough:4 flies:3 float:4 toy:3
a candy wrapper: disposable:4 plastic:3 paper:2 colorful:3 shiny:3 noise:2
a cinnamon stick: smell:4 brown:4 cook:3 tree_grow:3 sweet:1
a contact lens: wear:4 pairs:4 seethrough:4 plastic:3 drugstore:3 onhead:3
a croissant: breakfast:4 baked:4 eat:4 brown:3 soft:2 fingers:4
a cup of pudding: dessert:4 sweet:4 soft:4 cold:3 dairy:3 lid:3
a cup of yogurt: dairy:4 cold:4 breakfast:3 lid:4 white:2 soft:4
a desk: furniture:4 office2:4 school:4 flat:4 wood:3 $legs:4 four_legs:3
a dish rack: kitchen:4 wet:4 metal:3 plastic:3 container:3
a dustpan: clean:4 plastic:3 handle:4 flat:3 floor:2
a ferris wheel: vehicle:4 round:4 sky:4 payuse:4 electric:4 light:3
a fidget spinner: toy:4 parts:4 round:3 plastic:3 metal:2 moves:2
a fish tank: glass:4 water:4 container:4 hasliquid:4 pet:0 seethrough:4 light:3
a flute: music:4 played:4 blow:4 mouth:4 metal:3 long:4 school:3
a folder: paper:3 plastic:2 office2:4 school:4 container:3 flat:4
a funnel: plastic:3 metal:2 kitchen:3 garage:3 hole:4 hardware:3
a garden: plant:4 flower:4 green:4 leaves:4 grows:4 wet:3 place:3
a garlic press: kitchen:4 cook:4 metal:4 handle:4 parts:4 tool:3
a glass of lemonade: drink:4 sweet:4 yellow:4 cold:4 liquid:4
a golf club: sport:4 long:4 metal:4 hit:4 expensive:2 inhand:4
a grain of rice: white:4 eat:4 cooked:4 seeds:2 grocery:4
a grater: kitchen:4 cook:4 metal:4 sharp:4 blade:3 handle:3
a guitar: music:4 played:4 strings:4 wood:4 noise:4 expensive:3
a hat: wear:4 onhead:4 clothes:4 cloth:3 winter:2
a head of broccoli: veg:4 green:4 eat:4 salad:2 cooked:3 rabbits:3
a high chair: baby:4 furniture:4 kitchen:4 $legs:4 plastic:3 wood:2
a hockey puck: sport:4 team:4 hit:4 winter:3 black:4 round:4 flat:4 cold_place:3
a hockey stick: sport:4 team:4 long:4 hit:4 wood:3 winter:3
a hot water bottle: hot:3 comfort:4 winter:3 soft:3 hasliquid:4 bedroom:3
a hula hoop: toy:4 round:4 hole:4 plastic:4 colorful:3 sport:2
a jar of mayonnaise: white:4 sauce:4 lid:4 glass:2 plastic:3 grocery:4
a jar of peanut butter: sticky:4 brown:4 lid:4 breakfast:2 salty:2 sweet:1
a jelly bean: sweet:4 colorful:4 snack:3 holiday:3 fingers:4
a kaleidoscope: toy:4 colorful:4 glass:3 seethrough:2 round:3 long:3
a ladder: long:4 metal:3 wood:2 garage:4 hardware:4 fold:3 climbs:0
a ladle: kitchen:4 cook:4 eatwith:3 long:4 metal:3 plastic:2 handle:4
a lantern: light:4 night:4 camping:4 handle:4 battery:3 glass:3
a laundry basket: container:4 plastic:4 bedroom:3 clean:2 handle:3 hole:3
a lawn chair: furniture:4 fold:4 $outdoors:4 camping:4 beach:4 metal:3 plastic:3
a lighter: dangerous:3 light:3 plastic:4 hot:2 pocket:4
a lock: metal:4 opens:3 hardware:4 school:3 parts:3
a luggage cart: wheels:4 metal:4 traveller:4 carry:4 handle:4 vehicle:2
a magazine: read:4 paper:4 writing:4 colorful:4 flat:3 shiny:3
a medal: metal:4 round:3 shiny:4 sport:4 decor:2 wear:2
a muffin: baked:4 sweet:3 breakfast:4 eat:4 fingers:4 round:3
a mug of hot chocolate: drink:4 sweet:4 hot:2 winter:4 dairy:3 brown:4 comfort:4
a mushroom: eat:3 grows:4 forest:4 wild:3 plant:2 veg:2 brown:3 white:3 dangerous:2
a noodle: eat:4 cooked:4 long:4 white:3 soft:3 yellow:2
a nutcracker: holiday:4 decor:3 face:3 tool:2 wood:3 parts:3 two_legs:2
a pair of dice: game:4 played:4 white:4 throw:4 pairs:4 spots:4
a paper airplane: paper:4 flies:4 throw:4 toy:4 white:3 fold:3
a pencil case: school:4 container:4 zipper:3 opens:4 cloth:2 plastic:2
a pickle: green:4 salty:4 crunchy:4 eat:4 veg:2 fingers:4
a picture frame: decor:4 wall:3 hang:4 glass:3 wood:3 metal:2 plastic:2
a piece of string: strings:4 long:4 cloth:3 white:2
a piggy bank: money:4 container:4 cute:3 hole:3 fragile:3 toy:2
a pretzel: salty:4 baked:4 snack:4 brown:4 crunchy:3 hole:3
a ribbon: gift:4 holiday:3 colorful:4 long:4 cloth:4 decor:3 shiny:2
a river: water:4 long:4 liquid:4 swimin:3 wild:3 moves:3 place:4 $livewater:2
a roll of gift wrap: gift:4 holiday:4 paper:4 colorful:4 long:3 round:2
a roller coaster: vehicle:4 fast:4 scary:4 payuse:4 loud:4 sky:3 metal:4
a rug: floor:4 soft:3 cloth:4 flat:4 colorful:3 decor:3 washable:3
a ruler: long:4 flat:4 school:4 write:2 plastic:3 wood:2 metal:2 writing:3
a safety pin: sharp:3 metal:4 fix:3 pocket:4 parts:2 clothes:0
a sausage: ismeat:4 eat:4 cooked:4 long:4 breakfast:3 brown:3 salty:3
a scarf: wear:4 winter:4 long:4 soft:4 cloth:4 clothes:4 colorful:3
a scoop of ice cream: cold:4 sweet:4 dessert:4 dairy:4 melt:4 round:3
a scrub brush: clean:4 bathroom:3 kitchen:3 plastic:3 wet:3 handle:2
a shopping cart: wheels:4 metal:4 container:4 handle:4 vehicle:2 carry:3 shop:0
a shower: bathroom:4 water:4 wet:4 clean:4 everyday:4 wall:4 swimin:0
a shower cap: bathroom:4 plastic:4 wear:4 onhead:4 wet:3 drugstore:4
a shower head: bathroom:4 water:4 metal:3 wall:4 hole:4 shiny:3
a ski pole: sport:4 winter:4 long:4 pairs:4 metal:4 cold_place:3
a slice of french toast: breakfast:4 cooked:4 sweet:3 brown:3 flat:4 eggs:0 baked:1
a slice of garlic bread: baked:4 cooked:4 smell:4 crunchy:3 fingers:4 hot:2
a slice of lasagna: dairy:4 ismeat:3 cooked:4 baked:4 red:3 hot:2 fingers:0
a smoothie: drink:4 cold:4 sweet:3 colorful:3 breakfast:3 liquid:3 fruit:0
a snow globe: glass:4 water:4 decor:4 holiday:3 fragile:4 gift:3 hasliquid:4
a snowman: winter:4 white:4 cold:4 melt:4 face:4 holiday:3 $outdoors:4 watery:4
a soap dispenser: clean:4 bathroom:4 kitchen:3 plastic:3 hasliquid:4 tube:3
a spool of thread: strings:4 cloth:3 fix:3 round:3 colorful:3
a spoonful of sugar: sweet:4 white:4 cook:3 kitchen:4 grocery:4
a stick: wood:4 brown:4 long:4 tree_grow:3 forest:4 throw:3 burn:4
a stick of cotton candy: sweet:4 soft:4 sticky:4 colorful:4 melt:3
a sticker: sticky:4 flat:4 paper:3 colorful:4 school:3 toy:2
a surfboard: water:4 ocean:3 beach:4 sport:4 float:4 long:4 flat:4 vehicle:2
a teapot: kitchen:4 handle:4 lid:4 hot:2 container:4 hasliquid:3 fragile:2
a telescope: sky:4 night:4 glass:4 long:4 seethrough:2 expensive:3
a tie: wear:4 long:4 office2:3 clothes:4 cloth:4
a tire pump: tool:4 garage:4 carpart:3 hardware:4 blow:0 handle:3
a towel rack: bathroom:4 wall:4 metal:3 hang:3 long:4
a toy car: toy:4 wheels:4 rolls:4 colorful:3 metal:3 plastic:3
a tub of sour cream: dairy:4 white:4 cold:4 sauce:4 lid:4 grocery:4
a wok: kitchen:4 cook:4 metal:4 round:4 handle:4 hot:2
a wooden spoon: wood:4 kitchen:4 cook:4 long:4 handle:4
a wrench: tool:4 metal:4 garage:4 fix:4 hardware:4 handle:3
an ironing board: flat:4 long:4 fold:4 $legs:4 metal:3 cloth:3 clean:1
braces: mouth:4 metal:4 wear:4 expensive:4 teeth:0 shiny:3
mittens: wear:4 pairs:4 winter:4 soft:4 cloth:4 clothes:4
skis: sport:4 winter:4 pairs:4 long:4 cold_place:4 feet:4 vehicle:2
the ocean: water:4 salty:4 swimin:4 liquid:4 beach:4 place:4 wild:3 cold:2
a Christmas tree: holiday:4 green:4 decor:4 light:3 winter:4 $outdoors:2 $indoors:3 sliced:2 tree_grow:0 leaves:1 thorns:2
a bean: eat:4 seeds:3 veg:3 grows:4 farm:3 cooked:3 green:2 brown:2
a bib: baby:4 cloth:4 wear:4 kitchen:3 eatwith:2 washable:4 clothes:2
a blanket: soft:4 comfort:4 bedroom:4 cloth:4 winter:3 fold:4 washable:4
a bottle of wine: drink:4 glass:4 red:3 lid:4 hasliquid:4 liquid:3 tube:1 smell:2
a bowl of soup: eat:4 liquid:3 hot:2 cooked:4 winter:3 salty:3 eatwith:0
a bra: wear:4 clothes:4 cloth:4 pairs:2 bedroom:4 drawer:4
a broom: clean:4 long:4 handle:4 wood:3 plastic:3 floor:2 kitchen:3
a butter knife: eatwith:4 kitchen:4 metal:4 drawer:4 sharp:1 blade:2
a campfire: hot:4 light:4 night:4 camping:4 smell:4 dangerous:4 cook:3 bath:0 noise:2
a can opener: kitchen:4 tool:3 metal:4 opens:3 parts:4 drawer:4
a canoe: vehicle:4 water:4 float:4 long:4 camping:4 travel:3
a cashew: eat:4 snack:4 salty:3 crunchy:3 tree_grow:3 seeds:2
a chair: furniture:4 $legs:4 four_legs:3 wood:3 metal:2 plastic:2 floor:4 everyday:4
a chicken nugget: ismeat:4 cooked:4 fingers:4 salty:3 crunchy:3 snack:3
a cigarette: smell:4 dangerous:4 paper:3 white:3 mouth:4 hot:2 disposable:4 burn:4
a coat: wear:4 clothes:4 winter:4 $outdoors:3 zipper:3 buttons:3 cloth:4
a crib: baby:4 bedroom:4 furniture:4 wood:3 $legs:4 floor:4
a cup of coffee: drink:4 hot:2 brown:4 breakfast:4 smell:4 everyday:3 hasliquid:3
a curtain: cloth:4 hang:4 wall:3 opens:3 soft:3 fold:3
a dictionary: read:4 paper:4 writing:4 info:4 school:4 opens:4
a dishwasher pod: clean:4 kitchen:4 disposable:4 smell:3 grocery:4 dangerous:2
a donut: sweet:4 hole:3 dessert:3 snack:4 breakfast:3 round:4 fingers:4
a dreamcatcher: decor:4 hang:4 feathers:3 strings:3 bedroom:3 round:3
a drum: music:4 played:4 noise:4 loud:4 hit:4 round:4
a fishing hook: sharp:4 metal:4 water:3 camping:3 blade:3 pocket:4
a flower: plant:4 alive:4 colorful:4 smell:3 gift:3 grows:4 decor:3
a fly swatter: hit:4 plastic:4 handle:4 flat:3 insect:0
a food container: container:4 lid:4 kitchen:4 plastic:4 opens:4 washable:4
a french fry: eat:4 cooked:4 salty:4 fingers:4 yellow:4 long:3 snack:3
a furnace: winter:4 hot:3 appliance:4 metal:4 floor:4 dangerous:2 noise:2
a hairbrush: grooming:4 bathroom:3 bedroom:3 handle:4 plastic:3
a hammer: tool:4 metal:4 hit:4 fix:4 garage:4 hardware:4 handle:4 wood:2
a hard drive: info:4 withpc:4 electric:3 $electronic:4 office2:3
a heater: hot:3 winter:4 electric:4 plugin:4 appliance:3 cord:3
a hockey net: sport:4 team:4 strings:3 red:3 metal:3 hole:3 winter:3
a hot air balloon: sky:4 flies:4 vehicle:4 colorful:4 cloth:4 washable:2 payuse:3
a hot tub: water:4 swimin:3 wet:4 electric:3 $outdoors:3 dangerous:1 bath:0 comfort:2
a jar of salsa: spicy:3 red:4 sauce:4 glass:3 lid:4 grocery:4 snack:2
a key: metal:4 opens:3 pocket:4 everyday:4 hole:3 shiny:3
a key card: plastic:4 flat:4 traveller:4 opens:3 pocket:4
a keychain: pocket:4 everyday:3 hole:3 metal:2 plastic:2 decor:2
a kiddie pool: swimin:3 baby:3 water:4 toy:3
a kite: flies:4 sky:4 strings:4 toy:4 colorful:4 tail:2 cloth:2 plastic:3
a loaf of bread: baked:4 sliced:4 breakfast:4 brown:3 soft:3 grocery:4
a music box: music:4 played:3 decor:3 gift:3 parts:4 wood:3
a name tag: writing:4 read:4 wear:3 sticky:2 info:3
a necklace: wear:4 decor:4 gift:4 metal:3 shiny:3 strings:2
a needle: sharp:4 metal:4 fix:3 hole:4 dangerous:2
a notebook: paper:4 write:4 school:4 read:3
a paint roller: hardware:4 wet:3 rolls:4 handle:4
a paintbrush: write:2 wet:3 hardware:3 school:3 wood:3
a palm tree: hot_place:4 beach:4 tree_grow:0 leaves:4 sky:3
a pancake: breakfast:4 cooked:4 round:4 flat:4 sweet:3 sauce:0
a paper clip: metal:4 office2:4 desk:4 school:3 blade:0
a phone case: plastic:4 everyday:4 colorful:3
a photo: paper:4 flat:4 decor:3 gift:3 info:2 colorful:3
a pie: baked:4 dessert:4 sweet:4 sliced:4 round:4 holiday:3
a pinch of pepper: spicy:3 black:4 cook:4 sauce:3
a pinch of salt: salty:4 white:4 cook:4 everyday:3
a pine cone: forest:4 tree_grow:4 seeds:3 brown:4 thorns:1
a pine tree: green:4 forest:4 sky:3 thorns:2 leaves:2 smell:3 holiday:3
a pool table: game:4 played:4 sport:3 green:4 furniture:3
a pop can: metal:4 fizzy:4 hasliquid:4 drink:2 disposable:4 cold:2
a protractor: school:4 plastic:4 seethrough:3 flat:4 write:2
a radio: music:4 noise:4 speaker:4 electric:3 battery:2 played:3
a raisin: fruit:4 sweet:4 snack:4 brown:4 fingers:4
a rattle: baby:4 toy:4 noise:4 plastic:4 handle:3
a rubber band: office2:4 round:3 colorful:2
a sailboat: vehicle:4 water:4 float:4 cloth:3 ocean:3 travel:3 strings:3
a salt shaker: salty:4 pairs:3 kitchen:4 eatwith:2 glass:2 plastic:2 metal:2
a saw: tool:4 sharp:4 blade:4 metal:4 hardware:4 garage:4 dangerous:3 wood:2
a screw: metal:4 hardware:4 fix:4 sharp:2 garage:3
a shelf: wall:4 wood:3 metal:2 flat:4 hang:2 container:2 floor:1
a shoelace: strings:4 long:4 pairs:4 feet:2 cloth:3
a shopping bag: plastic:3 paper:2 cloth:2 container:4 handle:4 fold:4 carry:3
a skirt: wear:4 clothes:4 lower:4 cloth:4 colorful:3
a sled: winter:4 toy:4 vehicle:4 plastic:3 wood:2 cold_place:3
a spatula: kitchen:4 cook:4 flat:3 handle:4 plastic:3 metal:2
a sponge: clean:4 soft:4 wet:4 kitchen:4 bathroom:3 yellow:3 hole:3
a stalk of wheat: farm:4 yellow:4 plant:4 seeds:4 grows:4 baked:0 eat:2
a staple remover: office2:4 desk:4 metal:4 tool:3
a stapler: office2:4 desk:4 school:4 metal:3 plastic:3 tool:3
a stick of gum: sweet:3 sticky:3 mouth:4 eat:2 disposable:4
a sunflower: yellow:4 flower:4 seeds:4 farm:3 sky:2 plant:4
a sweater: wear:4 clothes:4 winter:3 soft:4 cloth:4 washable:4
a table: furniture:4 $legs:4 four_legs:3 flat:4 wood:3 everyday:4 kitchen:4
a tack or pin: sharp:4 metal:4 office2:4 school:3 wall:2
a tea bag: paper:4 drink:2 disposable:4 smell:3 strings:3
a thermos: hasliquid:4 container:4 lid:4 metal:4 camping:4 hot:1 cold:1
a tortilla: flat:4 round:4 soft:3 cooked:3 white:3 fold:4
a toy train: toy:4 wheels:4 set:4 parts:3 colorful:3 metal:2 plastic:3
a tree: tree_grow:0 wood:4 leaves:4 green:4 sky:3 wild:4 forest:4
a tube of lipstick: grooming:4 red:4 lid:4 wear:3 drugstore:4 mouth:2
a tulip: flower:4 colorful:4 plant:4 gift:3 alive:4
a ukulele: music:4 played:4 strings:4 wood:4 noise:4
a unicycle: vehicle:4 wheels:4 sport:2 metal:3 parts:3
a water cooler: water:4 cold:4 office2:4 drink:2 hasliquid:4 plastic:3
a water heater: water:4 hot:3 metal:4 appliance:4 hasliquid:4 floor:4
a whisk: kitchen:4 cook:4 metal:4 handle:4 baked:0 hole:3
a whistle: noise:4 loud:4 blow:4 sport:4 mouth:4 metal:2 plastic:3
a window: glass:4 seethrough:4 opens:4 fragile:3 wall:4 flat:4
a wine glass: glass:4 fragile:4 seethrough:4 eatwith:3 drink:0 kitchen:3
a xylophone: music:4 played:4 hit:4 noise:4 colorful:3 toy:3
a yo-yo: toy:4 strings:4 round:4 parts:3 plastic:3 wood:2
an acorn: tree_grow:4 seeds:4 brown:4 forest:4 round:3 lid:2 eat:0
an almond: eat:4 snack:4 tree_grow:3 seeds:3 crunchy:4 brown:4
an apron: kitchen:4 cook:4 wear:4 cloth:4 strings:3 clothes:2
an elevator: buttons:4 electric:4 carry:4 metal:4 moves:3 vehicle:3 building:1
an exit sign: red:4 light:4 writing:4 read:4 wall:4 electric:4
an ice cream scoop: kitchen:4 metal:4 round:3 handle:4 cold:1 dessert:1
an ice pack: cold:4 hospital:3 soft:3 plastic:4 flat:3 drugstore:3
an inhaler: hospital:3 drugstore:4 plastic:4 mouth:4 blow:1 dangerous:0
chopsticks: eatwith:4 pairs:4 wood:3 plastic:2 long:4 mouth:3
safety goggles: wear:4 onhead:4 plastic:4 seethrough:4 garage:4 school:3 hardware:4
sandals: wear:4 feet:4 pairs:4 hot_place:3 beach:4 clothes:4
shorts: wear:4 clothes:4 lower:4 hot_place:3 cloth:4
sunglasses: wear:4 onhead:4 glass:3 plastic:4 beach:4 black:3 seethrough:2
a LEGO brick: toy:4 plastic:4 colorful:4 set:4 hole:2 pocket:4
a baby: alive:4 mammal:4 cute:4 face:4 two_legs:1 noise:4 loud:4 soft:3
a baby bottle: baby:4 plastic:4 hasliquid:4 lid:4 mouth:3 drink:1
a bandana: cloth:4 wear:4 onhead:3 colorful:4 fold:4
a bar of soap: clean:4 smell:4 bathroom:4 wet:4 grooming:4
a basil leaf: green:4 smell:4 cook:4 leaves:2 plant:4 wild:1
a bed: furniture:4 bedroom:4 soft:4 comfort:4 floor:4 $legs:3 four_legs:3 everyday:4
a bell pepper: veg:4 fruit:2 seeds:4 crunchy:4 salad:3 red:3 green:3 yellow:2
a belt: wear:4 lower:4 clothes:3 brown:3 black:3 hole:4 metal:2
a bottle of ketchup: red:4 sauce:4 tube:4 plastic:3 lid:4 grocery:4 liquid:2
a bowl of gravy: brown:4 sauce:4 liquid:3 hot:2 salty:3 eatwith:0
a paper plate: washable:0 disposable:4 paper:4 eatwith:4
a pea: fruit:1 veg:4 green:4
a stress ball: bounce:1 soft:4
an eggplant: fingers:0 veg:4 fruit:2
a diamond: sharp:1 dangerous:0 blade:0 shiny:4 expensive:4
a pencil sharpener: dangerous:1 sharp:2 school:4
leggings: black:2
a bubble wand: blow:4 toy:4 water:2 wet:3
a cabinet: wall:3 opens:4 container:4 kitchen:4
a can: metal:4 grocery:4
a comb: grooming:4
a cupcake: baked:4 dessert:4 sweet:4 gift:2
a dandelion: blow:4 yellow:4 wild:4 flower:4
a dart: sharp:4 throw:4 game:4
a door: opens:4 handle:4 wall:4 wood:3 metal:2
a drone: flies:4 sky:3 battery:4 toy:3 noise:3
a firework: holiday:4 loud:4 sky:4 night:4 dangerous:4 light:4 colorful:4
a flag: holiday:3 cloth:4 hang:3 colorful:4 school:3
a football: ball:4 sport:4 team:4 throw:4 brown:3
a glue gun: hot:2 fix:4 sticky:3 electric:4
a hoodie: wear:4 clothes:4 soft:4 comfort:3 winter:3
a jar: glass:4 lid:4 container:4 seethrough:3
a lamp: light:4 electric:4 plugin:4 bedroom:3
a letter: paper:4 read:4 writing:4 envelope:4
a log: wood:4 burn:4 forest:4 tree_grow:2
a milk carton: dairy:1 paper:3 hasliquid:4 drink:2
a pizza: cooked:4 baked:4 sliced:4 fingers:4 dairy:4
a playing card: paper:4 game:4 set:4 flat:4 played:4
a potato: underground:4 veg:4 cooked:4 brown:4
a purse: handle:4 container:4 money:3 zipper:3
a rake: tool:4 long:4 garage:4 leaves:0
a scooter: wheels:4 vehicle:4 toy:3
a screwdriver: tool:4 fix:4 metal:4 handle:4
a slice of toast: breakfast:4 baked:4 crunchy:3 cooked:4
a snowflake: winter:4 cold:4 white:4 fallsky:4 melt:4 crunchy:0 fragile:3
a stamp: paper:4 envelope:4 money:3 sticky:3
a steering wheel: carpart:4 round:4 handle:3 inhand:4
a stove: kitchen:4 cook:4 hot:2 appliance:4
a street light: light:4 night:4 sky:3 electric:4 long:4
a suit: wear:4 clothes:4 office2:4 expensive:3
a swimsuit: swimin:4 water:4 beach:4 wear:4
a trumpet: music:4 played:4 blow:4 metal:4 loud:4
a walnut: shell:4 tree_grow:4 crunchy:4
a wheelchair: wheels:4 hospital:4 vehicle:4 travel:3
a whiteboard: write:4 school:4 office2:4 wall:3 white:4
a worm: underground:2 wild:4 soft:4 long:4
an air conditioner: cold:3 electric:4 appliance:4 noise:3
an escalator: moves:4 electric:4 travel:3 vehicle:2
an icicle: cold:4 winter:4 sharp:3 melt:4 seethrough:3
an ornament: holiday:4 decor:4 fragile:3 hang:3
pajamas: wear:4 night:4 bedroom:4 comfort:4
slippers: feet:4 pairs:4 soft:4 bedroom:4
swim goggles: swimin:4 water:4 pairs:0 onhead:4
tongs: kitchen:4 cook:4 metal:4 pairs:0
a Christmas stocking: holiday:4 hang:4 red:4 container:3
a Q-tip: bathroom:4 grooming:4 disposable:4 white:4
a jellyfish: face:0 bites:3 seethrough:3 soft:4
a leaf: fragile:1
a glass of water: pocket:0
a cob of corn: fruit:1 veg:4
a green bean: fruit:1 veg:4
a newspaper: everyday:1
a fan: cold:2
a bug: washable:0
a starfish: face:0 float:0
a pig: mouth:1
a sheep: mouth:0 eat:1
a fork: sharp:2 dangerous:1 blade:2
a hamster: expensive:1 $steal:1
a guinea pig: expensive:1 $steal:1
a hedgehog: dangerous:1
a toothpick: dangerous:1 blade:2
a battery: hasliquid:1 cord:0
a light bulb: cord:0
a snail: float:0
an olive: juicy:1
an egg: cold:2
a pineapple: blade:0
a rose: dangerous:1
ice skates: travel:1
a cucumber: fruit:2 veg:4
a zucchini: fruit:2 veg:4
a squash: fruit:2 veg:4
a pumpkin: fruit:2 veg:3
a hot pepper: fruit:2 veg:4
a dryer: dangerous:1
a cow: mouth:1
a goat: mouth:1
a chicken: mouth:2
a duck: mouth:1
a turkey: mouth:2
a crab: mouth:2
a lobster: mouth:2
a goose: mouth:1
a cow: mouth:2
a chicken: mouth:2
a goat: mouth:2
a pig: mouth:2
a sheep: mouth:2 eat:2
a turkey: mouth:2
a crab: mouth:2
a lobster: mouth:2
a duck: mouth:2
a fish: mouth:2
a guinea pig: expensive:2
a snail: float:2
a battery: cord:1
a taxidermy animal: alive:0 moves:0 $made:4 mammal:2 bird:1 fish:1 fur:3 feathers:1 face:4 teeth:2 horns:2 tail:2 $legs:2 four_legs:2 decor:4 scary:3 hang:3 wall:3 brown:3 expensive:3 $steal:1 $indoors:4 $outdoors:0 pet:0 farm:0 zoo:0 wild:2 eat:0 mouth:0 cute:1 soft:2 $hard:2 glass:1 wood:2 burn:3 washable:0 everyday:0 gift:1 smell:1 noise:0 sharp:0 dangerous:0 container:0 fragile:1 $household:0 hardware:0 grocery:0 drugstore:0 toy:0 played:0 comfort:0 bedroom:1 garage:1 $pickup:3 $movable:4 $small2:4 $car:0 $person:0 $light:0 $pound:3 $duck:2 $microwave:2 shoebox:1 pocket:0 $hold:2 $small:1 forest:0 $livewater:0 ocean:0 grows:0 cold:0 hot:0 smooth:1 shiny:0 colorful:0 rolls:0 float:1 floor:1 info:0 writing:0
'''
def table():
    out = {}
    for line in RAW.strip().splitlines():
        n, rest = line.split(':', 1)
        out[n.strip()] = {k: int(v) for k, v in (p.rsplit(':', 1) for p in rest.split())}
    return out
THIN = table()
