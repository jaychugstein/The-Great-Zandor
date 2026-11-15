# "Is it smooth?" (Nov 15, Jordan): does it feel smooth when you run your hand over it? Fur, hair, feathers, scales, spines,
# fuzz, bumps and rough surfaces are not smooth; skin like a dolphin's or a baby's is; paper, glass, metal, plastic,
# appliances and utensils usually are. Worked out for everything from what it's made of, then the exceptions by hand.
# (Survey answers still win; animals are set one by one in thin.py.)
FOOD = {   # food by how its outside feels
 4: 'an apple,a banana,a grape,a cherry,a plum,a tomato,an eggplant,a bell pepper,a hot pepper,an egg,a block of cheese,a stick of butter,a piece of chocolate,a chocolate bar,a piece of candy,a lollipop,a jelly bean,a candy cane,a bowl of jello,a cup of pudding,a cup of yogurt,a jar of honey,a scoop of ice cream,a popsicle,a noodle,a piece of caramel,a marshmallow,a block of tofu,a tub of sour cream,a jar of mayonnaise,a grain of rice,a pea,a bean,a blueberry,a cranberry,an olive,a sausage,a hot dog,a slice of ham,a slice of pepperoni,a can of whipped cream',
 3: 'a pear,a mango,a watermelon,a lime,a lemon,a radish,a zucchini,a carrot,a sweet potato,a stalk of celery,an onion,a clove of garlic,a mushroom,a pumpkin,a squash,a beet,a bagel,a pancake,a tortilla,a donut,a cupcake,a cake,a pie,a cookie,a muffin,a meatball,a pickle,a stick of cotton candy,a piece of sushi,a slice of lasagna,an omelette',
 2: 'an orange,a grapefruit,a potato,a cucumber,a cob of corn,a loaf of bread,a baguette,a croissant,a waffle,a slice of toast,a pretzel,a brownie,a cinnamon bun,a slice of french toast,a hamburger,a sandwich,a burrito,a taco,a pizza,a steak,a pork chop,a chicken wing,a chicken nugget,a strip of bacon,a strip of beef jerky,a grilled cheese,a slice of garlic bread,an avocado,a head of lettuce,a head of cabbage,a leaf of spinach,a leaf of kale,a mint leaf,a basil leaf,a green bean,a stalk of asparagus,a peanut,an almond,a cashew,a pistachio,a sunflower seed,a raisin,a piece of ginger,a granola bar,a french fry,a plate of poutine,a bowl of mac & cheese',
 1: 'a strawberry,a raspberry,a blackberry,a peach,a cracker,a potato chip,a nacho,a piece of popcorn,a head of broccoli,a head of cauliflower,a brussels sprout,a walnut,a cantaloupe,a cinnamon stick,a bag of trail mix,a pinch of salt,a pinch of pepper,a spoonful of sugar,a bowl of cereal',
 0: 'a kiwi,a pineapple,a coconut',
}
ROUGH = {   # things that aren't what their material suggests
 0: 'a sheet of sandpaper,a loofah,a scrub brush,a hairbrush,a toothbrush,a doormat,a teddy bear,a cactus,a pine cone,a Christmas tree,a wreath,a feather duster,a tennis ball,a pom-pom,a scratching post,a bath mat,a broom,a sponge,a toilet brush,a paintbrush,a hedgehog,a porcupine,a tree,a branch,a piece of bark,a tree stump,a pine tree,a palm tree,a bush,moss,a nest,a beard,hair,a strand of hair,an eyebrow',
 1: 'a brick,a rock,a boulder,a mountain,sand,dirt,a hill,a rope,a basket,a laundry basket,a sweater,a towel,a washcloth,a rug,a blanket,a quilt,a ball of yarn,a sleeping bag,a tarp,a golf ball,a cardboard box,a wooden crate,a sidewalk,a road,a parking lot,a field,a sock,socks,mittens,gloves,a toque,a scarf,a hoodie,a coconut,a pumice stone,a nail file,a grater,a doghouse,a fence,a wall,a beach,a seashell,a sled,a toboggan,a bale of hay,a straw hat,smoke,fire,a cloud,a snowman,snow,a sneaker,sneakers,a hockey stick,a baseball bat,a log',
 2: 'a basketball,a football,a soccer ball,a volleyball,a tire,a wheel,a shoe,boots,sandals,slippers,a pillow,a bed,a couch,a mattress,a chair,a bean bag chair,a car seat,a stroller,a T-shirt,jeans,a dress,a skirt,shorts,a coat,a jacket,a vest,a tie,a bow tie,a bag of flour,a paper bag,an envelope,a newspaper,a book,a map,a puzzle,a piece of string,a shoelace,a leaf,a flower,a rose,a tulip,a sunflower,a dandelion,a plant,a blade of grass,a stalk of wheat,a cattail,a bird feeder,a birdhouse,a picnic table,a bench,a stick,a popsicle stick,a skateboard,a surfboard,a yoga mat,a hockey puck',
 4: 'a pebble,a marble,a glass,a mirror,a window,a light bulb,a balloon,a bubble,an ice cube,an icicle,water,the ocean,a lake,a river,a pond,a puddle,ice skates,a snowflake,a pearl,a diamond,a ring,a coin,a key,a spoon,a knife,a fork,a plate,a bowl,a mug,a bathtub,a sink,a toilet,a refrigerator,a microwave,a phone,a tablet,a laptop,a TV,a computer monitor,a remote,a TV remote,a watch,a smartwatch,a pen,a pencil,a crayon,a marker,a ruler,a sheet of paper,a playing card,a credit card,a photo,a postcard,a sticker,a magnet,a bowling ball,a bowling pin,a billiard ball,a guitar,a violin,a piano,a desk,a table,a coffee table,a dresser,a nightstand,a bookshelf,a door,a doorknob,a car,a bus,an airplane,a boat,a kayak,a canoe,a tooth,a fingernail,a baby,a child,a person,lips,a dolphin,a whale,a seal,a frog,a worm,a snail,a jellyfish,an octopus,a hippo',
}
def table():
    out = {}
    for d in (FOOD, ROUGH):
        for v, names in d.items():
            for n in names.split(','): out[n.strip()] = v
    return out
SMOOTH = table()
def guess(t):
    """from what it's made of, for things not listed: the roughest material decides (a chair of wood and cloth: sometimes)"""
    if t.get('fur', 0) >= 3: return 0
    if t.get('thorns', 0) >= 3: return 0
    if t.get('feathers', 0) >= 3: return 1
    if t.get('scales', 0) >= 3: return 1
    if t.get('shell', 0) >= 3: return 2
    mats = [v for k, v in (('glass', 4), ('metal', 4), ('plastic', 4), ('paper', 4), ('wood', 3), ('cloth', 2)) if t.get(k, 0) >= 3]
    if mats: return min(mats)
    if t.get('appliance', 0) >= 3 or t.get('$electronic', 0) >= 3 or t.get('electric', 0) >= 3: return 4
    return None
