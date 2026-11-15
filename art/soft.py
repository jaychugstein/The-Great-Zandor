# "Is it soft or squishy?" (Nov 15, Jordan): soft = feels soft or gives a little when you press it (a pillow, fur, a towel,
# bread); squishy = squashes when you squeeze it (a sponge, a stress ball, jello). Hard things - metal, glass, wood, hard
# plastic, stone, bone, shells, crunchy food - are not. Worked out from what it's made of, then the exceptions by hand.
# (Survey answers still win.)
SET = {
 4: ('a pillow,a bean bag chair,a mattress,a blanket,a quilt,a teddy bear,a stuffed animal,a puppet,a towel,a washcloth,a bath mat,a robe,pajamas,'
     'a sweater,a hoodie,a scarf,mittens,socks,a toque,slippers,a sleeping bag,a dog bed,a cushion,a sponge,a loofah,a stress ball,a pool noodle,'
     'a marshmallow,a loaf of bread,a slice of bread,a bagel,a croissant,a muffin,a cupcake,a cake,a donut,a cinnamon bun,a pancake,a waffle,'
     'a bowl of jello,a cup of pudding,a cup of yogurt,a scoop of ice cream,a stick of cotton candy,a jar of mayonnaise,a tub of sour cream,'
     'a can of whipped cream,a stick of butter,a block of tofu,a banana,a peach,a plum,a tomato,a mango,a strawberry,a raspberry,a blackberry,'
     'a blueberry,a grape,an avocado,a kiwi,a jelly bean,a noodle,a plate of spaghetti,a slice of lasagna,a bowl of mac & cheese,an omelette,'
     'a tortilla,a hot dog,a sausage,a meatball,a tub of play dough,a ball of yarn,a cotton ball,a tissue,a napkin,a paper towel,a roll of toilet paper,'
     'a diaper,a feather,a cloud,snow,a snowflake,a mud puddle,a puddle,dirt,moss,a worm,a jellyfish,an octopus,a snail,a slug,a caterpillar,'
     'a baby,a strand of hair,a beard,a mustache,an eyebrow,an eyelash,lips,a tongue,a stomach,a belly button,a patch of skin,an earlobe,'
     'a balloon,a water balloon,a whoopee cushion,a bubble,a hot water bottle,an ice pack,earplugs,a pacifier,a dryer sheet,a pillowcase,a bed sheet'),
 3: ('a dog,a cat,a rabbit,a hamster,a guinea pig,a mouse,a sheep,a llama,a panda,a koala,a chipmunk,a squirrel,a ferret,a fox,a bear,a polar bear,'
     'a duck,a chicken,a goose,a swan,an owl,a parrot,a penguin,a bird,a seal,a frog,a person,a child,an ear,a nose,a cheek,a hand,a finger,a thumb,'
     'a T-shirt,a tank top,underwear,a bra,a dress,a skirt,shorts,leggings,a vest,a coat,a jacket,a tie,a bow tie,a bandana,a headband,a hair tie,'
     'gloves,a baseball cap,a hat,an apron,a bib,a curtain,a tablecloth,a rug,a placemat,a couch,a car seat,a yoga mat,a sock monkey,a scrunchie,'
     'a shower cap,a mask,a rubber duck,a slinky,a cheese,a block of cheese,a pear,a pickle,a cucumber,a zucchini,a mushroom,a fig,a cherry,'
     'a sandwich,a burrito,a hamburger,a slice of ham,a chicken nugget,a piece of sushi,a grilled cheese,a slice of french toast,a baguette,'
     'a slice of garlic bread,a brownie,a piece of caramel,a piece of chocolate,a bowl of oatmeal,a bowl of soup,a bowl of gravy,a jar of peanut butter,'
     'a jar of jam,a jar of honey,a pillow fort,a basketball,a soccer ball,a volleyball,a football,a tennis ball,a beach ball,a ball,a life jacket,'
     'a tent,a hammock,a parachute,a kite,a flag,a shopping bag,a paper bag,a sheet of paper,a newspaper,a magazine,a comic book,a leaf,a flower,'
     'a rose,a tulip,a dandelion,a blade of grass,seaweed,sand,a lip balm,a tube of lip balm,a tube of toothpaste,a tube of lipstick,a bar of soap'),
 1: ('a wooden crate,a sneaker,sneakers,boots,sandals,a shoe,jeans,a belt,a wallet,a purse,a backpack,a suitcase,a briefcase,a helmet,a book,'
     'a notebook,a cardboard box,an envelope,a hockey puck,a baseball,a golf ball,a bowling ball,a carrot,an apple,an onion,a potato,a raw potato,'
     'a coconut,a walnut,an almond,a peanut,a cashew,a pistachio,a cracker,a pretzel,a potato chip,a nacho,a cookie,a candy cane,a lollipop,'
     'a piece of candy,a chocolate bar,a granola bar,a strip of beef jerky,a strip of bacon,a steak,a pork chop,a chicken wing,a french fry,'
     'a piece of popcorn,a slice of toast,a pizza,a taco,a bell pepper,a hot pepper,a head of lettuce,a head of cabbage,a head of broccoli,'
     'a head of cauliflower,a stalk of celery,a stalk of asparagus,a green bean,a pea,a bean,a radish,a beet,a sweet potato,an eggplant,a squash,'
     'a pumpkin,a watermelon,a cantaloupe,a pineapple,an orange,a lemon,a lime,a grapefruit,a cob of corn,an olive,a raisin,a cranberry,a turtle,'
     'a crab,a lobster,a snake,a lizard,an alligator,a fish,a goldfish,a shark,a whale,a dolphin,an elephant,a hippo,a rhino,a horse,a cow,a pig,'
     'a goat,a deer,a moose,a camel,a giraffe,a zebra,a donkey,a buffalo,a kangaroo,a monkey,a gorilla,a lion,a tiger,a cheetah,a wolf,a raccoon,'
     'a skunk,a beaver,an otter,a sloth,a bat,a rat,a walrus,a seahorse,a stingray,an eagle,a turkey,a flamingo,an ostrich,a peacock,a starfish,'
     'a head,an arm,a leg,a foot,a toe,a back,a shoulder,a neck,an eye'),
}
def table():
    out = {}
    for v, names in SET.items():
        for n in names.split(','): out[n.strip()] = v
    return out
SOFT = table()
def guess(t):
    """for things not listed: what it's made of"""
    if t.get('fur', 0) >= 3: return 3
    if t.get('cloth', 0) >= 3: return 3
    if t.get('shell', 0) >= 3 or t.get('scales', 0) >= 3 or t.get('thorns', 0) >= 3: return 0
    if any(t.get(k, 0) >= 3 for k in ('metal', 'glass', 'wood', 'rock', '$hard')): return 0
    if t.get('plastic', 0) >= 3 or t.get('$electronic', 0) >= 3 or t.get('appliance', 0) >= 3: return 0
    if t.get('paper', 0) >= 3: return 2
    return None
