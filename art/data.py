# The game's knowledge: the questions, the things it can guess, and how each thing answers each question.
# Each thing has a few tags; a question asks about one tag. A tag written plainly means YES, +tag USUALLY,
# ~tag SOMETIMES, -tag RARELY, and anything not tagged is NO. Some answers are worked out (size, made by people...).
#   answers stored as 0 no, 1 rarely, 2 sometimes, 3 usually, 4 yes

# ------------------------------------------------------------------ the questions (key, text)
Q = [
 # size (worked out from each thing's size class)
 ('$small', 'Is it smaller than a loaf of bread?'),
 ('$person', 'Is it bigger than a person?'),
 ('$car', 'Is it bigger than a car?'),
 ('$pickup', 'Can you pick it up by yourself?'),
 ('$heavy', 'Is it heavy?'),
 ('pocket', 'Can it fit in a pocket?'),
 # what it is
 ('alive', 'Is it alive?'),
 ('$made', 'Is it made by people?'),
 ('$touch', 'Can you touch it?'),
 ('moves', 'Does it move by itself?'),
 ('mammal', 'Is it a mammal?'),
 ('bird', 'Is it a bird?'),
 ('fish', 'Is it a fish?'),
 ('reptile', 'Is it a reptile?'),
 ('insect', 'Is it a bug or insect?'),
 ('plant', 'Is it a plant?'),
 ('fruit', 'Is it a fruit?'),
 ('veg', 'Is it a vegetable?'),
 ('eat', 'Can you eat it?'),
 ('drink', 'Can you drink it?'),
 ('person', 'Is it a person?'),
 ('job', 'Is it a job?'),
 ('pretend', 'Is it make-believe?'),
 ('place', 'Is it a place?'),
 ('building', 'Is it a building?'),
 ('abstract', 'Is it an idea or a feeling?'),
 ('weather', 'Does it have to do with weather?'),
 ('sky', 'Is it found in the sky?'),
 ('space', 'Is it in outer space?'),
 ('vehicle', 'Can you ride in it or on it?'),
 ('furniture', 'Is it furniture?'),
 ('appliance', 'Is it an appliance?'),
 ('tool', 'Is it a tool?'),
 ('toy', 'Is it a toy?'),
 ('weapon', 'Is it a weapon?'),
 ('wear', 'Can you wear it?'),
 # animals
 ('fur', 'Does it have fur?'),
 ('feathers', 'Does it have feathers?'),
 ('scales', 'Does it have scales?'),
 ('shell', 'Does it have a shell?'),
 ('wings', 'Does it have wings?'),
 ('tail', 'Does it have a tail?'),
 ('horns', 'Does it have horns or antlers?'),
 ('$legs', 'Does it have legs?'),
 ('four_legs', 'Does it have four legs?'),
 ('two_legs', 'Does it walk on two legs?'),
 ('many_legs', 'Does it have more than four legs?'),
 ('stripes', 'Does it have stripes?'),
 ('spots', 'Does it have spots?'),
 ('face', 'Does it have a face?'),
 ('teeth', 'Does it have teeth?'),
 ('pet', 'Do people keep it as a pet?'),
 ('farm', 'Would you find it on a farm?'),
 ('zoo', 'Would you see it at a zoo?'),
 ('wild', 'Does it live in the wild?'),
 ('meat', 'Does it eat meat?'),
 ('eats_plants', 'Does it eat plants?'),
 ('eggs', 'Does it lay eggs?'),
 ('flies', 'Can it fly?'),
 ('swims', 'Can it swim?'),
 ('ocean', 'Does it live in the ocean?'),
 ('water', 'Is it found in or near water?'),
 ('night', 'Is it out at night?'),
 ('cold_place', 'Is it found where it is cold?'),
 ('hot_place', 'Is it found where it is hot?'),
 ('jungle', 'Does it live in a jungle?'),
 ('africa', 'Does it come from Africa?'),
 ('climbs', 'Can it climb?'),
 ('jumps', 'Can it jump?'),
 ('fast', 'Is it fast?'),
 ('bites', 'Can it bite or sting?'),
 ('cute', 'Is it cute?'),
 ('dangerous', 'Is it dangerous?'),
 # food and plants
 ('sweet', 'Is it sweet?'),
 ('cooked', 'Is it usually cooked?'),
 ('juicy', 'Is it juicy?'),
 ('seeds', 'Does it have seeds or a pit?'),
 ('peel', 'Can you peel it?'),
 ('tree_grow', 'Does it grow on a tree?'),
 ('underground', 'Does it grow underground?'),
 ('salad', 'Would you put it in a salad?'),
 ('snack', 'Is it a snack?'),
 ('breakfast', 'Do people eat it for breakfast?'),
 ('flower', 'Does it have flowers?'),
 # looks and feel
 ('green', 'Is it green?'),
 ('red', 'Is it red?'),
 ('yellow', 'Is it yellow?'),
 ('orange', 'Is it orange?'),
 ('brown', 'Is it brown?'),
 ('black', 'Is it black?'),
 ('white', 'Is it white?'),
 ('colorful', 'Is it usually colourful?'),
 ('round', 'Is it round?'),
 ('long', 'Is it long and thin?'),
 ('flat', 'Is it flat?'),
 ('soft', 'Is it soft?'),
 ('sharp', 'Is it sharp?'),
 ('shiny', 'Does it shine?'),
 ('liquid', 'Is it a liquid?'),
 ('hot', 'Is it hot?'),
 ('cold', 'Is it cold?'),
 ('smell', 'Does it have a strong smell?'),
 ('noise', 'Does it make a sound?'),
 ('fragile', 'Does it break if dropped?'),
 # what it's made of
 ('metal', 'Is it made of metal?'),
 ('plastic', 'Is it made of plastic?'),
 ('wood', 'Is it made of wood?'),
 ('glass', 'Is some part of it made of glass?'),
 ('paper', 'Is it made of paper?'),
 ('cloth', 'Is it made of cloth?'),
 ('watery', 'Is it made of water?'),
 # what it does / where it is
 ('electric', 'Does it use electricity?'),
 ('battery', 'Does it use batteries?'),
 ('screen', 'Does it have a screen?'),
 ('buttons', 'Does it have buttons?'),
 ('wheels', 'Does it have wheels?'),
 ('engine', 'Does it have an engine?'),
 ('internet', 'Can it go on the internet?'),
 ('light', 'Does it give off light?'),
 ('container', 'Do you put things in it?'),
 ('opens', 'Can you open it?'),
 ('handle', 'Does it have a handle?'),
 ('pairs', 'Does it come in pairs?'),
 ('cook', 'Is it used for cooking?'),
 ('eatwith', 'Do you eat or drink with it?'),
 ('clean', 'Is it used for cleaning?'),
 ('write', 'Is it used to write or draw?'),
 ('read', 'Do you read it?'),
 ('talk', 'Is it used to talk to people?'),
 ('music', 'Is it used to make music?'),
 ('sport', 'Is it used in a sport?'),
 ('kitchen', 'Would you find it in a kitchen?'),
 ('bathroom', 'Would you find it in a bathroom?'),
 ('bedroom', 'Would you find it in a bedroom?'),
 ('office', 'Do you use it at work?'),
 ('garage', 'Would you find it in a garage?'),
 ('$indoors', 'Is it usually found indoors?'),
 ('$outdoors', 'Is it usually found outdoors?'),
 ('everyday', 'Would you use it daily?'),
 ('expensive', 'Is it considered valuable?'),
 ('gift', 'Is it given as a gift?'),
 ('holiday', 'Is it part of a holiday?'),
 ('old', 'Has it been around a long time?'),
 ('songs', 'Do you know any songs about it?'),
 ('washable', 'Can it be washed?'),
 ('tasks', 'Does it help accomplish tasks?'),
 ('$pound', 'Is it heavier than a pound of butter?'),
 ('enjoy', 'Can you enjoy it?'),
 ('travel', 'Is it used in travel?'),
 ('hasliquid', 'Does it contain a liquid?'),
 ('desk', 'Is it found on a desk?'),
 ('info', 'Does it store information?'),
 ('paint', 'Do people ever paint it?'),
 ('leaves', 'Does it have leaves?'),
 ('kinds', 'Are there many different sorts?'),
 ('rabbits', 'Do rabbits eat it?'),
 ('smooth', 'Is it smooth?'),
 ('$hard', 'Is it hard?'),
 ('larger', 'Does it come from something larger?'),
 ('rolls', 'Does it roll?'),
 ('wet', 'Does it get wet?'),
 ('sliced', 'Is it usually sliced or carved?'),
 ('envelope', 'Can it fit in an envelope?'),
 ('$small2', 'Is it small?'),
 ('forest', 'Does it live in the forest?'),
 ('$livewater', 'Does it live in water?'),
 ('claws', 'Does it have claws?'),
 ('$beak', 'Does it have a bill or beak?'),
 ('$duck', 'Does it weigh more than a duck?'),
 ('$hold', 'Can you hold it?'),
 ('$household', 'Is it a common household object?'),
 ('office2', 'Would you find it in an office?'),
 ('$home', 'Do you use it in your home?'),
 ('$steal', 'Would a thief want to steal it?'),
 ('$buy', 'Is it something you can purchase?'),
 ('$joy', 'Does it bring joy to people?'),
 ('public', 'Do you use it in public?'),
 ('$microwave', 'Is it larger than a microwave?'),
 ('$invented', 'Was it invented?'),
 ('withpc', 'Do you use it with a computer?'),
 ('addictive', 'Is it addictive?'),
 ('box', 'Does it come in a box?'),
 ('played', 'Can it be played?'),
 ('$bring', 'Is it something you bring along?'),
 ('comfort', 'Is it comforting?'),
 ('set', 'Is it from a set?'),
 ('$movable', 'Can it be easily moved?'),
 ('payuse', 'Would you pay to use it?'),
 ('$electronic', 'Is it electronic?'),
 ('writing', 'Does it have writing on it?'),
 ('$huge', 'Is it very large?'),
 ('uniform', 'Does it wear a uniform?'),
 ('hospital', 'Is it found in a hospital?'),
 ('royal', 'Is it royal?'),
 ('foodthere', 'Can you buy food there?'),
 ('scary', 'Is it scary?'),
 ('dessert', 'Is it a dessert?'),
 ('ball', 'Is it a ball?'),
 ('rings', 'Does it ring or beep?'),
 ('thorns', 'Does it have spines or thorns?'),
 ('body', 'Is it part of the body?'),
 ('onhead', 'Is it on your head?'),
 ('insidebody', 'Is it inside your body?'),
 ('five', 'Do you have five of them?'),
 ('plugin', 'Does it plug into the wall?'),
 ('feet', 'Do you wear it on your feet?'),
 ('clothes', 'Is it clothing?'),
]

# ------------------------------------------------------------------ the things
# (name with its article, category A/V/M/O, size class, tags)
# size: 0 tiny (coin, ant)  1 fits in a hand  2 loaf of bread / cat  3 person / chair  4 car / horse  5 house / whale  6 huge (mountain, sun)  x no size
OBJ = [
 # ---------- animals
 ('a dog', 'A', 3, 'mammal pet fur four_legs tail teeth meat ~eats_plants noise swims jumps fast ~bites cute +farm ~wild ~indoor brown ~black ~white ~night old'),
 ('a cat', 'A', 2, 'mammal pet fur four_legs tail teeth meat noise climbs jumps fast ~bites cute ~farm ~wild indoor ~black ~white ~orange ~stripes ~spots night old'),
 ('a horse', 'A', 4, 'mammal farm fur four_legs tail teeth eats_plants noise fast vehicle ~pet ~wild brown ~black ~white ~spots ~bites old ~zoo'),
 ('a cow', 'A', 4, 'mammal farm fur four_legs tail teeth eats_plants noise ~horns spots black white ~brown eat smell old'),
 ('a pig', 'A', 3, 'mammal farm four_legs tail teeth eats_plants ~meat noise eat smell cute ~pet ~wild ~black'),
 ('a sheep', 'A', 3, 'mammal farm fur four_legs tail teeth eats_plants noise white ~horns ~eat soft cute ~black'),
 ('a goat', 'A', 3, 'mammal farm fur four_legs tail teeth eats_plants noise horns jumps climbs ~eat ~zoo ~white ~brown ~pet smell'),
 ('a chicken', 'A', 2, 'bird farm feathers wings two_legs eggs eats_plants ~meat noise eat ~flies white ~brown ~red ~pet'),
 ('a duck', 'A', 2, 'bird farm feathers wings two_legs eggs swims flies water noise ~eat ~wild ~eats_plants ~meat ~white ~green ~brown ~yellow cute ~pet'),
 ('a turkey', 'A', 3, 'bird farm feathers wings two_legs eggs eats_plants noise eat holiday brown ~wild ~flies ~cooked'),
 ('a rabbit', 'A', 2, 'mammal pet fur four_legs tail teeth eats_plants jumps fast cute soft ~farm ~wild white ~brown ~black holiday'),
 ('a hamster', 'A', 1, 'mammal pet fur four_legs teeth eats_plants cute soft indoor ~bites brown ~white ~night pocket'),
 ('a mouse', 'A', 1, 'mammal fur four_legs tail teeth eats_plants ~pet ~wild noise fast night ~bites cute ~indoor ~farm white ~brown ~black pocket climbs'),
 ('a rat', 'A', 1, 'mammal fur four_legs tail teeth eats_plants ~meat ~pet wild night ~bites ~indoor ~farm brown ~black ~white climbs swims'),
 ('a squirrel', 'A', 1, 'mammal wild fur four_legs tail teeth eats_plants climbs jumps fast cute brown ~black ~red'),
 ('a raccoon', 'A', 2, 'mammal wild fur four_legs tail teeth meat eats_plants climbs night stripes ~bites black ~white swims ~dangerous'),
 ('a skunk', 'A', 2, 'mammal wild fur four_legs tail teeth meat eats_plants night stripes black white smell ~bites'),
 ('a fox', 'A', 3, 'mammal wild fur four_legs tail teeth meat ~eats_plants fast night orange ~red ~white ~cold_place jumps ~bites cute ~farm'),
 ('a wolf', 'A', 3, 'mammal wild fur four_legs tail teeth meat fast noise night dangerous bites ~zoo ~cold_place ~black ~white'),
 ('a deer', 'A', 4, 'mammal wild fur four_legs tail teeth eats_plants ~horns fast jumps brown ~spots ~eat ~cold_place cute ~zoo'),
 ('a moose', 'A', 4, 'mammal wild fur four_legs tail teeth eats_plants horns cold_place brown water swims ~dangerous ~zoo'),
 ('a bear', 'A', 4, 'mammal wild fur four_legs teeth meat eats_plants climbs swims dangerous bites zoo brown ~black ~cold_place noise ~fast'),
 ('a polar bear', 'A', 4, 'mammal wild fur four_legs teeth meat white cold_place swims water ocean dangerous bites zoo noise'),
 ('a panda', 'A', 4, 'mammal wild fur four_legs teeth eats_plants black white zoo cute climbs ~cold_place'),
 ('a koala', 'A', 2, 'mammal wild fur four_legs teeth eats_plants climbs zoo cute ~white hot_place night'),
 ('a kangaroo', 'A', 3, 'mammal wild fur two_legs tail teeth eats_plants jumps fast zoo hot_place brown ~dangerous'),
 ('a monkey', 'A', 3, 'mammal wild fur two_legs ~four_legs tail teeth eats_plants ~meat climbs jumps zoo jungle noise hot_place brown cute ~africa'),
 ('a gorilla', 'A', 4, 'mammal wild fur ~two_legs ~four_legs teeth eats_plants zoo jungle africa black dangerous hot_place climbs noise'),
 ('an elephant', 'A', 5, 'mammal wild four_legs tail teeth eats_plants zoo africa hot_place noise ~vehicle ~dangerous water swims old'),
 ('a giraffe', 'A', 5, 'mammal wild fur four_legs tail teeth eats_plants zoo africa hot_place spots yellow ~brown long fast'),
 ('a zebra', 'A', 4, 'mammal wild fur four_legs tail teeth eats_plants zoo africa hot_place stripes black white fast'),
 ('a lion', 'A', 4, 'mammal wild fur four_legs tail teeth meat zoo africa hot_place noise dangerous bites fast yellow ~brown'),
 ('a tiger', 'A', 4, 'mammal wild fur four_legs tail teeth meat zoo jungle stripes orange black ~white dangerous bites fast swims hot_place noise'),
 ('a cheetah', 'A', 4, 'mammal wild fur four_legs tail teeth meat zoo africa hot_place spots yellow fast dangerous bites'),
 ('a hippo', 'A', 5, 'mammal wild four_legs tail teeth eats_plants zoo africa hot_place water swims dangerous bites ~brown noise'),
 ('a rhino', 'A', 5, 'mammal wild four_legs tail teeth eats_plants zoo africa hot_place horns dangerous ~fast'),
 ('a camel', 'A', 4, 'mammal four_legs tail teeth eats_plants hot_place vehicle ~zoo ~farm ~wild brown ~africa smell'),
 ('a bat', 'A', 1, 'mammal wild fur wings flies teeth night ~meat ~eats_plants ~bites black ~brown noise climbs'),
 ('a beaver', 'A', 2, 'mammal wild fur four_legs tail teeth eats_plants water swims brown cold_place ~zoo'),
 ('an otter', 'A', 2, 'mammal wild fur four_legs tail teeth meat water swims ~ocean brown cute zoo'),
 ('a hedgehog', 'A', 1, 'mammal ~pet ~wild four_legs teeth meat ~eats_plants sharp brown cute night'),
 ('a sloth', 'A', 3, 'mammal wild fur four_legs teeth eats_plants jungle climbs zoo brown hot_place cute'),
 ('a whale', 'A', 6, 'mammal wild tail ocean water swims ~meat noise ~black ~white ~zoo old'),
 ('a dolphin', 'A', 4, 'mammal wild tail teeth meat ocean water swims jumps fast noise cute zoo ~white'),
 ('a seal', 'A', 3, 'mammal wild fur tail meat ocean water swims cold_place noise cute zoo ~white ~black'),
 ('a shark', 'A', 4, 'fish wild tail teeth meat ocean water swims fast dangerous bites ~zoo ~eggs ~white'),
 ('a penguin', 'A', 2, 'bird wild feathers wings two_legs eggs meat ocean water swims cold_place black white cute zoo noise'),
 ('an octopus', 'A', 2, 'wild many_legs meat ocean water swims ~bites ~eat ~zoo ~red ~eggs'),
 ('a jellyfish', 'A', 1, 'wild ocean water swims bites ~dangerous ~colorful ~zoo ~light'),
 ('a crab', 'A', 1, 'wild shell many_legs meat ~eats_plants ocean water swims bites eat ~red eggs ~cooked'),
 ('a lobster', 'A', 2, 'wild shell many_legs tail meat ocean water swims bites eat cooked ~red expensive eggs'),
 ('a starfish', 'A', 1, 'wild ocean water meat ~orange ~red flat ~eggs'),
 ('a goldfish', 'A', 1, 'fish pet tail water swims orange eggs eats_plants ~meat indoor cute shiny scales'),
 ('a salmon', 'A', 3, 'fish wild tail water swims ocean eat ~cooked eggs meat jumps ~red scales'),
 ('a clownfish', 'A', 1, 'fish wild tail ocean water swims orange white stripes eggs cute ~pet ~zoo scales'),
 ('a frog', 'A', 1, 'wild four_legs water swims jumps eggs meat green noise ~night ~pet cute'),
 ('a turtle', 'A', 2, 'reptile wild shell four_legs tail eggs water swims ~ocean ~eats_plants ~meat green ~pet ~zoo old'),
 ('a snake', 'A', 3, 'reptile wild tail scales eggs meat ~dangerous bites long ~green ~pet ~zoo swims ~hot_place ~jungle'),
 ('a lizard', 'A', 1, 'reptile wild four_legs tail scales eggs meat climbs fast ~pet green ~brown hot_place'),
 ('a crocodile', 'A', 5, 'reptile wild four_legs tail teeth scales eggs meat water swims dangerous bites zoo hot_place green long'),
 ('a chameleon', 'A', 1, 'reptile wild four_legs tail eggs meat climbs jungle green colorful ~pet ~zoo hot_place'),
 ('an owl', 'A', 2, 'bird wild feathers wings two_legs eggs meat flies night noise brown ~white ~zoo cute'),
 ('an eagle', 'A', 3, 'bird wild feathers wings two_legs eggs meat flies fast ~dangerous sky brown white ~zoo'),
 ('a parrot', 'A', 2, 'bird pet feathers wings two_legs eggs eats_plants flies noise colorful green red jungle ~zoo hot_place ~bites'),
 ('a pigeon', 'A', 1, 'bird wild feathers wings two_legs eggs eats_plants flies noise ~white ~black'),
 ('a crow', 'A', 1, 'bird wild feathers wings two_legs eggs eats_plants meat flies noise black'),
 ('a flamingo', 'A', 3, 'bird wild feathers wings two_legs eggs flies water zoo hot_place long ~meat'),
 ('an ostrich', 'A', 4, 'bird wild feathers wings two_legs eggs eats_plants fast zoo africa hot_place long ~dangerous'),
 ('a peacock', 'A', 3, 'bird feathers wings two_legs eggs ~flies colorful ~zoo ~farm noise ~green'),
 ('a swan', 'A', 3, 'bird wild feathers wings two_legs eggs flies swims water white ~black ~bites'),
 ('a hummingbird', 'A', 0, 'bird wild feathers wings two_legs eggs flies fast colorful ~green tiny cute pocket'),
 ('a bee', 'A', 0, 'insect wild wings flies many_legs stripes yellow black bites noise eggs flower pocket'),
 ('an ant', 'A', 0, 'insect wild many_legs eggs ~bites ~black ~red ~indoor pocket'),
 ('a butterfly', 'A', 0, 'insect wild wings flies many_legs eggs colorful cute flower pocket'),
 ('a spider', 'A', 0, 'many_legs wild meat bites eggs climbs black ~dangerous ~indoor pocket'),
 ('a mosquito', 'A', 0, 'insect wild wings flies many_legs bites noise night eggs water pocket'),
 ('a fly', 'A', 0, 'insect wild wings flies many_legs noise eggs ~indoor black pocket'),
 ('a ladybug', 'A', 0, 'insect wild wings flies many_legs spots red black eggs cute pocket shell'),
 ('a worm', 'A', 0, 'wild long eats_plants underground brown ~red pocket'),
 ('a snail', 'A', 0, 'wild shell eats_plants eggs water brown pocket'),
 ('a grasshopper', 'A', 0, 'insect wild wings ~flies many_legs jumps eggs eats_plants green noise pocket'),
 ('a cockroach', 'A', 0, 'insect wild wings ~flies many_legs eggs brown indoor night fast pocket'),
 ('a scorpion', 'A', 0, 'many_legs wild tail meat bites dangerous hot_place ~black ~brown pocket shell'),
 ('a dinosaur', 'A', 5, 'reptile ~pretend tail teeth ~meat ~eats_plants eggs scales dangerous old ~green ~zoo ~two_legs ~four_legs ~flies ~long'),
 # ---------- vegetable (plants, food from plants, things made of plants)
 ('an apple', 'V', 1, 'fruit eat sweet juicy seeds tree_grow red ~green ~yellow round snack old ~breakfast ~cooked gift'),
 ('a banana', 'V', 1, 'fruit eat sweet peel tree_grow yellow long snack breakfast soft'),
 ('an orange', 'V', 1, 'fruit eat sweet juicy seeds peel tree_grow orange round ~drink breakfast smell'),
 ('a lemon', 'V', 1, 'fruit eat juicy seeds tree_grow yellow ~round smell ~drink'),
 ('grapes', 'V', 1, 'fruit eat sweet juicy ~seeds green ~red ~black round snack pairs ~drink'),
 ('a strawberry', 'V', 0, 'fruit eat sweet juicy seeds red snack ~salad breakfast pocket smell flower'),
 ('a watermelon', 'V', 2, 'fruit eat sweet juicy seeds green red round heavy underground_no'),
 ('a pineapple', 'V', 2, 'fruit eat sweet juicy peel yellow brown ~green sharp hot_place'),
 ('a cherry', 'V', 0, 'fruit eat sweet juicy seeds tree_grow red round pairs pocket'),
 ('a peach', 'V', 1, 'fruit eat sweet juicy seeds tree_grow orange ~red ~yellow round soft'),
 ('a pear', 'V', 1, 'fruit eat sweet juicy seeds tree_grow green ~yellow ~brown'),
 ('a coconut', 'V', 2, 'fruit eat ~sweet drink tree_grow brown round hard hot_place ~white'),
 ('a blueberry', 'V', 0, 'fruit eat sweet juicy ~seeds round ~breakfast pocket snack'),
 ('an avocado', 'V', 1, 'fruit eat seeds peel tree_grow green ~salad ~breakfast ~black soft'),
 ('a tomato', 'V', 1, 'fruit ~veg eat juicy seeds red round salad ~cooked'),
 ('a potato', 'V', 1, 'veg eat cooked underground brown ~peel ~round ~yellow'),
 ('a carrot', 'V', 1, 'veg eat underground orange long salad ~cooked ~sweet snack ~peel'),
 ('an onion', 'V', 1, 'veg eat underground peel round smell ~white ~yellow ~red ~salad ~cooked'),
 ('lettuce', 'V', 1, 'veg eat green salad soft ~round'),
 ('broccoli', 'V', 1, 'veg eat green ~cooked ~salad flower'),
 ('corn', 'V', 1, 'veg eat yellow cooked ~sweet seeds long ~snack ~breakfast'),
 ('a pumpkin', 'V', 3, 'veg ~fruit eat orange round seeds cooked holiday heavy'),
 ('a cucumber', 'V', 1, 'veg ~fruit eat green long salad juicy seeds'),
 ('a mushroom', 'V', 0, 'eat ~veg ~cooked ~salad brown ~white ~dangerous ~round pocket'),
 ('peas', 'V', 0, 'veg eat green round seeds cooked pairs'),
 ('a peanut', 'V', 0, 'eat underground brown peel snack seeds pocket'),
 ('rice', 'V', 0, 'eat cooked white seeds'),
 ('bread', 'V', 2, 'eat ~cooked breakfast brown soft ~white $madefood smell'),
 ('french fries', 'V', 1, 'eat cooked hot long yellow snack $madefood'),
 ('popcorn', 'V', 1, 'eat cooked snack white $madefood seeds ~hot'),
 ('chocolate', 'V', 1, 'eat sweet brown snack $madefood gift holiday ~flat'),
 ('coffee', 'V', 1, 'drink hot liquid brown ~black breakfast seeds smell everyday $madefood ~cooked'),
 ('tea', 'V', 1, 'drink hot ~cold liquid ~brown ~green breakfast $madefood old'),
 ('a pizza', 'V', 2, 'eat cooked hot round flat ~red $madefood smell ~snack'),
 ('a sandwich', 'V', 1, 'eat $madefood ~flat snack'),
 ('cereal', 'V', 1, 'eat breakfast $madefood ~sweet colorful'),
 ('spaghetti', 'V', 1, 'eat cooked hot long $madefood ~yellow ~red'),
 ('a cookie', 'V', 0, 'eat sweet snack round flat $madefood ~brown pocket'),
 ('a cake', 'V', 2, 'eat sweet $madefood soft gift holiday ~round ~white ~colorful'),
 ('a tree', 'V', 6, 'plant alive green brown wood_grows tall_x old ~flower'),
 ('a flower', 'V', 1, 'plant alive colorful ~red ~yellow ~white gift smell fragile flower'),
 ('a rose', 'V', 1, 'plant alive red flower gift smell sharp holiday ~white'),
 ('a sunflower', 'V', 3, 'plant alive yellow flower seeds tall_x ~brown'),
 ('grass', 'V', 0, 'plant alive green long soft'),
 ('a cactus', 'V', 2, 'plant alive green sharp hot_place ~flower thorns ~indoor ~desk ~gift ~long'),
 ('a leaf', 'V', 1, 'plant ~alive green flat ~red ~yellow ~orange ~brown fragile tree_grow'),
 ('a pine cone', 'V', 1, 'brown seeds tree_grow ~sharp'),
 ('seaweed', 'V', 2, 'plant alive green ocean water ~eat long'),
 ('a log', 'V', 3, 'wood brown heavy ~hot long round'),
 ('paper', 'V', 1, 'paper flat white write office fragile $made everyday'),
 ('a book', 'V', 1, 'paper read office ~bedroom flat ~gift $made old opens'),
 ('a pencil', 'V', 1, 'wood write long office ~sharp yellow $made pocket everyday'),
 ('a cardboard box', 'V', 2, 'paper container brown opens $made ~flat'),
 ('a newspaper', 'V', 1, 'paper read flat white black $made everyday ~office'),
 ('a T-shirt', 'V', 1, 'cloth wear soft colorful $made everyday bedroom ~gift'),
 ('a towel', 'V', 2, 'cloth soft bathroom clean $made colorful everyday'),
 ('a chair', 'V', 3, 'furniture ~wood ~plastic ~metal $made indoor four_legs office kitchen everyday'),
 ('a table', 'V', 3, 'furniture wood ~plastic ~metal $made indoor four_legs kitchen flat ~office'),
 ('a door', 'V', 4, 'wood ~metal $made opens handle flat ~glass everyday'),
 ('a baseball bat', 'V', 2, 'wood ~metal $made sport long weapon_x handle'),
 ('a guitar', 'V', 3, 'wood $made music noise ~electric gift'),
 ('cotton', 'V', 1, 'plant white soft ~cloth'),
 ('maple syrup', 'V', 1, 'eat sweet liquid brown breakfast tree_grow $madefood'),
 ('a pickle', 'V', 1, 'eat green long ~salad $madefood smell'),
 ('peanut butter', 'V', 1, 'eat brown sweet breakfast snack $madefood'),
 ('a carrot cake_x', 'X', 0, ''),
 # ---------- mineral (rocks, metal, glass, plastic things)
 ('a rock', 'M', 1, 'hard ~round ~heavy ~black ~white ~brown old water_x'),
 ('sand', 'M', 0, 'yellow ~brown ~white hot_place water ocean soft'),
 ('a diamond', 'M', 0, 'shiny expensive gift wear sharp ~white pocket old'),
 ('gold', 'M', 1, 'metal shiny yellow expensive heavy wear_x old'),
 ('a ring', 'M', 0, 'metal shiny wear expensive gift round pocket ~gold_x'),
 ('a necklace', 'M', 1, 'metal shiny wear expensive gift long ~colorful'),
 ('a coin', 'M', 0, 'metal round flat shiny pocket everyday ~gold_x'),
 ('a key', 'M', 0, 'metal shiny pocket everyday opens_x'),
 ('scissors', 'M', 1, 'metal ~plastic tool sharp handle office ~kitchen pairs_x dangerous'),
 ('a knife', 'M', 1, 'metal sharp kitchen eatwith cook handle tool weapon dangerous everyday'),
 ('a fork', 'M', 1, 'metal ~plastic kitchen eatwith sharp shiny everyday'),
 ('a spoon', 'M', 1, 'metal ~plastic ~wood kitchen eatwith shiny everyday ~round'),
 ('a plate', 'M', 2, 'kitchen eatwith flat round ~glass fragile everyday ~white ~plastic'),
 ('a mug', 'M', 1, 'kitchen eatwith container handle ~hot ~glass fragile everyday ~colorful'),
 ('a glass', 'M', 1, 'glass kitchen eatwith container fragile round everyday'),
 ('a bottle', 'M', 1, '~glass ~plastic container opens kitchen ~fragile long'),
 ('a frying pan', 'M', 2, 'metal kitchen cook hot handle round flat black'),
 ('a pot', 'M', 2, 'metal kitchen cook hot handle container round'),
 ('a toaster', 'M', 2, 'appliance electric metal kitchen cook hot breakfast'),
 ('a microwave', 'M', 3, 'appliance electric kitchen cook hot buttons opens container noise light'),
 ('a refrigerator', 'M', 4, 'appliance electric kitchen cold container opens handle heavy white light'),
 ('a stove', 'M', 4, 'appliance ~electric kitchen cook hot heavy metal'),
 ('a sink', 'M', 3, 'metal ~white kitchen bathroom water clean handle_x everyday heavy'),
 ('a toilet', 'M', 3, 'white bathroom water heavy everyday handle fragile_x'),
 ('a bathtub', 'M', 4, 'white bathroom water container heavy clean'),
 ('a mirror', 'M', 2, 'glass shiny bathroom ~bedroom fragile flat everyday'),
 ('a light bulb', 'M', 1, 'glass electric light hot fragile round'),
 ('a lamp', 'M', 2, 'electric light bedroom ~office ~metal ~plastic furniture_x'),
 ('a TV', 'M', 3, 'electric screen buttons noise light ~internet expensive flat black ~bedroom everyday'),
 ('a computer', 'M', 2, 'electric screen buttons internet office expensive ~noise ~light everyday plastic'),
 ('a laptop', 'M', 2, 'electric battery screen buttons internet office expensive opens flat plastic'),
 ('a phone', 'M', 1, 'electric battery screen ~buttons internet talk noise expensive pocket everyday light flat'),
 ('a camera', 'M', 1, 'electric battery buttons ~screen expensive gift light'),
 ('a clock', 'M', 1, 'round ~battery ~electric noise ~bedroom ~kitchen ~office face old'),
 ('a watch', 'M', 0, 'wear battery ~metal round ~screen ~buttons gift ~expensive everyday pocket'),
 ('a radio', 'M', 2, 'electric ~battery buttons noise music talk_x old'),
 ('headphones', 'M', 1, 'electric ~battery wear noise music pairs plastic'),
 ('a video game console', 'M', 2, 'electric toy buttons ~screen ~internet expensive gift plastic noise'),
 ('a remote control', 'M', 1, 'battery buttons plastic ~black everyday'),
 ('a battery', 'M', 0, 'metal electric pocket ~round ~long'),
 ('a calculator', 'M', 1, 'battery buttons screen office plastic flat'),
 ('a car', 'M', 4, 'vehicle wheels engine metal moves_x expensive fast noise ~colorful everyday garage glass_x light'),
 ('a bicycle', 'M', 3, 'vehicle wheels metal sport garage ~colorful pairs_x'),
 ('a motorcycle', 'M', 4, 'vehicle wheels engine metal fast noise dangerous expensive garage'),
 ('a bus', 'M', 5, 'vehicle wheels engine metal yellow noise ~office ~everyday light'),
 ('a train', 'M', 5, 'vehicle wheels engine metal fast noise long light old'),
 ('an airplane', 'M', 5, 'vehicle wheels engine metal flies sky fast noise expensive wings white light'),
 ('a boat', 'M', 4, 'vehicle ~engine water ~ocean ~wood ~metal expensive swims_x'),
 ('a helicopter', 'M', 4, 'vehicle engine metal flies sky noise expensive fast'),
 ('a rocket', 'M', 5, 'vehicle engine metal flies sky space fast noise expensive dangerous hot long light'),
 ('a truck', 'M', 5, 'vehicle wheels engine metal noise heavy light'),
 ('a skateboard', 'M', 2, 'vehicle wheels wood toy sport flat'),
 ('a hammer', 'M', 2, 'tool metal ~wood handle garage heavy noise_x weapon_x'),
 ('a screwdriver', 'M', 1, 'tool metal handle garage long sharp_x'),
 ('a nail', 'M', 0, 'metal sharp long garage pocket'),
 ('a saw', 'M', 2, 'tool metal sharp handle garage dangerous noise'),
 ('a ladder', 'M', 4, 'tool metal ~wood garage long two_legs_x'),
 ('an umbrella', 'M', 2, 'cloth metal handle opens weather long ~colorful ~black'),
 ('a shovel', 'M', 3, 'tool metal ~wood handle garage long'),
 ('a bucket', 'M', 2, 'container plastic ~metal handle garage water ~toy'),
 ('a pen', 'M', 1, 'write plastic ~metal office long pocket everyday ~colorful'),
 ('a crayon', 'M', 1, 'write colorful toy long ~office pocket'),
 ('a ruler', 'M', 1, 'plastic ~wood office long flat'),
 ('a stapler', 'M', 1, 'metal office tool ~plastic noise'),
 ('a paper clip', 'M', 0, 'metal office shiny pocket'),
 ('a backpack', 'M', 2, 'cloth container wear opens office ~colorful everyday'),
 ('a shoe', 'M', 1, 'wear pairs ~cloth everyday ~black ~white ~colorful ~smell public box bring ~sport washable_x hard_x'),
 ('glasses', 'M', 1, 'wear glass ~plastic ~metal fragile everyday pocket'),
 ('a hat', 'M', 1, 'wear cloth ~soft ~colorful'),
 ('socks', 'M', 1, 'wear cloth soft pairs everyday ~white ~colorful bedroom pocket'),
 ('a balloon', 'M', 1, 'toy colorful round ~flies fragile soft holiday gift ~plastic'),
 ('LEGO bricks', 'M', 0, 'toy plastic colorful gift pocket'),
 ('a teddy bear', 'M', 2, 'toy soft cloth fur gift bedroom brown cute face'),
 ('a doll', 'M', 2, 'toy ~plastic ~cloth gift face cute ~bedroom'),
 ('a ball', 'M', 2, 'toy sport round colorful bounce_x'),
 ('a kite', 'M', 2, 'toy flies sky colorful ~cloth ~paper ~plastic'),
 ('a trumpet', 'M', 2, 'music metal shiny noise yellow'),
 ('a piano', 'M', 4, 'music furniture wood noise heavy expensive black white buttons_x old'),
 ('a drum', 'M', 2, 'music noise round ~wood ~plastic'),
 ('a bell', 'M', 1, 'metal noise music ~holiday shiny'),
 ('money', 'M', 0, 'paper flat green pocket expensive everyday gift'),
 ('a credit card', 'M', 0, 'plastic flat pocket everyday'),
 ('a window', 'M', 4, 'glass flat fragile opens everyday'),
 ('a candle', 'M', 1, 'light hot holiday ~white smell long ~gift ~bathroom ~bedroom ~colorful ~kitchen dangerous ~pretty_x'),
 ('ice', 'M', 1, 'cold watery water ~white fragile ~kitchen shiny'),
 ('snow', 'M', 0, 'cold watery white weather soft cold_place sky_x holiday'),
 ('salt', 'M', 0, 'eat white kitchen everyday ~ocean'),
 ('a magnet', 'M', 1, 'metal ~toy'),
 ('a sword', 'M', 3, 'weapon metal sharp shiny dangerous long handle old'),
 ('a robot', 'M', 3, 'electric metal moves ~toy face buttons ~pretend'),
 ('a washing machine', 'M', 3, 'appliance electric clean heavy opens buttons water noise'),
 ('a vacuum cleaner', 'M', 2, 'appliance electric clean noise handle wheels long rolls ~garage ~bedroom everyday ~heavy box expensive_x ~plastic'),
 ('a fan', 'M', 2, 'electric cold noise ~buttons bedroom'),
 ('a hair dryer', 'M', 1, 'electric hot noise bathroom handle'),
 ('a toothbrush', 'M', 1, 'plastic clean bathroom long handle everyday ~colorful'),
 ('a comb', 'M', 1, 'plastic bathroom pocket flat everyday'),
 ('soap', 'M', 1, 'clean bathroom smell everyday ~white'),
 ('a garbage can', 'M', 3, 'container plastic ~metal kitchen opens smell everyday tasks ~hasliquid ~rolls washable ~wheels alsoout ~noise ~writing ~box'),
 ('a traffic light', 'M', 4, 'electric light red green yellow metal'),
 ('a bed', 'M', 4, 'furniture soft bedroom heavy everyday ~wood four_legs'),
 ('a couch', 'M', 4, 'furniture soft cloth heavy everyday'),
 ('a pillow', 'M', 2, 'soft cloth bedroom everyday ~white'),
 ('a bicycle helmet_x', 'X', 0, ''),
 # ---------- other (nature, places, people, ideas)
 ('the sun', 'O', 6, 'sky space hot light round yellow old natural_x'),
 ('the moon', 'O', 6, 'sky space night round white light_x old'),
 ('a star', 'O', 6, 'sky space night light hot old'),
 ('a cloud', 'O', 5, 'sky weather white soft watery ~flies'),
 ('rain', 'O', 0, 'weather watery liquid sky cold_x'),
 ('lightning', 'O', 5, 'weather sky light hot dangerous noise fast'),
 ('a rainbow', 'O', 6, 'weather sky colorful light'),
 ('wind', 'O', 6, 'weather noise cold fast'),
 ('fire', 'O', 2, 'hot light dangerous smell noise red orange yellow'),
 ('water', 'O', 0, 'liquid drink watery everyday clean ocean_x'),
 ('the ocean', 'O', 6, 'watery water liquid place blue_x old ocean'),
 ('a river', 'O', 6, 'watery water liquid place long old'),
 ('a mountain', 'O', 6, 'place cold_place old heavy'),
 ('a volcano', 'O', 6, 'place hot dangerous light old'),
 ('an island', 'O', 6, 'place water ocean hot_place'),
 ('the earth', 'O', 6, 'space place round old'),
 ('smoke', 'O', 2, 'sky smell hot black ~white dangerous flies'),
 ('a shadow', 'O', 3, 'black flat moves'),
 ('a dream', 'O', 'x', 'abstract night bedroom pretend'),
 ('music', 'O', 'x', 'noise music abstract everyday'),
 ('love', 'O', 'x', 'abstract gift_x holiday'),
 ('time', 'O', 'x', 'abstract old everyday'),
 ('a person', 'O', 3, 'person mammal alive two_legs face teeth moves talk'),
 ('a baby', 'O', 2, 'person mammal alive face cute noise moves soft'),
 ('a teacher', 'O', 3, 'person job office alive face teeth moves talk read write'),
 ('a police officer', 'O', 3, 'person job alive face moves talk ~weapon ~dangerous ~vehicle_x car_x'),
 ('a doctor', 'O', 3, 'person job alive face moves talk white ~expensive'),
 ('a firefighter', 'O', 3, 'person job alive face moves hot ~dangerous red_x'),
 ('Santa Claus', 'O', 3, 'person pretend holiday gift face old red white flies_x'),
 ('a ghost', 'O', 3, 'pretend white night flies dangerous_x holiday'),
 ('a dragon', 'O', 5, 'pretend flies wings tail teeth dangerous hot scales eggs ~green ~red four_legs'),
 ('a unicorn', 'O', 4, 'pretend horns four_legs tail fur white cute colorful'),
 ('a school', 'O', 5, 'place building office old'),
 ('a hospital', 'O', 5, 'place building white'),
 ('a castle', 'O', 6, 'place building old expensive'),
 ('a park', 'O', 6, 'place green'),
 ('a house', 'O', 5, 'place building everyday expensive opens_x'),
 ('a birthday party', 'O', 'x', 'holiday gift abstract'),
 ('the internet', 'O', 'x', 'internet abstract everyday talk'),
 ('a song', 'O', 'x', 'music noise abstract'),
 ('a game', 'O', 'x', 'toy abstract'),
 ('a number', 'O', 'x', 'abstract office write_x'),
]
OBJ = [o for o in OBJ if o[1] != 'X']
from more import MORE
from more2 import MORE2
from more4 import MORE4
MORE2 = MORE2 + MORE4
from more3 import Q4, extra_answers
from fixes import fixes_for, FIX
import json as _json, os as _os
_lp = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'learned.json')
LEARNED = _json.load(open(_lp)) if _os.path.exists(_lp) else {}
Q = Q + [(k, t) for k, t, _ in Q4]
MORE = MORE + MORE2
_NEWNAMES = set(m[0] for m in MORE)
_have = set(o[0] for o in OBJ)
OBJ += [m for m in MORE if m[0] not in _have]
# Taken out again: family members and vague relations. "A person", "a baby" and "a child" cover them; nobody could tell a brother from a neighbor in 20 questions.
DROP = ('a toothpaste', 'a mom', 'a dad', 'a grandma', 'a grandpa', 'a brother', 'a sister', 'a neighbor', 'a stranger', 'a friend', 'a bride', 'a boss', 'a babysitter')
# Careers and job positions are out too (a teacher, a doctor, a plumber, a clown, a cowboy...). Storybook characters stay: a king, a pirate, a witch.
DROP += ('a teacher', 'a police officer', 'a doctor', 'a firefighter', 'a chef', 'a nurse', 'a farmer', 'a soldier', 'an astronaut', 'a mailman', 'a pilot', 'a dentist', 'a lawyer', 'a judge', 'a magician', 'a singer', 'an actor', 'a hockey player', 'a referee', 'a coach', 'a waiter', 'a cashier', 'a plumber', 'a mechanic', 'a carpenter', 'a janitor', 'a librarian', 'a scientist', 'an artist', 'a bus driver', 'a lifeguard', 'a president', 'a clown', 'a cowboy', 'a ninja', 'a knight')
# And the ideas nobody can answer questions about (he missed these more than anything else).
DROP += ('a hole', 'an idea', 'pain', 'night', 'air', 'sadness', 'a name', 'a memory', 'anger', 'luck', 'winter', 'summer', 'gravity', 'a color', 'a wish', 'a holiday', 'fear', 'an echo', 'a lie', 'a massage')
OBJ = [o for o in OBJ if o[0] not in DROP]
# More answers for things that were thinly filled in and often missed (found with art/worst.py). Same tag format; added to the thing's own tags.
PLUS = {
 'a brick': 'red $hard $heavy $outdoors old tasks ~rock set ~paint', 'a charger': 'electric plugin long pocket everyday $home $bring withpc ~travel plastic ~black ~white bedroom',
 'a bandage': 'pocket bathroom hospital sticky fix flat soft $home box wear ~brown', 'a leash': 'long handle $outdoors $bring ~cloth ~metal $home ~everyday',
 'a fish tank': 'glass container water hasliquid $indoors $home wet fragile $heavy ~electric ~light $household', 'a field': 'green flat farm $outdoors ~sport ~flower $huge',
 'steam': 'hot watery wet white ~kitchen ~bathroom ~dangerous', 'a purse': 'container opens handle wear $bring public ~cloth ~expensive money ~gift everyday ~strings',
 'a peeler': 'sharp handle kitchen tool metal', 'a skeleton': 'white $hard scary holiday science ~pretend face teeth two_legs old',
 'concrete': '$hard $heavy $outdoors flat ~rock', 'a fossil': 'old rock $hard underground science ~expensive $outdoors',
 'a projector': 'electric light plugin office school ~expensive $indoors', 'a staircase': '$indoors $home $huge long ~wood $household everyday',
 'a saddle': 'farm brown ~sport $heavy', 'a lock': 'metal $hard pocket opens tasks $home school ~everyday', 'a paintbrush': 'long handle tool write ~wood',
 'a wheelbarrow': 'wheels handle container carry tool $outdoors garage metal', 'a tire': 'round black rolls garage $outdoors $heavy smell',
 'a flag': 'cloth colorful $outdoors hang holiday ~school flat', 'a fence': 'long $outdoors $huge ~wood ~metal paint farm',
 'a lunchbox': 'container opens handle school $bring kitchen ~plastic ~metal everyday', 'a piggy bank': 'container money toy ~fragile bedroom gift cute',
 'a paint roller': 'long handle tool rolls ~wet garage', 'a can': 'metal container round kitchen hasliquid opens', 'a bowl': 'round container kitchen eatwith ~fragile',
 'a wedding': 'event holiday enjoy good ~white ~music ~expensive gift ~ontv', 'a sneeze': 'loud ~wet', 'a yawn': '~night good', 'a hiccup': 'funny',
 'a number': 'write read writing school science money info kinds', 'a word': 'say write read writing school info kinds',
 'a story': 'say read enjoy pretend ontv writing ~school kinds old', 'time': 'old science ~money say everyday',
 'a salad': 'green veg kitchen eat cold salad leaves', 'a toy train': 'toy wheels plastic ~electric played set box', 'a snowman': 'cold white watery holiday winter round face $outdoors $made',
 'a genie': 'pretend magic_x famous male ~scary old container_x', 'a plant': 'green alive leaves ~flower $indoors ~$outdoors grows $home', 'a bush': 'green alive leaves $outdoors grows ~flower ~thorns',
 'a tank top': 'wear cloth clothes ~sport everyday ~bedroom', 'thread': 'long pocket fix cloth strings ~colorful', 'wrapping paper': 'paper gift holiday colorful ~flat',
 'a whiteboard': 'white flat write writing office school hang $hard $indoors', 'a diaper': 'wear baby smell white lower soft',
}
# Nov 13: things you wear on your head that were never marked so ("Is it on your head?" said no for a hat)
for _n in ('a hat', 'a baseball cap', 'a helmet', 'glasses', 'sunglasses', 'headphones', 'earrings', 'a crown', 'a wig', 'earbuds'):
    PLUS[_n] = (PLUS.get(_n, '') + ' onhead').strip()
# a speaker covers Bluetooth speakers too: you can take it with you, and it can wake the neighbours
PLUS['a speaker'] = (PLUS.get('a speaker', '') + ' ~battery ~plugin ~$bring ~internet ~withpc ~light gift ~expensive ~everyday alsoout plastic black buttons').strip()
PLUS['a CD'] = (PLUS.get('a CD', '') + ' box ~$bring').strip()   # (music only: DVDs and Blu-rays, with pictures, are their own thing)
OBJ = [(n, c, sz_, (tg + ' ' + PLUS[n]) if n in PLUS else tg) for n, c, sz_, tg in OBJ]

# ---------------------------------------------------------------------------------------------------------------------
# Zandor guesses something you are LOOKING AT. So everything you can't lay eyes on is out (ideas, feelings, events, make-believe
# creatures, your insides, outer space), and so are look-alikes nobody could tell apart by eye in 21 questions: it is "a bird"
# unless the bird is unmistakable (a penguin, an owl, a flamingo), "a fish" unless it is a shark, "a snake", "a tree", and so on.
def _bare(n):
    n = n.lower()
    for p in ('a ', 'an ', 'the '):
        if n.startswith(p): return n[len(p):]
    return n
_OUT = set(w.strip() for w in """
 store,
 santa claus, king, queen, pirate, vampire, zombie, witch, wizard, princess, prince, thief, superhero,
 ghost, dragon, unicorn, t-rex, mammoth, mermaid, fairy, alien, monster, bigfoot, easter bunny, mummy, werewolf, tooth fairy, genie, magic wand, giant, troll,
 elf, leprechaun, goblin, angel, devil, cyclops, phoenix, centaur, loch ness monster, dinosaur,
 volcano, island, earth, hospital, castle, lighthouse, farm, zoo, desert, cave, city, library, movie theater, airport, mall, glacier, iceberg, canyon, cliff, swamp,
 jungle, cemetery, north pole, museum, bank, grocery store, bakery, hotel, jail, fire station, stadium, hockey rink, gym, bowling alley, casino, circus,
 amusement park, factory, basement, attic, kitchen, bathroom, bedroom, apartment, igloo, pyramid, windmill, train station,
 heart, brain, blood, bones, chest, wrist, ankle, heel, cheek, chin, forehead, freckle, lung, kidney, liver, muscle, vein, skull, rib, spine,
 pigeon, crow, hummingbird, rooster, seagull, woodpecker, bluejay, vulture, bald eagle, toucan, canary, parakeet, hawk, pelican, robin, sparrow, cardinal, dove,
 falcon, raven, loon, canada goose, stork, heron, puffin, emu, chick, duckling,
 salmon, clownfish, catfish, trout, piranha, koi, tuna, eel, swordfish, pufferfish, angelfish, minnow, bass, cod,
 firefly, cricket, flea, bedbug, termite, hornet, bumblebee, praying mantis, maggot, millipede,
 leopard, jaguar, cougar, hyena, badger, mole, puppy, kitten, lamb, bull, sea lion, manatee, squid, shrimp, oyster, tadpole, salamander, iguana, gecko, cobra,
 rattlesnake, python, tick, centipede, slug, pony, hermit crab, tarantula, chimpanzee, orangutan, meerkat, armadillo, anteater, platypus, opossum, coyote,
 antelope, wild boar, weasel, orca, narwhal, gerbil, chinchilla, calf, piglet, foal, clam, mussel, sea urchin, sea turtle, coral, leech, toad, tortoise,
 komodo dragon, anaconda, garter snake, black widow, daddy longlegs, crocodile, chameleon, scorpion, reindeer,
 cotton, bamboo, ivy, daisy, fern, vine, lily, orchid, daffodil, lavender, poppy, clover, weed, maple tree, oak tree, birch tree, willow tree, venus flytrap,
 lily pad, poison ivy, mistletoe, holly, hay,
 rocket, wind, spaceship, satellite, planet, comet, meteor, tornado, thunder, hail, hurricane, flood, earthquake, northern lights, outer space, black hole,
 galaxy, mars, jet, blimp,
 submarine, minivan, jeep, limousine, race car, convertible, sports car, tank, snowplow, tow truck, dump truck, excavator, streetcar, ferry, speedboat, rowboat, yacht,
 sword, crown, crystal ball, skeleton, coffin, tombstone, germ, tear, steam, dust, leather, wool, cocoon, pearl, ruby, emerald, crystal, silver, copper, iron,
 steel, fossil, coal, oil, gasoline, clay, concrete, tumbleweed, root, jukebox, pinball machine, slot machine, disco ball, metal detector, jackhammer, siren,
 engine, gong, bagpipes, accordion, tuba, trombone, saxophone, cello, banjo, harp, clarinet, cymbal, maracas, tambourine, kazoo, electric guitar,
 bow and arrow, boomerang, pogo stick, punching bag, horseshoe, saddle, anchor, mousetrap, crutch, microscope, cape, costume, overalls, poker chip,
 lottery ticket, sparkler, easter egg, stocking, confetti, gingerbread man, whiskey, champagne, apple pie, honeydew melon, nectarine, tangerine, pomegranate,
 papaya, apricot, fig, date, leek, turnip, rhubarb, hazelnut, chestnut, pecan
""".replace('\n', ' ').split(',') if w.strip())
_seen = set(); _keep = []
for _o in OBJ:
    if _o[2] == 'x' or (_bare(_o[0]) in _OUT and _o[0] != 'an iron') or _o[0] in _seen: continue   # (ideas have no size; the list above, but the metal iron, not the clothes iron; and no doubles)
    _seen.add(_o[0]); _keep.append(_o)
_gone = _OUT - set(_bare(o[0]) for o in OBJ)
OBJ = _keep

# Questions that no longer tell anything apart (they were about people, ideas and make-believe), or were too vague to answer the same way twice.
LEAVE4 = set("""a phone|a wallet|a key|a keychain|a purse|a backpack|a credit card|a twenty dollar bill|a coin|an ID card|a phone case|a water bottle|a lunchbox|a vape|a cigarette|a lighter|an inhaler|a tube of lip balm|a pacifier|a sippy cup|a baby bottle|a diaper|headphones|earbuds|sunglasses|glasses|a watch|a smartwatch|a hearing aid|braces|a contact lens|a lanyard|a mask|a hair tie|a bobby pin|a ring|a necklace|earrings|a bracelet""".split('|'))
LEAVE2 = set("""a book|a laptop|a tablet|a charger|a camera|a pen|a pencil|a notebook|a magazine|a newspaper|a shopping bag|a suitcase|a briefcase|a thermos|a juice box|a comb|a hairbrush|a bottle of sunscreen|hand sanitizer|a piece of gum|an umbrella|a leash|a stroller|a car seat|a cooler|a pill bottle|a USB stick|a map|a letter|an envelope|a passport|a ticket|a tissue|a bandage|a granola bar|a bag of trail mix|a skateboard|a frisbee|a ball|a fishing rod|a kite|a toy car|an action figure|a doll|a teddy bear|a stuffed animal|a tube of lipstick|a makeup kit|a pocket knife|a flashlight|a helmet|swim goggles|a swimsuit|a stress ball|a fidget spinner|a stylus|a bookmark|a GPS|binoculars|a name tag|a toque|a scarf|mittens|gloves|a raincoat|a jacket|a hoodie|a sweater|a coat|boots|a bib|a rattle|a party hat|a shopping cart_x""".split('|'))
LEAVE0 = set("""a dartboard|a trophy|a bowling pin|a dumbbell|a punching bag|a pool table|a treadmill|a hockey net|a basketball hoop""".split('|'))
LEAVE1 = set("""a diamond|skis|a stethoscope|a thimble|earplugs|a snorkel|a medal|a bowling ball|a net|a hockey puck|a dart|a crutch|pajamas|a robe|slippers|an oven mitt|a shower cap|an apron|a costume|a life jacket|roller skates|ice skates|a boxing glove|safety goggles|a mouthguard|a VR headset|a bra_x|a crown|a wig|a cape""".split('|'))
STAPLES = set("""salt|pepper|sugar|flour|butter|milk|an egg|bread|ketchup|mustard|mayonnaise|rice|noodles|spaghetti|cereal|coffee|tea|olive oil|oil|peanut butter|cheese|water|jam|vinegar|honey|soy sauce|maple syrup|cinnamon""".split('|'))
QDROP = set("""paint job pretend abstract space royal uniform female male family bodydoes event say famous ontv science songs insidebody room good enjoy $joy kinds
 tasks $invented $buy africa jungle larger old addictive funny office $huge person
 $home $bring public""".split())   # (Nov 13: 'in your home?' depends on whose home; 'carry it around?' was vague - see $leave; 'in front of strangers?' mixes would and could)
# The wording Zandor uses. Same meaning as the plain question it replaces, but his own: stranger, funnier, nothing lifted from the old toy.
QTEXT = {
 '$hold': 'Would it fit in your two hands?',
 '$small': 'Is it smaller than a human head?', '$person': 'Is it bigger than a coffin?', '$car': 'Is it bigger than a hearse?', '$microwave': 'Is it bigger than a case of beer?',
 '$pound': 'Is it heavier than a pound of ground beef?', '$small2': 'Is it bigger than a hamster?', '$heavy': 'Would you need both hands to carry it?',
 'pocket': 'Could you sneak it out in your pocket?', 'envelope': 'Could you mail it in an envelope?', '$made': 'Did people make it, not nature?',
 '$touch': 'Could you poke it with a finger?', 'moves': 'Does it move on its own?', 'eat': 'Do people eat it on purpose?', 'fur': 'Is it furry?',
 'bites': 'Could it bite or sting you?', 'cute': 'Would you call it cute?', 'dangerous': 'Could it send you to the hospital?',
 'smell': 'Could you smell it with your eyes shut?', 'noise': 'Does it make noise?', 'loud': 'Could it wake the neighbours?',
 'fragile': 'Would it shatter if you dropped it?', 'soft': 'Is it soft and squishy?', 'sharp': 'Could it cut you?', 'hot': 'Would it burn your hand?',
 'cold': 'Is it cold to the touch?', 'shiny': 'Is it shiny?', '$steal': 'Would a burglar bother stealing it?', 'expensive': 'Is it worth more than a hundred bucks?',
 'fast': 'Could it outrun you?', 'night': 'Does it come out at night?', 'scary': 'Would it scare a small child?', 'washable': 'Do people ever wash it?',
 'everyday': 'Did you use one today?', 'gift': 'Would it make a decent birthday gift?', '$home': 'Is there one in your home?',
 '$household': 'Does almost every home have one?', 'public': 'Would you use it in front of strangers?', '$bring': 'Do you carry it around with you?',
 'travel': 'Does it help you get somewhere?', 'electric': 'Does it need power to work?', 'light': 'Does it glow or light up?',
 'writing': 'Are there words printed on it?', 'body': 'Is it part of your body?', 'lower': 'Is it below the belt?', 'sweet': 'Would a dentist disapprove of it?',
 'hit': 'Do you whack it?', 'throw': "Is it something you'd throw?", 'rolls': 'Would it roll down a hill?', 'long': 'Is it long and skinny?',
 '$hard': 'Is it hard to the touch?', 'wet': 'Does it often get wet?', 'internet': 'Can it get on the Wi-Fi?', 'hasliquid': 'Is there liquid inside it?',
 'comfort': 'Would you cuddle up with it?', 'sky': 'Do you have to look up to see it?', 'office2': 'Would you find it in an office?', 'wild': 'Does it live in the wild?',
 'alive': 'Is it alive right now?', 'face': 'Does it have a face?', 'pet': 'Do people keep it as a pet?', '$movable': 'Could one person move it?',
 'weapon': 'Was it made to hurt things?', 'grows': 'Does it grow?', 'money': 'Does it have to do with money?', 'played': 'Can it be played?',
}
Q = [(k, QTEXT.get(k, t)) for k, t in Q if k not in QDROP]
Q.append(('$light', 'Is it lighter than a hot dog?'))               # (a second weight question, at the light end)
Q.append(('$leave', 'Do you take it along when you leave home?'))   # (what goes out the door with you: a phone, keys, your coat; not a stapler)

# One of it, not a heap: every thing is a single item (a grape, not grapes; a glass of milk, not milk), so "is it heavier than..." has
# one answer. The name he says is on the right; the plain name on the left is still what the rest of this file calls it.
DISPLAY = {
 'a recorder': 'a recorder (flute)',   # (the school instrument, not a tape recorder)
 'a remote control': 'a TV remote',
 'a crane': 'a crane (machine)',
 'grapes': 'a grape', 'peas': 'a pea', 'french fries': 'a french fry', 'LEGO bricks': 'a LEGO brick', 'green beans': 'a green bean', 'brussels sprouts': 'a brussels sprout',
 'beans': 'a bean', 'noodles': 'a noodle', 'nachos': 'a nacho', 'jelly beans': 'a jelly bean', 'playing cards': 'a playing card', 'dice': 'a pair of dice',
 'dominoes': 'a domino', 'eyelashes': 'an eyelash', 'contact lenses': 'a contact lens', 'fireworks': 'a firework', 'corn': 'a cob of corn', 'celery': 'a stalk of celery',
 'lettuce': 'a head of lettuce', 'cabbage': 'a head of cabbage', 'garlic': 'a clove of garlic', 'toast': 'a slice of toast', 'bread': 'a loaf of bread',
 'bacon': 'a strip of bacon', 'pepperoni': 'a slice of pepperoni', 'gum': 'a stick of gum', 'candy': 'a piece of candy', 'chalk': 'a stick of chalk', 'soap': 'a bar of soap',
 'paper': 'a sheet of paper', 'tape': 'a roll of tape', 'toilet paper': 'a roll of toilet paper', 'money': 'a twenty dollar bill', 'sushi': 'a piece of sushi',
 'ham': 'a slice of ham', 'beef jerky': 'a strip of beef jerky', 'ice': 'an ice cube', 'grass': 'a blade of grass', 'rice': 'a grain of rice', 'popcorn': 'a piece of popcorn',
 'cereal': 'a bowl of cereal', 'spaghetti': 'a plate of spaghetti', 'soup': 'a bowl of soup', 'oatmeal': 'a bowl of oatmeal', 'coffee': 'a cup of coffee', 'tea': 'a cup of tea',
 'hot chocolate': 'a mug of hot chocolate', 'milk': 'a glass of milk', 'orange juice': 'a glass of orange juice', 'lemonade': 'a glass of lemonade',
 'apple juice': 'a glass of apple juice', 'iced tea': 'a glass of iced tea', 'soda': 'a glass of soda', 'beer': 'a bottle of beer', 'wine': 'a bottle of wine',
 'water': 'a glass of water', 'ketchup': 'a bottle of ketchup', 'mustard': 'a bottle of mustard', 'maple syrup': 'a bottle of maple syrup', 'peanut butter': 'a jar of peanut butter',
 'jam': 'a jar of jam', 'honey': 'a jar of honey', 'mayonnaise': 'a jar of mayonnaise', 'salsa': 'a jar of salsa', 'vinegar': 'a bottle of vinegar',
 'olive oil': 'a bottle of olive oil', 'soy sauce': 'a bottle of soy sauce', 'hot sauce': 'a bottle of hot sauce', 'dish soap': 'a bottle of dish soap', 'bleach': 'a jug of bleach',
 'shampoo': 'a bottle of shampoo', 'lotion': 'a bottle of lotion', 'perfume': 'a bottle of perfume', 'sunscreen': 'a bottle of sunscreen', 'mouthwash': 'a bottle of mouthwash',
 'nail polish': 'a bottle of nail polish', 'toothpaste': 'a tube of toothpaste', 'glue': 'a bottle of glue', 'deodorant': 'a stick of deodorant', 'lipstick': 'a tube of lipstick',
 'lip balm': 'a tube of lip balm', 'whipped cream': 'a can of whipped cream', 'sour cream': 'a tub of sour cream', 'yogurt': 'a cup of yogurt', 'butter': 'a stick of butter',
 'ice cream': 'a scoop of ice cream', 'pudding': 'a cup of pudding', 'caramel': 'a piece of caramel', 'tofu': 'a block of tofu', 'asparagus': 'a stalk of asparagus',
 'string': 'a piece of string', 'yarn': 'a ball of yarn', 'thread': 'a spool of thread', 'aluminum foil': 'a roll of aluminum foil', 'plastic wrap': 'a roll of plastic wrap',
 'sandpaper': 'a sheet of sandpaper', 'chocolate': 'a piece of chocolate', 'cheese': 'a block of cheese', 'broccoli': 'a head of broccoli', 'cauliflower': 'a head of cauliflower',
 'wrapping paper': 'a roll of gift wrap', 'laundry detergent': 'a jug of detergent', 'dental floss': 'a pack of dental floss', 'cotton candy': 'a stick of cotton candy',
 'lasagna': 'a slice of lasagna', 'french toast': 'a slice of french toast', 'garlic bread': 'a slice of garlic bread', 'macaroni and cheese': 'a bowl of mac & cheese',
 'poutine': 'a plate of poutine', 'jello': 'a bowl of jello', 'gravy': 'a bowl of gravy', 'trail mix': 'a bag of trail mix', 'kale': 'a leaf of kale', 'spinach': 'a leaf of spinach',
 'basil': 'a basil leaf', 'mint': 'a mint leaf', 'ginger': 'a piece of ginger', 'bark': 'a piece of bark', 'makeup': 'a makeup kit', 'gold': 'a gold bar',
 'salt': 'a pinch of salt', 'sugar': 'a spoonful of sugar', 'flour': 'a bag of flour', 'pepper': 'a pinch of pepper', 'cinnamon': 'a cinnamon stick', 'wheat': 'a stalk of wheat',
 'Christmas lights': 'a string of lights', 'hair': 'a strand of hair', 'skin': 'a patch of skin', 'mud': 'a mud puddle',
}
assert all(len(v) < 24 for v in DISPLAY.values()), [v for v in DISPLAY.values() if len(v) >= 24]
assert all(k in [o[0] for o in OBJ] for k in DISPLAY), [k for k in DISPLAY if k not in [o[0] for o in OBJ]]
# the size of one of them (0 pocket .. 6 huge), where the old size was for a heap
_SIZE1 = {'grapes': 0, 'french fries': 0, 'noodles': 0, 'nachos': 0, 'popcorn': 0, 'ice': 0, 'bacon': 0, 'ham': 0, 'toast': 0, 'chocolate': 0, 'corn': 1, 'celery': 1,
          'gold': 1, 'hair': 0, 'skin': 0, 'bark': 0, 'kale': 0, 'spinach': 0, 'wheat': 1, 'fireworks': 1, 'salt': 0, 'sugar': 0, 'pepper': 0, 'flour': 1, 'paper': 0,
          'money': 0, 'lasagna': 1, 'cheese': 1, 'mud': 2}
OBJ = [(n, c, _SIZE1.get(n, s_), tg) for n, c, s_, tg in OBJ]
# Stuff with no "one" of it: how much there is changes the answer, so every size and weight question answers "sometimes".
MASS = ('sand', 'snow', 'dirt', 'moss', 'seaweed', 'rain', 'fog', 'smoke', 'fire', 'lightning')
assert all(len(t) < 44 for k, t in Q), [t for k, t in Q if len(t) >= 44]

EXTRA = {
 'songs': 'a spider;a star;the sun;rain;the moon;a sheep;a duck;a cow;a pig;a horse;a chicken;a mouse;a teddy bear;a bell;Santa Claus;a rainbow;a train;a bus;a boat;love;money;~a dog;~a cat;~a bee;~a butterfly;~a frog;~a monkey;~an elephant;~a fish;~the ocean;~a river;~a flower;~a rose;~a tree;~snow;~wind;~a baby;~a birthday party;~a cake;~a car;~a guitar;~a piano;~a drum;~time;~a dream;~a ghost;~a dragon;~a unicorn;~a crocodile;~a turkey;~a kite;~a balloon;~a phone;~a house;~a castle;~a mountain',
 'washable': 'a dog;a T-shirt;a towel;socks;a hat;a plate;a mug;a glass;a fork;a spoon;a knife;a frying pan;a pot;a car;a bicycle;an apple;grapes;a strawberry;a carrot;a potato;lettuce;a tomato;a cucumber;broccoli;a cherry;a peach;a pear;a blueberry;peas;a baby;a person;a bottle;a toothbrush;a comb;a pillow;a backpack;a shoe;a bathtub;a sink;a toilet;a window;a mirror;a bucket;a ball;LEGO bricks;a doll;~a teddy bear;~a cat;~a horse;~a pig;~a couch;~a bed;~a rabbit;~a hamster;~a table;~a chair;~a door;~a floor_x;~rice;~a mushroom;~an umbrella;~glasses;~a garbage can',
 'tasks': 'a knife;scissors;a hammer;a screwdriver;a saw;a shovel;a ladder;a computer;a laptop;a phone;a calculator;a pen;a pencil;a stapler;a paper clip;a ruler;a washing machine;a vacuum cleaner;a microwave;a toaster;a stove;a refrigerator;a car;a truck;a bus;a broom_x;a bucket;a hair dryer;a toothbrush;a comb;a frying pan;a pot;a fork;a spoon;a clock;a watch;a robot;a teacher;a doctor;a police officer;a firefighter;~a horse;~a dog;~a camera;~a light bulb;~a lamp;~a backpack;~a magnet;~a nail;~a key;~soap;~a towel;~a remote control;~a bicycle;~a person;~the internet;~glasses;~a battery',
 'enjoy': 'a dog;a cat;a rabbit;a hamster;a goldfish;a parrot;chocolate;a cake;a cookie;a pizza;popcorn;french fries;an apple;a banana;a strawberry;grapes;a watermelon;a cherry;a peach;a pineapple;a blueberry;peanut butter;a sandwich;cereal;spaghetti;maple syrup;coffee;tea;music;a song;a game;a video game console;a TV;a book;a ball;a kite;a balloon;LEGO bricks;a teddy bear;a doll;a guitar;a piano;a drum;a trumpet;a skateboard;a bicycle;a birthday party;love;a rainbow;the sun;a flower;a rose;a park;an island;the ocean;the internet;a dream;a phone;a couch;a bed;a pillow;Santa Claus;a unicorn;a dolphin;a butterfly;~a horse;~a camera;~a car;~a boat;~a laptop;~a computer;~snow;~rain;~a star;~a mountain;~a castle;~a person;~a baby;~a candle;~money;~a crayon;~a hat',
 'travel': 'a car;a bus;a train;an airplane;a boat;a helicopter;a motorcycle;a truck;a bicycle;a rocket;a backpack;a camel;a horse;~money;~a credit card;~a phone;~glasses;~a camera;~a skateboard;~an umbrella;~a hat;~a key;~a shoe;~a pillow;~a watch;~an elephant;~a battery;~headphones;~a book;~a laptop;~the internet;~a river;~the ocean;~an island',
 'hasliquid': 'a coconut;an orange;a watermelon;a lemon;a bottle;a mug;a glass;a pen;a battery;a cloud;the ocean;a river;a bathtub;a sink;a toilet;a pot;a refrigerator;a washing machine;a car;a truck;a bus;a motorcycle;an airplane;a candle_x;~a cucumber;~grapes;~a tomato;~a peach;~a pear;~a pineapple;~a strawberry;~a cherry;~an apple;~a bucket;~a person;~a baby;~a dog;~a cat;~a jellyfish;~an octopus;~a volcano;~soap;~a rocket;~a boat;~a helicopter;~a train;~ice;~snow;~a light bulb_x',
 'desk': 'a pen;a pencil;paper;a stapler;a paper clip;a ruler;a computer;a laptop;a calculator;a book;a lamp;a crayon;~a phone;~a mug;~a clock;~a glass;~a newspaper;~scissors;~a remote control;~glasses;~headphones;~a cardboard box;~a battery;~a magnet;~money;~a coin;~a key;~a plate;~a cookie;~a sandwich;~a watch;~a camera;~a candle;~a light bulb;~a flower;~a cactus;~a goldfish;~LEGO bricks;~a robot;~a bell',
 'info': 'a book;a computer;a laptop;a phone;a newspaper;a camera;the internet;a calculator;~paper;~a video game console;~a credit card;~a TV;~a radio;~a watch;~a clock;~money;~a person;~a teacher;~a robot;~a number;~a song;~a dream;~an elephant;~a remote control',
 'paint': 'a door;a chair;a table;a house;a car;a bicycle;a boat;a fence_x;a wall_x;a window;paper;a cardboard box;a log;a rock;a piano;a guitar;a skateboard;a garbage can;a bucket;a mailbox_x;a traffic light;a robot;a school;a hospital;a castle;a shoe;a plate;a mug;a pumpkin;a T-shirt;a ruler;a pencil;a crayon;a truck;a bus;a train;an airplane;a helicopter;a rocket;a motorcycle;a bed;a couch;a drum;a doll;a ball;a kite;a refrigerator;a toilet;a bathtub;a ladder;a shovel;a hammer;a sword;a bell;a candle;~a coin;~a toaster;~a computer;~a phone;~a lamp;~a stove;~a sink;~a mirror;~a glass;~a bottle;~a cookie;~a cake;~a person;~a baby;~a teddy bear;~LEGO bricks;~a hat;~a backpack',
 'leaves': 'a tree;a flower;a rose;a sunflower;lettuce;~broccoli;~a carrot;~a pineapple;~a strawberry;~an apple;~a cherry;~a tomato;~a pumpkin;~a cucumber;~peas;~corn;~tea;~seaweed;~grass;~a leaf;~a potato;~an onion;~a peanut;~cotton',
 'kinds': 'a dog;a cat;a horse;a cow;a chicken;a fish;a goldfish;a bird;a snake;a lizard;a spider;a bee;an ant;a butterfly;a shark;a whale;a monkey;a bear;a frog;a turtle;an apple;a banana;an orange;grapes;a tomato;a potato;a pepper_x;a mushroom;bread;a cookie;a cake;a pizza;a sandwich;cereal;tea;coffee;chocolate;a flower;a rose;a tree;a cactus;a book;a chair;a table;a car;a truck;a boat;a bicycle;a shoe;a hat;a ball;a game;a song;music;a rock;a phone;a computer;a TV;a clock;a lamp;a dinosaur;a dragon;a candle;a knife;a bell;a drum;a guitar;a bottle;a plate;a cup_x;a mug;a glass;a ring;a necklace;a house;a school;a building_x;a doctor;a teacher;~a salmon;~a deer;~a duck;~an owl;~a parrot;~a pig;~a sheep;~a goat;~a rabbit;~a mouse;~a rat;~a crab;~an octopus;~a star;~a cloud;~rain;~a river;~a mountain;~an island;~a hammer;~a saw;~a pen;~a pencil;~paper;~money;~a coin;~a key;~a toy_x;~a doll;~a robot;~a person;~a ghost',
 'rabbits': 'a carrot;lettuce;grass;broccoli;~an apple;~a flower;~a leaf;~peas;~a banana;~a strawberry;~a cucumber;~a tomato;~corn;~a pear;~a blueberry;~a sunflower;~a rose;~seaweed;~bread;~cereal;~rice;~a peanut;~a pumpkin;~a potato',
 'smooth': 'a glass;a mirror;a plate;a phone;a window;ice;a credit card;a light bulb;an apple;a cherry;a tomato;a cucumber;grapes;a blueberry;a bottle;a mug;a spoon;a fork;a knife;a sword;a diamond;a coin;a ring;gold;a necklace;a balloon;a dolphin;a whale;a seal;a shark;a laptop;a computer;a TV;a refrigerator;a toilet;a bathtub;a sink;a car;a frying pan;a bell;a trumpet;a piano;a ruler;a credit card;a battery;chocolate;a key;~a rock;~sand;~paper;~a table;~a door;~a ball;~a banana;~an orange;~a lemon;~a peach;~a pear;~an avocado;~a snake;~a frog;~a goldfish;~a salmon;~a hippo;~an egg_x;~a pencil;~a pen;~a crayon;~a skateboard;~a candle;~soap;~water;~the ocean',
 'larger': 'an apple;a banana;an orange;a lemon;grapes;a strawberry;a cherry;a peach;a pear;a coconut;a blueberry;an avocado;a tomato;a leaf;a pine cone;a log;corn;peas;a peanut;rice;cotton;maple syrup;a pickle;a cucumber;a pumpkin;a watermelon;a pineapple;a mushroom;paper;~a carrot;~a potato;~an onion;~a feather_x;~salt;~sand;~a rock;~gold;~a diamond;~ice;~snow;~rain;~a cloud;~smoke;~a shadow;~a baby;~bread;~french fries;~popcorn;~a cookie;~a river;~an island;~a coin;~a nail;~a book;~a newspaper;~a T-shirt;~a towel;~water;~a star;~the moon;~a battery;~a key',
 'rolls': 'a ball;a coin;an orange;an apple;a watermelon;a pumpkin;a coconut;grapes;a cherry;a blueberry;peas;a log;a bicycle;a car;a skateboard;a truck;a bus;a train;a battery;a pencil;a crayon;a bottle;a drum;the earth;~a rock;~a ring;~a tomato;~a potato;~an onion;~a peach;~a lemon;~a cookie;~a pizza;~a pen;~a mug;~a glass;~a light bulb;~a plate;~a vacuum cleaner;~a chair;~a hamster;~a hedgehog;~a dog;~a pig;~a horse;~a balloon;~a candle;~a cake;~corn;~a cucumber;~a carrot;~a snowball_x;~snow',
 'wet': 'a duck;a goose_x;a fish;a goldfish;a salmon;a clownfish;a shark;a whale;a dolphin;a seal;a penguin;an otter;a beaver;a frog;a turtle;a crocodile;a hippo;a swan;an octopus;a jellyfish;a crab;a lobster;a starfish;seaweed;a boat;an umbrella;a towel;soap;a toothbrush;a sink;a bathtub;a toilet;a plate;a mug;a glass;a spoon;a fork;a pot;ice;snow;rain;water;the ocean;a river;a cloud;sand;a rock;a car;a bucket;a sponge_x;a washing machine;~a dog;~a cat;~a person;~a baby;~a shoe;~socks;~a T-shirt;~grass;~a leaf;~a flower;~a tree;~a log;~a window;~a door;~a house;~a bicycle;~a bus;~a truck;~a ball;~a kite;~a mushroom;~a lettuce_x;~lettuce;~an apple;~grapes;~a tomato;~a cucumber;~a carrot;~a potato;~a fly;~a mosquito;~a snail;~a worm;~a snake',
 'sliced': 'bread;a cake;a pizza;a pumpkin;a turkey;a watermelon;a tomato;a cucumber;an onion;a log;a pineapple;an avocado;a lemon;~an apple;~an orange;~a potato;~a carrot;~a banana;~a peach;~a pear;~a mushroom;~a sandwich;~a pickle;~a salmon;~a coconut;~lettuce;~a pig;~a cow;~a chicken;~a rock;~a cookie;~chocolate;~a candle;~soap;~ice;~cheese_x',
 'forest': 'a deer;a bear;a wolf;a fox;an owl;a squirrel;a raccoon;a moose;a skunk;a hedgehog;a porcupine_x;a tree;a mushroom;a pine cone;a leaf;a log;a spider;an ant;a worm;a snail;a butterfly;a bee;a mosquito;a frog;a snake;a crow;a beaver;~a rabbit;~a mouse;~a rat;~a bat;~a lizard;~a ladybug;~a fly;~a grasshopper;~a cockroach;~a flower;~grass;~a gorilla;~a monkey;~a sloth;~a tiger;~a panda;~a koala;~an eagle;~a pigeon;~a turtle;~a ghost;~a unicorn;~a dragon;~a castle;~a park;~a river;~a mountain',
 'claws': 'a dog;a cat;a bear;a polar bear;a panda;a lion;a tiger;a cheetah;a wolf;a fox;a raccoon;a skunk;a squirrel;a mouse;a rat;a rabbit;a koala;a kangaroo;a sloth;an eagle;an owl;a parrot;a chicken;a turkey;a crab;a lobster;a scorpion;a lizard;a crocodile;a chameleon;a dragon;a hedgehog;a beaver;an otter;a dinosaur;an ostrich;a pigeon;a crow;a duck;a penguin;a seal;~a hamster;~a turtle;~a bat;~a monkey;~a gorilla;~a hummingbird;~a flamingo;~a swan;~a peacock;~a goose_x;~a unicorn;~a frog;~a spider;~a grasshopper;~a ladybug;~a beetle_x',
 'public': 'a car;a bus;a train;an airplane;a bicycle;a motorcycle;a phone;money;a credit card;a coin;a T-shirt;a shoe;socks;a hat;glasses;an umbrella;a backpack;a watch;headphones;a ball;a skateboard;a camera;a key;a pen;a traffic light;a ring;a necklace;a helicopter;a boat;a truck;a bench_x;~a book;~a newspaper;~a laptop;~a bottle;~a kite;~a balloon;~a sandwich;~a cookie;~french fries;~coffee;~a pizza;~a dog;~a horse;~a guitar;~a drum;~a trumpet;~a sword;~the internet;~a toilet;~a sink;~a candle;~a bell;~a towel;~a comb;~a toothbrush;~a computer;~a calculator;~a doll;~a teddy bear;~water',
 'withpc': 'the internet;headphones;a computer_x;~a mouse;~a phone;~paper;~a camera;~a video game console;~a lamp;~a chair;~a desk_x;~a battery;~a TV;~a laptop;~a calculator;~a game;~a song;~music;~a mug;~glasses;~a radio',
 'addictive': 'coffee;chocolate;a video game console;a phone;the internet;~a game;~tea;~popcorn;~french fries;~a TV;~a cookie;~a cake;~a pizza;~peanut butter;~cereal;~maple syrup;~a laptop;~a computer;~love;~music;~a song;~money;~salt;~LEGO bricks',
 'box': 'cereal;LEGO bricks;a phone;a laptop;a computer;a TV;a camera;a video game console;headphones;a toaster;a microwave;a fan;a hair dryer;a pizza;a cookie;a shoe;a crayon;a paper clip;a battery;a light bulb;a calculator;a remote control;a doll;a teddy bear;a watch;a ring;a necklace;a radio;a stapler;a vacuum cleaner;a washing machine;a refrigerator;a stove;popcorn;tea;a cake;a game;a robot;~chocolate;~a pen;~a pencil;~a ball;~socks;~a hat;~glasses;~a mug;~a glass;~a plate;~a fork;~a spoon;~a knife;~scissors;~a candle;~soap;~a toothbrush;~a comb;~a lamp;~a clock;~a kite;~a balloon;~a book;~a guitar;~a drum;~a trumpet;~a skateboard;~a bicycle;~a hammer;~a screwdriver;~a nail;~a saw;~a magnet;~a pot;~a frying pan;~a bottle;~rice;~spaghetti;~salt;~french fries;~a sandwich;~a diamond;~gold;~a credit card;~money;~a towel;~a pillow;~a T-shirt;~a backpack;~a cactus;~a goldfish_x;~a hamster;~a strawberry;~blueberry_x;~a blueberry;~grapes;~a cherry',
 'played': 'a game;a ball;a video game console;a song;music;a guitar;a piano;a drum;a trumpet;a radio;~a bell;~a kite;~LEGO bricks;~a doll;~a teddy bear;~a balloon;~a skateboard;~a phone;~a computer;~a laptop;~a TV;~a robot;~a dog;~a cat;~a ruler_x;~a bicycle;~a toy_x;~headphones;~a crayon;~a dream;~snow',
 'comfort': 'a pillow;a bed;a couch;a teddy bear;a towel;tea;love;socks;a house;a candle;~a dog;~a cat;~a rabbit;~a hamster;~chocolate;~a cookie;~a cake;~coffee;~music;~a song;~a mug;~a baby;~a person;~a doll;~the sun;~fire;~a T-shirt;~a hat;~rain;~a dream;~bread;~spaghetti;~a pizza;~peanut butter;~a book;~a TV;~a bathtub;~soap;~a cloud;~snow;~a park;~an island;~the ocean;~Santa Claus;~a birthday party;~a doctor',
 'set': 'LEGO bricks;a fork;a spoon;a knife;a plate;a crayon;a drum;socks;~a mug;~a glass;~a pencil;~a pen;~a chair;~a table;~a bed_x;~a screwdriver;~a hammer;~a saw;~a pot;~a frying pan;~a ring;~a necklace;~a doll;~a ball;~a book;~a number;~a game;~a shoe;~a towel;~a pillow;~a bottle;~a light bulb;~a battery;~a paper clip;~a key;~a coin;~a candle;~a bell;~a toy car_x;~a robot;~headphones;~a video game console',
 'payuse': 'a bus;a train;an airplane;the internet;a hospital;a doctor;a helicopter;~a phone;~a video game console;~a park;~a boat;~a washing machine;~a toilet;~a game;~a school;~music;~a TV;~a castle;~an island;~a rocket;~a car;~a motorcycle;~a taxi_x;~a computer;~a laptop;~a teacher;~a camel;~a horse;~an elephant;~a zoo_x;~a house;~a bathtub;~a song;~a bicycle;~a skateboard;~a radio;~a camera;~a microwave;~a stove;~a refrigerator;~a light bulb;~a lamp;~a fan;~water;~a credit card',
 'writing': 'a book;a newspaper;money;a coin;a credit card;cereal;a calculator;a clock;a ruler;a battery;a remote control;a cardboard box;a bottle;a pencil;a pen;a crayon;a computer;a laptop;a phone;a TV;a video game console;a microwave;a bus;a train;a truck;an airplane;a rocket;a traffic light_x;~paper;~a watch;~a T-shirt;~a mug;~a can_x;~a stapler;~a camera;~a light bulb;~a toaster;~a washing machine;~a refrigerator;~a car;~a boat;~a helicopter;~a garbage can;~a backpack;~a hat;~a cake;~chocolate;~a cookie;~popcorn;~a robot;~a school;~a hospital;~a ball;~a skateboard;~a game;~LEGO bricks;~a candle;~a ring;~a sword;~a key',
 'uniform': 'a police officer;a firefighter;a nurse;a soldier;a pilot;a mailman;a chef;an astronaut;a doctor;~a dentist;~a teacher;~a farmer;~a clown;~a king;~a queen;~a pirate',
 'hospital': 'a doctor;a nurse;a hospital;a bed;~a dentist;~a baby;~an ambulance;~a person;~a TV;~a towel;~soap;~a phone;~glasses;~a wheelchair_x',
 'royal': 'a king;a queen;a castle;a crown;~a diamond;~a necklace;~a ring;~gold;~a sword;~a horse;~a lion;~a peacock;~a swan;~a dragon;~a unicorn;~a wizard',
 'foodthere': 'a restaurant;a mall;an airport;a movie theater;a zoo;a farm;a school;a hospital;a park;a beach;~a city;~a library;~a castle;~an island;~a house;~a church',
 'scary': 'a vampire;a zombie;a ghost;a witch;a monster;a dragon;a nightmare;a shark;a snake;a cobra;a rattlesnake;a python;a spider;a scorpion;a tornado;lightning;a crocodile;a T-rex;a dinosaur;a wolf;a bear;a cave;thunder;a volcano;~a bat;~a clown;~a pirate;~Bigfoot;~an alien;~a dentist;~a wasp;~a bee;~a lion;~a tiger;~a gorilla;~fire;~Halloween;~a shadow;~a skeleton_x;~a cockroach;~a rat;~an owl;~the ocean;~fog;~a secret',
 'dessert': 'ice cream;a cake;a cookie;a pie;a donut;candy;chocolate;a lollipop;~a muffin;~a pancake;~a waffle;~jam;~a strawberry;~a banana;~a watermelon;~maple syrup;~popcorn;~gum',
 'ball': 'a ball;a soccer ball;a baseball;a football;a basketball_x;~a balloon;~a marble;~an orange;~a bubble;~the earth;~the moon;~a planet;~a snowman',
 'rings': 'a bell;a phone;a doorbell;a smoke alarm;a clock;a microwave;a watch;~a smartwatch;~a computer;~a laptop;~a tablet;~a dishwasher;~a washing machine;~a car;~a fire truck;~an ambulance;~a police car;~a video game console;~a remote control;~a toaster;~a calculator;~a whistle;~a bicycle',
 'thorns': 'a rose;a cactus;a porcupine;a hedgehog;a pineapple;~a pine cone;~a pine tree;~a tree;~a flower;~a raspberry;~a starfish;~a lizard;~a dinosaur;~a dragon;~a fish_x',
 'envelope': 'paper;money;a credit card;a leaf;a newspaper_x;a paper clip;~a coin;~a key;~a ring;~a necklace;~a diamond;~a crayon;~a pencil;~a comb;~a ruler;~a cookie;~chocolate;~a flower;~a rose;~a book;~a newspaper;~a T-shirt;~socks;~a battery;~a nail;~an ant;~a spider;~a fly;~a ladybug;~a butterfly;~a bee;~a mosquito;~grass;~sand;~salt;~seeds_x;~a number;~love;~a song;~a sandwich',
}
_NAMES = set(o[0] for o in OBJ)
EX = {}                                                        # name -> {question: 4 yes / 2 sometimes}
EX_UNKNOWN = set()
for _k, _v in EXTRA.items():
    for _w in _v.split(';'):
        _n = _w.lstrip('~')
        if _n.endswith('_x'): continue
        if _n not in _NAMES: EX_UNKNOWN.add(_n); continue
        EX.setdefault(_n, {})[_k] = 2 if _w.startswith('~') else 4

ALIVE_CATS = ('A',)
BIGMED = set(('a skateboard', 'a kite', 'a vacuum cleaner', 'a flag', 'a monitor', 'a laundry basket', 'a cooler', 'a fish tank', 'a tricycle', 'a life jacket',
    'a car seat', 'a litter box', 'a medicine cabinet', 'a towel rack', 'a leaf blower', 'a dog bed', 'a tripod', 'a guitar', 'an umbrella', 'a tennis racket', 'a keyboard',
    'a drum', 'a chainsaw', 'an axe', 'a pillow', 'a backpack', 'a doormat', 'a dartboard', 'a mirror', 'a lamp', 'a snow brush', 'a printer', 'a computer', 'a sign',
    'a raincoat', 'a toaster oven', 'a birdcage', 'a pizza box', 'a serving tray', 'a teddy bear', 'a paper shredder', 'a sewing machine', 'a dish rack', 'a mailbox'))
BIG4 = set(('a tricycle', 'a guitar', 'a vacuum cleaner', 'a car seat', 'a laundry basket', 'a fish tank'))
BIG2 = set(('a skateboard', 'a cooler'))   # (the user: sometimes)
MIDMED = set(('a laptop', 'a briefcase', 'a toolbox', 'a frying pan', 'a wok', 'a pot', 'a trumpet', 'a violin', 'a board game', 'a heater', 'a fan', 'a bowling ball',
    'a basketball', 'a soccer ball', 'a volleyball', 'a football', 'a helmet', 'a purse', 'a shopping bag', 'a globe', 'a record player', 'a cash register', 'a slow cooker',
    'an air fryer', 'a rice cooker', 'a projector', 'a speaker', 'a gas can', 'a can of paint', 'a watering can', 'a bucket', 'a garbage bag', 'a doll', 'boots'))

INSTRUMENTS = set(('a guitar', 'a trumpet', 'a piano', 'a drum', 'a harmonica', 'a violin', 'a flute', 'a ukulele', 'a xylophone', 'a recorder', 'a whistle'))
PLAYS = set(('a radio', 'a record player', 'a CD', 'a DVD or Blu-ray', 'a video game console', 'a game controller', 'a music box', 'a speaker', 'a drumstick', 'a rattle'))
GAMES = set(('a board game', 'a chess set', 'a playing card', 'a pair of dice', 'a domino', 'a puzzle', "a Rubik's cube", 'a pool table', 'a dartboard'))
PLAYED4 = set(('a video game console','a DVD or Blu-ray','a CD','a record player','a pool table','a dartboard'))
ODDS = {
    'an apple': {'gift': 1}, 'a bag of trail mix': {'travel': 0}, 'a flower': {'fragile': 0}, 'a mint leaf': {'sweet': 0},
    'a nest': {'washable': 0}, 'a spider web': {'washable': 1}, 'a gnome': {'moves': 0},
    'a sheet of paper': {'fragile': 0}, 'a tissue': {'fragile': 0}, 'a balloon': {'fragile': 2}, 'a bath bomb': {'fragile': 2},
    'a bag of flour': {'baked': 1}, 'a whisk': {'baked': 0}, 'a toaster': {'baked': 0}, 'a magnet': {'sticky': 2},
    'a postcard': {'travel': 0}, 'a sleeping bag': {'travel': 0}, 'a water bottle': {'travel': 0}, 'a cooler': {'travel': 0},
    'a compass': {'info': 0}, 'a thermometer': {'info': 1}, 'a school': {'foodthere': 2}, 'a hot tub': {'comfort': 1},
    'a printer': {'paper': 1}, 'a smoke alarm': {'rolls': 0}, 'a vacuum cleaner': {'rolls': 0}, 'a watch': {'rolls': 1},
    'earbuds': {'loud': 0}, 'headphones': {'music': 1}, 'a coat': {'cold': 0}, 'a sled': {'cold': 1},
    'a stethoscope': {'hardware': 0}, 'a finger': {'rings': 0}, 'a subway': {'underground': 0}, 'a tunnel': {'underground': 0},
    'dirt': {'underground': 0}, 'a bee': {'flower': 0}, 'a butterfly': {'flower': 0}, 'a polar bear': {'winter': 0},
    'a bottle of hot sauce': {'dangerous': 1}, 'a bottle of wine': {'expensive': 2}, 'ice skates': {'hospital': 0},
}
WILD = {'a goose': 3, 'a parrot': 2, 'a peacock': 2, 'a tree': 4, 'a flower': 3, 'a blade of grass': 4, 'a cactus': 4, 'seaweed': 4, 'a palm tree': 3,
        'a pine tree': 4, 'a dandelion': 4, 'moss': 4, 'a bush': 3, 'a sunflower': 2, 'a mint leaf': 2, 'a plant': 2, 'a tulip': 1, 'a stalk of wheat': 1}
NOISE = {'a bird': 4, 'a child': 4, 'a person': 4, 'a wasp': 4, 'an eagle': 4, 'a squirrel': 3, 'a fox': 3, 'a moose': 3, 'a zebra': 3, 'a camel': 3,
         'an otter': 3, 'a buffalo': 3, 'a llama': 3, 'a swan': 3, 'an alligator': 3, 'a ferret': 3, 'a rat': 3, 'a chipmunk': 3, 'an ostrich': 3,
         'a flamingo': 3, 'a snake': 3, 'a raccoon': 2, 'a deer': 2, 'a panda': 2, 'a cheetah': 2, 'a rhino': 2, 'a beaver': 2, 'a hamster': 2,
         'a hedgehog': 2, 'a dragonfly': 2, 'a keychain': 2, 'nail clippers': 2, 'fire': 3, 'a door': 3, 'a key': 2, 'scissors': 2, 'a kettle': 3,
         'a refrigerator': 3, 'a toaster': 2, 'a pop can': 2, 'a ball': 2, 'a hammer': 2, 'a stapler': 3, 'a can opener': 2, 'a computer': 2, 'a basketball': 2}

def boxy(name):                       # things that are themselves a box or carton (a cereal box, an egg carton, a jewelry box...)
    n = name.lower(); return ('box' in n or 'carton' in n or 'crate' in n) and 'boxing' not in n

def answers(name, cat, size, tags):
    t = {}; force = {}
    for w in tags.split():
        if w.endswith('_x'): continue                      # (notes, not used)
        v = 4;
        if w[0] == '+': v, w = 3, w[1:]
        elif w[0] == '~': v, w = 2, w[1:]
        elif w[0] == '-': v, w = 1, w[1:]
        if w[0] == '$' and w not in ('$made', '$madefood', '$natural'): force[w] = v; continue   # (a worked-out answer, set by hand: applied last)
        t[w] = max(t.get(w, 0), v)
    made = t.pop('$made', 0) or t.pop('$madefood', 0)
    for k, v in EX.get(name, {}).items(): t[k] = max(t.get(k, 0), v)
    # (for every thing: obvious answers to the later questions, so household things aren't marked "no" by mistake)
    g0 = lambda k: t.get(k, 0)
    for k, v in (('tasks', max(g0('tool'), g0('appliance'), g0('clean'), g0('cook'), g0('eatwith'), g0('write'), g0('vehicle'), g0('office'), g0('talk') if t.get('person', 0) < 3 else 0, g0('electric') if cat == 'M' else 0)),   # (anything you use for a job) ('hasliquid', max(g0('liquid'), g0('drink'))),
                 ('washable', max(g0('cloth'), g0('eatwith'))), ('enjoy', max(g0('toy'), g0('dessert'), g0('music'))), ('public', g0('vehicle'))):
        if v >= 3 and t.get(k, 0) < v: t[k] = v
    if name in _NEWNAMES:                                         # (things added later: no hand lists for these questions, so fill them sensibly)
        g = lambda k: t.get(k, 0)
        derive = {'washable': max(g('cloth'), g('eatwith'), 2 if cat == 'A' else 0, 2 if g('eat') >= 3 else 0),
                  'tasks': max(g('tool'), g('appliance'), g('job')), 'enjoy': max(g('toy'), g('sweet'), g('snack'), g('music'), g('pet'), g('sport'), 2),
                  'travel': g('vehicle'), 'hasliquid': max(g('liquid'), g('juicy'), g('drink')), 'desk': 2 if g('office') >= 3 else 0,
                  'info': 2 if g('read') >= 3 or g('screen') >= 3 else 0, 'paint': 2 if cat == 'M' or g('wood') >= 3 else 0,
                  'leaves': 4 if g('plant') >= 3 else 0, 'kinds': 2, 'rabbits': 3 if (g('veg') >= 3 and g('green') >= 3) else 0,
                  'smooth': 2, 'larger': 4 if g('fruit') >= 3 else (2 if cat == 'V' else 0), 'rolls': 2 if g('round') >= 3 else 0,
                  'wet': max(g('water'), g('watery')), 'sliced': 2 if g('cooked') >= 3 or g('fruit') >= 3 else 0, 'envelope': 2 if g('flat') >= 3 and (size == 0) else 0,
                  'songs': 2, 'forest': 0, 'claws': 2 if g('mammal') >= 3 or g('bird') >= 3 else 0, 'public': max(g('vehicle'), g('wear'), 2 if g('pocket') >= 3 else 0),
                  'withpc': 0, 'addictive': 2 if g('sweet') >= 3 else 0, 'box': 2 if cat == 'M' and size != 'x' and size <= 2 else 0, 'played': max(g('music'), g('toy') // 2 * 2, g('sport') // 2 * 2),
                  'comfort': 2 if g('soft') >= 3 else 0, 'set': 0, 'payuse': 2 if g('vehicle') >= 3 or 'place' in t else 0, 'writing': 2 if g('read') >= 3 else 0}
        for k, v in derive.items():
            if k not in t: t[k] = v
    # worked-out tags
    product = t.pop('product', 0)
    creature = cat == 'A' and 'body' not in t and not product and (not any(k in t for k in ('eat', 'drink', '$x')) or any(k in t for k in ('mammal', 'bird', 'fish', 'reptile', 'insect', 'tail', 'four_legs', 'many_legs', 'wings', 'swims', 'shell', 'wild', 'pet')))
    if cat == 'A' and 'body' not in t and not creature and made == 0 and name not in ('milk', 'an egg', 'honey'): made = 4   # (bacon, cheese, butter... are made)
    if (creature or 'person' in t): t.setdefault('alive', 4); t.setdefault('moves', 4); t.setdefault('face', 4)
    if 'plant' in t: t.setdefault('alive', 4)
    for k in ('fruit', 'veg'):
        if t.get(k, 0) >= 3: t.setdefault('eat', 4)
    if cat == 'A' and 'wild' not in t and 'pet' in t: pass
    if creature and not any(k in t for k in ('pet', 'farm')): t.setdefault('wild', 4)
    if 'wood_grows' in t: t.pop('wood_grows'); t['wood'] = 2
    if cat == 'M' and not made: made = 4
    if cat == 'M' and name in ('a rock', 'sand', 'a diamond', 'gold', 'ice', 'snow', 'salt'): made = 0
    if cat == 'M' and name == 'a diamond': made = 2
    if cat == 'V' and made == 0 and any(k in t for k in ('$madefood',)): made = 4
    if 'job' in t or 'building' in t: made = max(made, 4 if 'building' in t else 0)
    if name in ('a school', 'a hospital', 'a castle', 'a house', 'a park', 'a game', 'the internet', 'a song', 'music', 'a robot', 'a birthday party', 'a number'): made = 4
    t['$made'] = made
    for k in ('four_legs', 'two_legs', 'many_legs'):
        if k in t: t['$legs'] = max(t.get('$legs', 0), t[k])
    t['$touch'] = 0 if (size == 'x' or name in ('the sun', 'a star', 'a rainbow', 'a shadow', 'lightning', 'a ghost', 'wind')) else (2 if name in ('the moon', 'a cloud', 'smoke', 'fire', 'a dragon', 'a unicorn', 'Santa Claus') else 4)
    if cat in 'AV' or 'eat' in t or 'drink' in t: t.setdefault('$natural', 4)
    # size questions
    s = size if size != 'x' else None
    def sz(cond_yes, cond_some):
        if s is None: return 0
        return 4 if cond_yes(s) else (2 if cond_some(s) else 0)
    t['$small'] = sz(lambda s: s <= 1, lambda s: s == 2)
    t['$person'] = sz(lambda s: s >= 4, lambda s: s == 3)
    t['$car'] = sz(lambda s: s >= 5, lambda s: s == 4)
    t['$pickup'] = sz(lambda s: s <= 2, lambda s: s == 3)        # (the whole thing, with your own hands, no jack: a chair or a child sometimes, a car never)
    if size == 3 and t['$pickup']:                               # (person-sized things: it depends what it is)
        gp = lambda k: t.get(k, 0)
        t['$pickup'] = 0 if gp('engine') >= 3 else (1 if gp('appliance') >= 3 else (2 if (gp('alive') >= 3 or (gp('furniture') >= 3 and name not in ('a chair', 'a stool', 'a lawn chair', 'a high chair'))) else 3))
    # long or wide but light: you can still pick these up
    _PU = {'a ladder': 4, 'a surfboard': 4, 'skis': 4, 'a snowboard': 4, 'a fishing rod': 4, 'a paddle': 4, 'a toboggan': 4, 'a sled': 4, 'a rug': 3, 'a rope': 4, 'a hose': 4, 'a flag': 4, 'a ski pole': 4, 'a hockey stick': 4, 'a tent': 3, 'a hula hoop': 4, 'a pogo stick': 4, 'a crutch': 4, 'a broom': 4, 'a mop': 4, 'a rake': 4, 'a shovel': 4, 'a branch': 3, 'a kite': 4, 'a curtain': 4, 'a hammock': 4, 'a parachute': 3, 'a sleeping bag': 4, 'a shower curtain': 4, 'a canoe': 2, 'a kayak': 2, 'a hockey net': 2, 'a bench': 2, 'a wheelbarrow': 2, 'a wagon': 3, 'a stroller': 3, 'a tricycle': 4, 'a unicycle': 4, 'a scooter': 3, 'a skateboard': 4, 'a lawn chair': 4}
    if name in _PU: t['$pickup'] = _PU[name]
    t['$heavy'] = sz(lambda s: s >= 3, lambda s: s == 2)          # (heavy = harder to lift than a backpack)
    if 'heavy' in t: t['$heavy'] = max(t['$heavy'], t['heavy'])
    t['$pound'] = sz(lambda s: s >= 2, lambda s: s == 1)
    t['$small2'] = 0 if s is None else (0 if s == 0 else (3 if s == 1 else 4))   # ("bigger than a hamster": pocket things no, mug-sized usually, the rest yes)
    t['$duck'] = sz(lambda s: s >= 3, lambda s: s == 2)
    if t.get('$heavy', 0) >= 3: t['$pound'] = 4
    # hard: made of metal, glass or wood, or has a shell (soft things aren't)
    if t.get('soft', 0) >= 3 or t.get('liquid', 0) >= 3 or size == 'x': t['$hard'] = 0
    elif max(t.get('metal', 0), t.get('glass', 0), t.get('wood', 0), t.get('shell', 0), t.get('hard', 0)) >= 3 or name in ('a rock', 'a diamond', 'gold', 'ice', 'a coconut', 'a peanut', 'a dinosaur', 'a robot', 'a mountain', 'a tree', 'a log', 'a turtle'): t['$hard'] = 4
    elif t.get('plastic', 0) >= 3: t['$hard'] = 3
    elif cat == 'A' or 'person' in t: t['$hard'] = 0
    else: t['$hard'] = 2
    if s is not None and s <= 0: t.setdefault('pocket', 4)
    # where
    ind = t.pop('indoor', 0)
    home = max([t.get(k, 0) for k in ('kitchen', 'bathroom', 'bedroom', 'furniture', 'appliance')] + [ind])
    if cat == 'A': t['$indoors'] = ind; t['$outdoors'] = 4 if ind < 4 else 2
    elif 'place' in t or 'sky' in t or 'weather' in t or 'plant' in t or 'vehicle' in t: t['$indoors'] = 0; t['$outdoors'] = 4
    else: t['$indoors'] = 4 if home >= 3 else 2; t['$outdoors'] = 2 if home < 3 else 0
    if t.pop('alsoout', 0): t['$indoors'] = 3; t['$outdoors'] = 3
    if cat == 'A' and t.get('pet', 0) >= 3 and size != 'x' and size >= 2: t['$indoors'] = 2   # (dogs, cats: sometimes inside)
    if cat == 'M' and max(t.get('electric', 0), t.get('battery', 0)) >= 3 and t.get('plastic', 0) < 2: t['plastic'] = 2   # (electronics: partly plastic)
    if (t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3) and t.get('everyday', 0) < 2: t['everyday'] = 2   # (food: sometimes daily)
    # how the player answers (asked Nov 8): applied to every thing
    g = lambda k: t.get(k, 0); up = lambda k, v: t.__setitem__(k, max(g(k), v))
    isfood = g('eat') >= 3 or g('drink') >= 3
    if isfood and cat != 'A' or (isfood and cat == 'A' and 'farm_x' in t): up('kitchen', 3)
    if cat == 'A' and 'body' not in t and g('farm') >= 3 and (g('mammal') >= 3 or g('bird') >= 3) and name not in ('a horse', 'a dog', 'a donkey', 'a llama', 'a pony', 'a cat', 'a rabbit', 'a peacock', 'a lamb_x'): up('eat', 4)
    if g('fur') >= 3 and name not in ('a porcupine', 'a hedgehog'): up('soft', 3)
    if g('pet') >= 3 or g('vehicle') >= 3 or t.get('person', 0) >= 3 or name in ('love', 'a friend', 'a mom', 'a baby', 'a house', 'a phone', 'money'): up('expensive', 3)
    if g('comfort') >= 3 or g('gift') >= 3: up('expensive', 2)
    if g('vehicle') >= 3 and cat == 'M': t['moves'] = 0 if name in ('a bus', 'a train', 'a truck', 'a tractor', 'a skateboard', 'a wagon', 'a wheelchair', 'a canoe', 'a shopping cart') else 2   # (self-driving cars and e-bikes: sometimes; a bus: no)
    if name in ('an apple', 'a carrot', 'a potato', 'a pear', 'a coconut', 'a peanut', 'an almond', 'a walnut', 'an acorn', 'a radish', 'a beet', 'corn', 'a cucumber', 'a pumpkin', 'a sweet potato', 'celery', 'an onion'): t['$hard'] = 4
    if cat in 'MV' and g('colorful') == 2 and (g('$made') >= 3 or isfood): t['colorful'] = 3
    if g('vehicle') >= 3 and g('engine') >= 3: up('container', 4)
    if name in ('a couch', 'a bench', 'a piano', 'a dresser'): up('four_legs', 2)
    if g('appliance') >= 3 and g('cook') >= 3: up('hot', 4)
    if cat == 'M' and g('noise') < 2 and size != 'x': t['noise'] = 2
    if cat == 'A' or t.get('person', 0) >= 3: up('washable', 4)
    if name in ('a tomato', 'a cucumber', 'a pumpkin', 'a bell pepper', 'an eggplant', 'a zucchini', 'an avocado', 'a hot pepper', 'corn', 'peas', 'green beans'): up('fruit', 4); t['veg'] = 2
    if g('wear') >= 3 and g('cloth') >= 2: up('bedroom', 3)
    if (g('sharp') >= 3 or g('hot') >= 3) and not isfood and cat != 'O': up('dangerous', 3)
    if name in ('a phone', 'a wallet', 'a key', 'money', 'a coin', 'a credit card'): up('pocket', 4)
    if g('sport') >= 3 or g('ball') >= 3 or name in ('a rake', 'a shovel', 'a hose', 'a lawn mower', 'a wheelbarrow', 'a bucket', 'a ladder', 'a saw', 'an axe', 'a chainsaw'): t['$outdoors'] = 4
    if name in ('a clock', 'a doll', 'a robot', 'a teddy bear', 'a snowman', 'a jack-o-lantern', 'a scarecrow', 'a watch', 'a rubber duck', 'a toy car_x'): up('face', 4)
    if cat == 'M' and g('kitchen') >= 3 and max(g('cook'), g('eatwith')) >= 3 and size != 'x' and size <= 2 and g('appliance') < 3: up('tool', 2)
    if g('appliance') >= 3: up('metal', 2)
    if g('vehicle') >= 3 and g('wheels') >= 3 and size != 'x' and size <= 4: up('garage', 3)
    if name in ('milk', 'butter', 'ice cream', 'yogurt', 'cheese', 'orange juice', 'soda', 'lemonade', 'beer', 'a milkshake', 'an egg', 'lettuce'): up('cold', 3)
    if g('bathroom') >= 3: up('water', 2)
    if g('battery') >= 3: up('electric', 3)
    # old = around 50 years or more
    modern = ('a laptop', 'a tablet', 'a smartwatch', 'a USB stick', 'an air fryer', 'a charger', 'the internet', 'a video game console', 'a phone', 'a computer', 'a microwave', 'a smoke alarm', 'a computer mouse', 'a remote control', 'a credit card', 'LEGO bricks', 'a jet ski', 'a printer', 'headphones', 'a calculator', 'a skateboard', 'a frisbee', 'a rice cooker', 'a slow cooker', 'a dishwasher', 'a sticky note', 'a glue gun')
    if name in modern: t['old'] = 2 if name in ('a phone', 'a computer', 'a microwave', 'headphones', 'a calculator', 'a skateboard', 'a remote control', 'a video game console', 'a printer', 'a dishwasher', 'a credit card', 'LEGO bricks') else 0
    elif size != 'x' or cat != 'O': up('old', 3)

    t['$livewater'] = 4 if (t.get('fish', 0) >= 3 or name in ('seaweed',) or (cat == 'A' and t.get('ocean', 0) >= 3)) else (2 if cat == 'A' and t.get('water', 0) >= 3 and t.get('swims', 0) >= 3 else 0)
    t['$beak'] = 4 if t.get('bird', 0) >= 3 else (2 if name in ('an octopus', 'a turtle', 'a dinosaur') else 0)
    madeit = t['$made'] >= 3
    small = s is not None and s <= 2
    # hold = anything two hands can hold (clothes, a cat, a pizza); bigger things sometimes; can't touch it = no
    t['$hold'] = 0 if (size == 'x' or t['$touch'] == 0) else (4 if size <= 2 else (2 if size == 3 else 0))
    # "Would it fit in your two hands?": cupped or held together, not hugged. A mug or a phone yes, a cat or a pizza sometimes, a chair or a building no.
    if t['$hold']: t['$hold'] = 4 if size <= 1 else (2 if size == 2 else 0)
    if t['$hold'] and (g('liquid') >= 3 or g('gas') >= 3 or name in ('fire', 'smoke', 'a cloud', 'lightning', 'the moon')): t['$hold'] = 2 if g('liquid') >= 3 else 0
    t['$household'] = 4 if (madeit and cat in 'MV' and t['$indoors'] >= 3 and t.get('vehicle', 0) < 3) else (2 if madeit and cat in 'MV' and t['$indoors'] >= 2 and t.get('vehicle', 0) < 3 else 0)
    if isfood: t['$household'] = 4 if name in STAPLES else 2    # (salt, butter, bread: yes; a jar of salsa: sometimes)
    t['office2'] = t.get('office', 0)
    t['$home'] = 4 if (t['$indoors'] >= 3 and (madeit or t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3)) else (2 if t['$indoors'] >= 2 and (madeit or t.get('pet', 0) >= 3 or t.get('eat', 0) >= 3) else 0)
    touchable = t['$touch'] >= 3
    # "Would a thief want to steal it?" (not "could it be stolen": anything could)
    g_ = lambda k: t.get(k, 0)
    if not touchable or 'place' in t or g_('person') >= 3 or g_('body') >= 3: t['$steal'] = 0
    elif g_('expensive') >= 3 or name in ('money', 'a coin', 'a wallet', 'a purse', 'a credit card', 'a phone', 'a laptop', 'a tablet', 'a TV', 'a computer', 'a camera', 'a bicycle', 'a car', 'a motorcycle', 'a watch', 'a smartwatch', 'a ring', 'a necklace', 'earrings', 'a bracelet', 'gold', 'silver', 'a diamond', 'a video game console', 'a painting', 'a crown', 'a purse', 'a suitcase', 'a backpack', 'a key', 'a piggy bank', 'headphones', 'earbuds', 'a drone', 'a truck', 'a pickup truck', 'a scooter', 'a snowmobile', 'an ATV', 'a trophy', 'a medal', 'a pearl', 'a ruby', 'an emerald', 'a guitar', 'an electric guitar', 'a present', 'a lottery ticket', 'a ticket', 'a boat', 'a jet ski', 'a toolbox', 'a drill', 'a chainsaw', 'a game controller', 'a GPS', 'a speaker', 'sunglasses', 'a skateboard', 'a statue', 'a crystal ball'): t['$steal'] = 4
    # (from the survey: a burglar takes what is easy to sell: gadgets, sports gear, power tools, medicine.
    #  Not food, not clothes, not kitchen tools, and nothing bolted down or built in.)
    elif g_('engine') >= 3 and g_('vehicle') < 3 or name in ('a lawn mower', 'a leaf blower', 'a weed whacker', 'a chainsaw', 'a drill', 'a pill', 'a pill bottle', 'a jewelry box', 'a music box'): t['$steal'] = 4
    elif madeit and s is not None and s <= 2 and g_('electric') >= 3 and (g_('screen') >= 3 or g_('music') >= 3 or g_('camera') >= 3) and name != 'a calculator': t['$steal'] = 4
    elif g_('wall') >= 3 or name in ('a ferris wheel', 'a roller coaster', 'a calculator_x', 'a traffic light', 'an elevator', 'an oven', 'a stove', 'a ceiling fan', 'an exit sign', 'a hand dryer', 'a slide', 'a kiddie pool'): t['$steal'] = 0
    elif g_('pet') >= 3: t['$steal'] = 2
    elif g_('eat') >= 3 or g_('drink') >= 3 or g_('farm') >= 3 or g_('kitchen') >= 3: t['$steal'] = 0
    elif madeit and s is not None and s <= 4 and (g_('sport') >= 3 or g_('music') >= 3 or (g_('electric') >= 3 and s <= 3) or (g_('toy') >= 3 and s >= 2)): t['$steal'] = 2
    else: t['$steal'] = 0
    t['$buy'] = 0 if not touchable and name not in ('music', 'a song', 'a game', 'the internet') else (4 if madeit or t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3 or t.get('pet', 0) >= 3 or name in ('a house', 'gold', 'a diamond', 'salt', 'ice', 'a flower', 'a rose', 'a tree', 'a cactus', 'water', 'sand', 'a log') else (2 if t.get('farm', 0) >= 2 or name in ('an island', 'a castle', 'a rock', 'a sunflower', 'cotton', 'seaweed', 'grass') else 0))
    if t.get('job', 0) >= 3: t['$buy'] = 0
    if cat == 'A' and t.get('farm', 0) >= 3: t['$buy'] = 4   # (you can legally buy farm animals and pets; not wild ones)
    t['$joy'] = t.get('enjoy', 0)
    t['$microwave'] = sz(lambda s: s >= 4, lambda s: s == 3)
    # "Is it bigger than a case of beer?" (a case is about 16 x 11 x 10 inches). Chair-sized things usually are; a medium thing only if it is long
    # (a guitar, a skateboard, a snow shovel) or wide (a monitor, a laundry basket); hand-sized things never.
    if s is not None and s == 3: t['$microwave'] = 3
    elif s is not None and s == 2:
        t['$microwave'] = 4 if name in BIG4 else 2 if name in BIG2 else (3 if name in BIGMED else (2 if t.get('long', 0) >= 3 else (1 if name in MIDMED else 0)))
    t['$invented'] = 0 if t['$made'] < 3 else (2 if (t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3 or t.get('job', 0) >= 3 or name in ('music', 'a song', 'a house', 'a park', 'a birthday party', 'a number', 'paper_x')) else 4)
    if name in ('a computer',): t['withpc'] = 4
    t['$bring'] = 4 if (madeit and small and (t.get('pocket', 0) >= 3 or t.get('public', 0) >= 3 or t.get('travel', 0) >= 3 or t.get('wear', 0) >= 3)) else (2 if (small and touchable and (madeit or t.get('snack', 0) >= 3 or t.get('pet', 0) >= 3)) else 0)
    t['plugin'] = 4 if t.get('electric', 0) >= 3 and t.get('battery', 0) < 3 and t.get('vehicle', 0) < 3 and size != 'x' and cat == 'M' else (2 if t.get('electric', 0) >= 3 and t.get('battery', 0) >= 2 else 0)
    t['clothes'] = 4 if t.get('wear', 0) >= 3 and (t.get('cloth', 0) >= 3 or name in ('a shoe', 'boots', 'sneakers', 'sandals', 'a raincoat')) else 0
    t['feet'] = 4 if name in ('a shoe', 'socks', 'boots', 'sneakers', 'sandals', 'slippers', 'roller skates', 'skis') else 0
    t['$electronic'] = max(t.get('electric', 0), t.get('battery', 0), t.get('screen', 0))
    t['$huge'] = sz(lambda s: s >= 5, lambda s: s == 4)
    t['$movable'] = 0 if not touchable or 'place' in t else sz(lambda s: s <= 2, lambda s: s == 3)
    # "Do people ever paint it?" (not "could it be painted": anything could)
    PY = ('a fence', 'a house', 'a door', 'a car', 'a fingernail', 'an Easter egg', 'a painting', 'a bench', 'a mailbox', 'a birdhouse', 'a shed', 'a barn', 'a chair', 'a table', 'a dresser', 'a bookshelf', 'a picture frame', 'a toy car', 'a boat', 'a bicycle', 'a kitchen', 'a bedroom', 'a bathroom', 'a gate', 'a doghouse', 'a treehouse', 'a fire hydrant', 'a stop sign', 'a cabinet', 'a shelf', 'a truck', 'a bus', 'an airplane', 'a train', 'a motorcycle', 'a school bus', 'a race car', 'paper', 'clay', 'an artist', 'a garage', 'a closet', 'an apartment', 'a basement', 'a crib', 'a nightstand', 'a coffee table', 'a picnic table', 'a stool', 'a rocking chair', 'a desk', 'a deck', 'a canoe', 'a rowboat', 'a sailboat', 'a wagon', 'a windmill', 'a lighthouse', 'a school', 'a church', 'a sign', 'a billboard', 'an ornament', 'a mask', 'a snowmobile', 'a helicopter', 'a rocket', 'a tank', 'a jet', 'a sports car', 'a convertible', 'a van', 'a minivan', 'a pickup truck', 'a jeep', 'a taxi', 'a fire truck', 'an ambulance', 'a police car', 'a limousine', 'a tractor', 'a go-kart')
    PS = ('a pumpkin', 'a rock', 'a mug', 'a plate', 'a refrigerator', 'a shoe', 'a piano', 'a drum', 'a ladder', 'a bucket', 'a kite', 'a robot', 'a bed', 'a T-shirt', 'a face', 'a statue', 'a road', 'a bathtub', 'a guitar', 'a skateboard', 'a doll', 'a window', 'a castle', 'a hospital', 'a bridge', 'a skyscraper', 'a vase', 'a pot', 'a bowl', 'a toe', 'a hand', 'a pebble', 'a brick', 'a tire', 'a helmet', 'a surfboard', 'a snowboard', 'a sled', 'a toboggan', 'a boomerang', 'a jack-o-lantern', 'a pine cone', 'a seashell', 'a log', 'a cardboard box', 'a crate', 'a barrel', 'a basket', 'a hockey stick', 'a trophy', 'a flag', 'a poster', 'a clock', 'a lamp', 'a toy train', 'a dollhouse', 'an action figure', 'a puppet', 'a coffin', 'a tombstone', 'a house_x', 'a staircase', 'a chimney', 'a fireplace', 'a radiator', 'a doorknob', 'a mirror', 'a cutting board', 'a wooden spoon', 'a broom', 'a rolling pin', 'a baseball bat', 'a violin', 'a cello', 'a ukulele', 'a banjo', 'a harp', 'an electric guitar', 'a xylophone', 'a submarine', 'a cruise ship', 'a yacht', 'a ferry', 'a speedboat', 'a kayak', 'a hot air balloon', 'a ferris wheel', 'a roller coaster', 'a swing', 'a slide', 'a seesaw', 'a trampoline', 'a lawn chair', 'a barbecue', 'a garbage can', 'a traffic light', 'a street light', 'a parking meter', 'a sidewalk', 'concrete', 'a tile_x', 'a stick', 'a branch', 'a tree stump', 'a leaf', 'an egg', 'a cookie', 'a cake', 'lips', 'a mouth_x', 'an eye_x', 'a spaceship', 'a satellite', 'a crane', 'a bulldozer', 'a forklift', 'an excavator', 'a dump truck', 'a tow truck', 'a garbage truck', 'a snowplow', 'a zamboni', 'a golf cart', 'a scooter', 'a tricycle', 'a unicycle', 'a stroller', 'a shopping cart', 'a trailer', 'a camper', 'a wheelbarrow', 'a lawn mower')
    t['paint'] = 4 if name in PY else (2 if name in PS else 0)
    t.update(extra_answers(name, cat, size, t, globals().get('DISPLAY', {}).get(name))); t.update(force)
    # Answers a real player gave in the training survey. One person's answer is evidence, not the truth (the next player may
    # answer differently), so it moves Zandor to "usually" / "rarely" rather than a flat yes / no, unless he already leaned that way.
    # lighter than a hot dog: pocket things mostly are, unless they are dense; paper and cloth things up to a mug's size are too
    _s = None if size == 'x' else size
    t['$light'] = 0 if _s is None else (3 if _s == 0 else ((3 if (t.get('paper', 0) >= 3 or t.get('cloth', 0) >= 3) else 1) if _s == 1 else 0))
    if name in ('a phone', 'a wallet', 'a hockey puck', 'a lock', 'a pocket knife', 'a rock', 'a watch', 'a battery', 'a golf ball', 'a baseball', 'a stapler', 'a mug', 'a brick', 'a smartwatch', 'a harmonica', 'a camera'): t['$light'] = 0 if name not in ('a watch', 'a battery', 'a golf ball', 'a smartwatch', 'a harmonica') else 2
    if name in ('a feather', 'a leaf', 'a tissue', 'a napkin', 'a balloon', 'a straw', 'a paper airplane', 'an envelope', 'a stamp', 'a ticket', 'a receipt', 'a sticky note', 'a paper clip', 'a button', 'a coin', 'a key', 'a match', 'a toothpick', 'a needle', 'a hair tie', 'a rubber band', 'a bubble', 'a snowflake', 'a butterfly', 'a fly', 'a mosquito', 'an ant', 'a ladybug', 'a bee'): t['$light'] = 4
    if name in MASS:
        for k in ('$small', '$small2', '$pound', '$duck', '$heavy', '$light', '$microwave', '$pickup', '$hold', 'pocket'): t[k] = 2
        if name in ('fire', 'smoke', 'lightning', 'fog'): t['$hold'] = 0; t['$pickup'] = 0; t['pocket'] = 0   # (you can't hold these at all)
    # A container with something in it (a bag of trail mix, a glass of milk, a bowl of soup): the bag or glass is one thing and
    # what is inside is another, so "is it hard?" and "is it soft?" have no single answer. Both are "sometimes".
    _shown = globals().get('DISPLAY', {}).get(name, '')
    if _shown.split(' of ')[0] in ('a bag', 'a bowl', 'a plate', 'a glass', 'a cup', 'a mug', 'a bottle', 'a jar', 'a can', 'a tub', 'a jug', 'a tube', 'a pack'):
        t['$hard'] = 2; t['soft'] = 2
    # "Is it cold to the touch?": winter clothes and gear keep you warm, they are not cold themselves
    if name in ('a scarf', 'mittens', 'a thermos', 'a sled', 'skis', 'boots', 'a sweater', 'a coat', 'gloves', 'a fan', 'a toque', 'a jacket', 'a hoodie', 'a snowboard', 'a toboggan', 'ice skates', 'a snowmobile'): t['cold'] = 0
    if name in ('a refrigerator', 'a freezer', 'a cooler', 'an air conditioner', 'a vent'): t['cold'] = 2   # (cold inside, not outside)
    # Nov 13: rule corrections found by comparing the rules with a real player's survey answers
    gg = lambda k: t.get(k, 0)
    if max(gg('wall'), gg('appliance'), gg('furniture'), gg('floor'), gg('hang')) >= 3: t['$bring'] = min(gg('$bring'), 0)   # (fixed in place: a light switch, an outlet)
    if gg('eat') >= 3 and gg('snack') < 3: t['$bring'] = min(gg('$bring'), 1)            # (ingredients and meals stay home)
    if max(gg('wall'), gg('appliance'), gg('furniture')) >= 3: t['pocket'] = min(gg('pocket'), 1)   # (you can't pocket what's fixed to the wall)
    if gg('kitchen') >= 3 and gg('$bring') == 2 and name not in ('a lunchbox', 'a thermos', 'a water bottle', 'a juice box', 'a zip-top bag', 'a sippy cup', 'a baby bottle'): t['$bring'] = 1   # (kitchen things stay in the kitchen)
    if size != 'x' and size == 2 and gg('$heavy') < 3 and max(gg('metal'), gg('wood'), gg('glass'), gg('rock')) < 3 and (max(gg('cloth'), gg('paper'), gg('ball'), gg('plastic')) >= 3) and name != 'a bowling ball': t['$pound'] = 1   # (big but light: a soccer ball, a sweater, a flag)
    if size != 'x' and size == 2 and t.get('$pound') == 1 and max(gg('cloth'), gg('paper'), gg('ball')) < 3: t['$pound'] = 2   # (a plastic cooler, bucket or laundry basket: often over a pound)
    if (gg('eat') >= 3 or gg('drink') >= 3) and cat != 'V' and gg('$indoors') >= 2: t['$outdoors'] = min(gg('$outdoors'), 1)   # (food is mostly kept indoors)
    if (gg('eat') >= 3 or gg('drink') >= 3) and cat == 'A' and gg('alive') < 3: t['$indoors'] = 4; t['$outdoors'] = 1   # (butter, milk, a pork chop: kitchen things, not animals in a field)
    if name in ('a bowling ball', 'a bowling pin', 'a trophy', 'a headband', 'a fish tank', 'a pool table', 'a dartboard', 'a treadmill', 'a punching bag', 'a yoga mat', 'dice'): t['$outdoors'] = 1; t['$indoors'] = 4
    if gg('liquid') >= 3 or (cat == 'M' and gg('$hard') >= 3 and max(gg('plastic'), gg('glass'), gg('metal')) >= 3 and name not in ('sandpaper', 'a brick', 'a cheese grater', 'a grater', 'a file', 'a saw')): t['smooth'] = max(gg('smooth'), 3)
    if gg('round') >= 3 and gg('flat') < 3 and size != 'x' and size <= 2 and gg('$movable') >= 3: t['rolls'] = max(gg('rolls'), 3)
    if gg('veg') >= 3 or (gg('fruit') >= 3 and gg('juicy') >= 3): t['sliced'] = max(gg('sliced'), 2)
    # do you take it along when you leave home? Yes: what goes out the door with you (and what you're wearing). Sometimes: a book, a ball.
    _sh = globals().get('DISPLAY', {}).get(name, name)
    if name in LEAVE4 or _sh in LEAVE4: t['$leave'] = 4
    elif name in LEAVE2 or _sh in LEAVE2: t['$leave'] = 2
    elif name in LEAVE1 or _sh in LEAVE1: t['$leave'] = 1
    elif name in LEAVE0: t['$leave'] = 0
    elif gg('wear') >= 3 and gg('body') < 3 and gg('$made') >= 3: t['$leave'] = 4
    elif cat == 'M' and gg('sport') >= 3 and gg('$movable') >= 3 and size != 'x' and size <= 2: t['$leave'] = 2
    elif cat == 'M' and gg('snack') >= 3: t['$leave'] = 2
    else: t['$leave'] = 1 if (cat == 'M' and gg('pocket') >= 3 and max(gg('wall'), gg('kitchen'), gg('office2'), gg('desk'), gg('bathroom'), gg('garage')) < 3) else 0
    # (Nov 14, from the survey: where the rules and real answers kept disagreeing)
    _g = lambda k: t.get(k, 0)
    # "Heavier than a pound of ground beef?" Hand-sized things mostly aren't (a lemon, scissors, a stapler); only the dense ones might be
    # (metal, stone, glass, gadgets, full of liquid). Medium things usually are, not always (a cat, a doll, a purse).
    if size != 'x' and size == 1 and t.get('$pound', 0) == 2:
        t['$pound'] = 2 if max(_g('metal'), _g('rock'), _g('glass'), _g('electric'), _g('hasliquid'), _g('$hard') if _g('wood') >= 3 else 0) >= 3 else 1
    if size != 'x' and size == 2 and t.get('$pound', 0) == 4 and _g('$heavy') < 3: t['$pound'] = 3
    _g = lambda k: t.get(k, 0)
    if (_g('fruit') >= 3 or _g('veg') >= 3) and _g('flat') < 3: t['rolls'] = max(_g('rolls'), 3)       # (a pepper, a mango, lettuce: people say they'd roll)
    if _g('fruit') >= 3 or _g('veg') >= 3: t['washable'] = max(_g('washable'), 3)                         # (you rinse fruit and vegetables)
    elif _g('eat') >= 3 or _g('drink') >= 3: t['washable'] = min(_g('washable'), 1)                       # (but not yogurt or jerky)
    if _g('wood') >= 3 and cat in 'MV' and size != 'x' and size >= 1 and _g('float') >= 3: t['float'] = 2 # (people doubt a wooden stool would float)
    if _g('mammal') >= 3 and size != 'x' and size >= 4: t['loud'] = max(_g('loud'), 2)                    # (a rhino, a giraffe: big animals can be loud)
    # "Do you hold it in your hand to use it?": a fork, a pen, a hammer, a phone, a racket. Not a chair, a lamp, a fridge or a sandwich.
    _sz = 9 if size == 'x' else size
    if _g('$made') < 3 or max(_g('eat'), _g('drink'), _g('alive'), _g('place'), _g('body'), _g('building'), _g('vehicle'), _g('wear'), _g('wall')) >= 3: t['inhand'] = 0
    elif _sz <= 1 and _g('read') >= 3: t['inhand'] = 4
    elif _sz <= 2 and max(_g('tool'), _g('eatwith'), _g('write'), _g('grooming'), _g('clean'), _g('weapon'), _g('blade'), _g('ball'), _g('beltloop')) >= 3: t['inhand'] = 4
    elif _sz <= 2 and _g('handle') >= 3 and max(_g('furniture'), _g('appliance'), _g('container')) < 3: t['inhand'] = 4
    elif _sz <= 1 and (_g('$electronic') >= 3 and _g('buttons') >= 3 or _g('toy') >= 3 or _g('music') >= 3 or _g('sport') >= 3 or _g('game') >= 3): t['inhand'] = 4
    elif max(_g('furniture'), _g('appliance'), _g('decor'), _g('wall'), _g('floor'), _g('wear'), _g('disposable')) >= 3: t['inhand'] = 1 if _sz <= 1 else 0
    else: t['inhand'] = 2 if _sz <= 1 else 0
    for _n4 in ('a phone', 'a book', 'a key', 'tongs', 'a tablet', 'binoculars', 'a lighter', 'an iron', 'a vape', 'a magnifying glass', 'a smartphone', 'a game controller', 'a GPS', 'a walkie-talkie', 'a stylus', 'a fan_x', 'a hair dryer', 'a curling iron', 'a glue gun', 'a drill', 'a leaf blower', 'a weed whacker', 'a fly swatter', 'a squirt gun', 'a water gun', 'a magic wand', 'a rattle', 'a fidget spinner', 'a stress ball', 'a lint roller', 'a nail file', 'tweezers', 'nail clippers', 'a letter opener', 'a staple remover', 'a hole punch', 'a label maker', 'a pizza cutter', 'a peeler', 'a grater', 'a corkscrew', 'a bottle opener', 'a garlic press', 'a potato masher', 'an ice cream scoop', 'a mug', 'a cup of coffee_x', 'a water bottle', 'a sippy cup', 'a baby bottle', 'a wine glass', 'a glass'):
        if name == _n4: t['inhand'] = 4
    if name in ('a compass', 'a thermometer', 'a wallet', 'a credit card', 'a coin', 'money', 'a dictionary', 'a bowl', 'a kettle', 'a plate', 'a vacuum cleaner', 'a nail', 'a sticky note', 'paper', 'a towel', 'toilet paper', 'a napkin', 'soap', 'a balloon', 'a pitcher', 'a tape measure_x'): t['inhand'] = 3 if name in ('a compass', 'a thermometer', 'a credit card', 'a dictionary', 'a vacuum cleaner', 'a kettle', 'a bowl') else 2
    if name in ('a light switch', 'a doorbell', 'a blender', 'a medal', 'a router', 'a hard drive', 'a charger', 'a seatbelt', 'a license plate', 'a sprinkler', 'a coaster', 'a napkin holder', 'a butter dish', 'a placemat', 'a hanger', 'a brick', 'a nest', 'a feather', 'flour', 'vinegar', 'olive oil', 'soy sauce', 'hot sauce', 'a food container', 'a pill bottle', 'an ice cube tray', 'a baking sheet', 'a magnet', 'a battery', 'a jar', 'a pillowcase', 'a postcard', 'a greeting card'): t['inhand'] = 1 if name not in ('a light switch', 'a doorbell', 'a router', 'a hard drive', 'a seatbelt', 'a license plate', 'a sprinkler') else 0
    # "Does it have moving parts?": scissors, a stapler, a bike, a blender, a clock. Not a plate, a vase or a brick.
    MOVP = ('scissors', 'a stapler', 'pliers', 'a clock', 'an alarm clock', 'an umbrella', 'a tape measure', 'a can opener', 'a laptop', 'a door', 'a piano', 'a keyboard',
            'a lock', 'nail clippers', 'a corkscrew', 'a garlic press', 'a hole punch', 'a salad spinner', 'a fan', 'a ceiling fan', 'a printer', 'a blender', 'a mixer',
            'a washing machine', 'a dryer', 'a dishwasher', 'a drill', 'a chainsaw', 'a lawn mower', 'a jack-in-the-box', 'a music box', 'a yo-yo', 'a fidget spinner',
            "a Rubik's cube", 'a windmill', 'a ferris wheel', 'a roller coaster', 'an escalator', 'an elevator', 'a conveyor belt', 'a car jack', 'a tire pump', 'a toaster',
            'a watch', 'a pencil sharpener', 'a staple remover', 'a nutcracker', 'tongs', 'a clothespin', 'a mousetrap', 'a pocket knife', 'a sewing machine', 'a paper shredder',
            'a leaf blower', 'a weed whacker', 'a vacuum cleaner', 'a hair dryer', 'a record player', 'a DVD or Blu-ray player', 'a printer', 'a camera', 'a slot machine',
            'a pinball machine', 'a cash register', 'a vending machine', 'a treadmill', 'a swing', 'a seesaw', 'a rocking chair', 'a hamster wheel', 'a pinwheel', 'a spinning top',
            'a pepper grinder', 'a salt shaker_x', 'a zipper', 'a kaleidoscope', 'a slinky', 'roller skates', 'a skateboard', 'a scooter', 'a stroller', 'a wagon', 'a wheelbarrow',
            'a shopping cart', 'a luggage cart', 'a toy car', 'a toy train', 'a robot', 'a drone', 'a helicopter', 'a garage door_x', 'a gate', 'a mailbox', 'a toilet', 'a faucet',
            'a light switch', 'a doorknob', 'a remote control', 'a computer mouse', 'a game controller', 'a typewriter', 'a calculator_x', 'a fishing rod', 'binoculars', 'a telescope', 'a tripod')
    if name in MOVP or _g('engine') >= 3 or _g('wheels') >= 3: t['parts'] = 4
    elif _g('$made') < 3 or max(_g('eat'), _g('drink'), _g('alive'), _g('place'), _g('body')) >= 3: t['parts'] = 0
    elif _g('appliance') >= 3 and _g('electric') >= 3: t['parts'] = 3
    elif _g('opens') >= 3 and _g('lid') >= 3 or _g('buttons') >= 3 or _g('fold') >= 3 and _g('metal') >= 3: t['parts'] = 2
    else: t['parts'] = 0
    if name in ('an egg', 'a seashell', 'a feather', 'a tooth', 'hair', 'a fingernail'): t['grows'] = max(_g('grows'), 3)
    if name in ('a bell pepper', 'a hot pepper', 'a bagel', 'a tomato', 'a cucumber', 'an onion', 'a zucchini'): t['sliced'] = max(_g('sliced'), 3)
    # "Would it catch fire from a lighter?", re-learned from 400 survey answers (Nov 14). People say yes to far more than paper and wood:
    # plastic melts and burns, gadgets burn, anything with a gas tank burns, soft furniture burns. Only bare metal, stone and glass are a firm no.
    _made = t.get('$made', 0) >= 3 and max(_g('eat'), _g('drink'), _g('alive'), _g('body'), _g('place')) < 3
    if _made and size != 'x':
        _soft = max(_g('wood'), _g('paper'), _g('cloth')) >= 3
        _met = _g('metal') >= 3
        if _soft and not _met: _b = 4                                                     # (a piano, a couch, a kite)
        elif _g('engine') >= 3: _b = 4                                                     # (a car, a lawn mower: gasoline)
        elif _g('plastic') >= 3 and not _met: _b = 4                                       # (a comb, a laundry basket, LEGO)
        elif _g('liquid') >= 3 or _g('hasliquid') >= 3 and max(_g('clean'), _g('grooming')) >= 3: _b = 3   # (glue, lotion, mouthwash; bleach less so)
        elif max(_g('electric'), _g('$electronic')) >= 3 and not _met: _b = 3              # (a camera, a radio, a monitor)
        elif _g('ball') >= 3 or _g('bounce') >= 3: _b = 3                                  # (a football, a basketball)
        elif _met and (_soft or _g('plastic') >= 2 or _g('wood') == 2 or _g('cloth') == 2): _b = 2   # (part metal, part something that burns: a hammer, a rake)
        elif _g('metal') == 2: _b = 2                                                      # (sometimes metal, sometimes not: a chair, a paddle)
        elif _met and max(_g('handle'), _g('wear'), _g('wheels')) >= 3: _b = 2             # (a knife, a pot, a bracelet: people often say sometimes)
        elif _met or max(_g('glass'), _g('rock')) >= 3: _b = 0                             # (a key, a nail, a jar, a brick)
        else: _b = 2
        t['burn'] = _b
    for k, v in fixes_for(name, globals().get('DISPLAY', {}).get(name)).items(): t[k] = v   # (plain facts the rules missed: art/fixes.py)
    # (things that fold or roll up, like a tarp or a blanket: smaller than a case of beer folded, bigger opened out, so "sometimes")
    if t.get('fold', 0) >= 3 and size != 'x' and size >= 2 and max(t.get('furniture', 0), t.get('$hard', 0), t.get('metal', 0)) < 3 \
            and max(t.get('cloth', 0), t.get('paper', 0), t.get('plastic', 0), t.get('soft', 0)) >= 3: t['$microwave'] = 2
    # (Nov 14, from playing: toasters eaten for breakfast, a vape blown into, honey not in the kitchen, a slide "played", a goose not wild)
    if t.get('eat', 0) < 3 and t.get('drink', 0) < 3: t['breakfast'] = 0                       # (only food is eaten for breakfast)
    if (t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3) and t.get('grocery', 0) >= 3 and t.get('alive', 0) < 3: t['kitchen'] = max(t.get('kitchen', 0), 3)
    # "Can it be played?" means an instrument (or a record, a game): not a slide or a bowling pin
    # (Jordan: played = an instrument, a board game, a video game, a movie or a record. Not a bowling pin or a ball.)
    _dn = globals().get('DISPLAY', {}).get(name, name)
    if {name, _dn} & (INSTRUMENTS | GAMES | PLAYED4): t['played'] = 4
    elif {name, _dn} & PLAYS: t['played'] = 3
    elif _dn in ('a baseball cap', 'sneakers', 'a golf cart', 'a zamboni', 'a field', 'a treadmill', 'a headband', 'a stress ball', 'swim goggles', 'a snorkel'): t['played'] = min(t.get('played', 0), 1)
    elif t.get('ball', 0) >= 3: t['played'] = 4                       # (Jordan: a ball can be played)
    elif t.get('sport', 0) >= 3 and _dn not in ('a trophy', 'a medal', 'a water bottle', 'a yoga mat', 'a mouthguard'): t['played'] = 2   # (sports gear: sometimes)
    elif t.get('played', 0) >= 2: t['played'] = 1
    from thin import THIN as _TH
    for _k, _v in _TH.get(_dn, {}).items(): t[_k] = _v   # (gaps filled in on the thinnest things: art/thin.py)
    # (do people ever wash it? pets, farm animals and people yes; wild animals hardly; bugs never)
    if t.get('alive', 0) >= 3 and t.get('plant', 0) < 3 and t.get('body', 0) < 3 and _dn not in ('a person', 'a baby', 'a child'):
        if t.get('insect', 0) >= 3 or _dn in ('a worm', 'a snail', 'a spider', 'a bug', 'a jellyfish', 'a starfish', 'an octopus', 'a seahorse'): t['washable'] = 0
        elif t.get('pet', 0) >= 3: t['washable'] = max(t.get('washable', 0), 3)
        elif t.get('farm', 0) >= 3 or _dn in ('an elephant',): t['washable'] = 2
        else: t['washable'] = 1
    for _k, _v in {**ODDS.get(name, {}), **ODDS.get(_dn, {})}.items(): t[_k] = _v
    from hamster import LIGHT as _HL, BIG as _HB   # (hot dog weight / hamster size, set one by one: art/hamster.py)
    if _dn in _HL: t['$light'] = _HL[_dn]
    if _dn in _HB: t['$small2'] = _HB[_dn]
    from hamster import HEARSE as _HH
    if _dn in _HH: t['$car'] = _HH[_dn]   # (one-off oddities found in the Nov 14 sweep)
    if _dn in WILD or name in WILD: t['wild'] = WILD.get(_dn, WILD.get(name))
    if _dn in NOISE or name in NOISE: t['noise'] = NOISE.get(_dn, NOISE.get(name))
    elif t.get('noise', 0) == 2 and t.get('alive', 0) < 3 and max(t.get('electric', 0), t.get('engine', 0), t.get('music', 0)) < 3: t['noise'] = 1   # (a rock, a ring, a plate: they don't make noise)
    if name in ('a vape',): t['blow'] = 1
    if name in ('a doll', 'an action figure'): t['two_legs'] = 2
    # (clothes: almost all of it can live in a drawer or a closet, in the bedroom. Shoes and coats less often in a drawer.)
    if name in ('a backpack', 'a lanyard', 'an oven mitt', 'a purse'): t['clothes'] = 0
    if t.get('clothes', 0) >= 3:
        _shoe = t.get('feet', 0) >= 3 or name in ('a coat', 'a raincoat', 'a jacket', 'a suit', 'a dress', 'a robe', 'a baseball cap', 'a hat')
        t['drawer'] = max(t.get('drawer', 0), 2 if _shoe else 3)
        if name in ('socks', 'underwear', 'a bra', 'pajamas'): t['drawer'] = 4
        t['bedroom'] = max(t.get('bedroom', 0), 3 if name != 'an apron' else 0)
    for k, v in LEARNED.get(name, {}).items():
        cur = t.get(k, 0)
        t[k] = (4 if cur >= 3 else 3) if v >= 3 else ((0 if cur <= 1 else 1) if v <= 1 else 2)
    # (Nov 14, Jordan: questions that ask a thing about itself are confusing, so either answer is fair)
    if _dn in ('the ocean',): t['ocean'] = 2
    if _dn == 'a beach': t['ocean'] = 1
    if _dn == 'a wave': t['ocean'] = 3
    if _dn == 'a forest': t['forest'] = 2
    if _dn in ('the ocean', 'a lake', 'a river', 'a pond', 'a waterfall', 'a wave', 'rain'): t['$livewater'] = 2
    if _dn in ('a leaf', 'a leaf of kale', 'a basil leaf', 'a mint leaf', 'a leaf of spinach'): t['leaves'] = 2
    if _dn == 'a flower': t['flower'] = 2
    if _dn == 'a seed': t['seeds'] = 2
    # (a pop can, a mug: the drink goes in your mouth, the can or mug only touches it)
    if _dn in ('a pop can', 'a juice box', 'a water bottle', 'a mug', 'a glass', 'a wine glass', 'a bottle', 'a baby bottle', 'a sippy cup', 'a thermos', 'a cup'): t['mouth'] = 2
    # ("would it burn your hand?": hot food or a pan only burns you when it is just cooked or switched on, not sitting on the counter)
    if t.get('hot', 0) >= 2 and 'hot' not in LEARNED.get(name, {}) and _dn not in ('the sun', 'a star', 'lightning', 'fire', 'a campfire'): t['hot'] = 2
    if _dn == 'a hot tub': t['hot'] = 1
    if name == 'a mouthguard': t['played'] = 0   # (Jordan: a mouthguard cannot be played, over the older survey answer)
    if name in ('a tarp', 'a curtain', 'a coat', 'a parachute', 'a shower curtain', 'a garbage bag'): t['$microwave'] = 2   # (folded smaller than a case of beer, opened out bigger: the user's own rule, over older survey answers)
    # (body parts: "could you pick it up?", "would it fit in your pocket?" make no sense for your back or your nose, so neither answer counts against them,
    #  and once he knows it is a body part he stops asking them)
    if t.get('body', 0) >= 3:
        for _k in ('$pickup', '$heavy', 'pocket', '$hold', '$movable', '$duck', '$microwave', '$light', 'shoebox', '$outdoors', '$indoors', 'rolls', 'float', 'envelope', '$steal'): t[_k] = 2
    if (t.get('eat', 0) >= 3 or t.get('drink', 0) >= 3) and 'inhand' not in LEARNED.get(name, {}): t['inhand'] = 2   # (you hold a sandwich or a drink, but is that 'using' it? either answer is fair)
    if boxy(name): t['box'] = 2   # (a cereal box IS a box: "does it come in a box?" can honestly go either way, so neither answer counts against it)
    g = lambda k: t.get(k, 0); up = lambda k, v: t.__setitem__(k, max(g(k), v))
    # round 3: small home things are used at home
    if name in ('a candle', 'a scale', 'a vase', 'a picture frame', 'a mirror', 'a lamp', 'a pillow', 'a blanket', 'a clock', 'a rug', 'a curtain', 'a towel', 'a plant pot_x', 'a light bulb', 'a remote control', 'a box', 'a basket', 'a hanger', 'a bucket', 'a broom'): t['$home'] = 4; up('$household', 4); up('$indoors', 4)
    if name == 'a candle': t['electric'] = 0; t['$electronic'] = 0; t['plugin'] = 0
    if name == 'a scale': t['screen'] = 2; t['battery'] = 2; t['electric'] = 2; t['$electronic'] = 2; t['buttons_x'] = 0
    # player answers, round 2
    if name in ('a tomato', 'an avocado', 'a pumpkin', 'a cucumber', 'a pepper', 'an eggplant', 'a zucchini', 'an olive', 'a squash'): t['fruit'] = 4; t['veg'] = 2
    if cat == 'A' and g('pet') >= 3: up('$indoors', 4)
    if name == 'a car': up('metal', 4)
    if name in ('a fridge', 'a refrigerator', 'a freezer', 'a stove', 'an oven', 'a washing machine', 'a dryer', 'a dishwasher'): up('metal', 3)
    if name in ('a TV', 'a television', 'a computer', 'a laptop', 'a phone', 'a microwave'): up('metal', 2)
    if cat == 'A' and g('pet') >= 3 and name in ('a dog',): up('dangerous', 3)
    if (g('vehicle') >= 3 and g('engine') >= 3) or name in ('fire', 'a knife', 'a gun', 'a sword', 'an axe', 'a saw', 'a chainsaw', 'scissors', 'a stove', 'lightning', 'a volcano'): up('dangerous', 4)
    if g('ball') >= 3 or name in ('a kite', 'a video game console', 'a yo-yo', 'a frisbee', 'a jump rope', 'a skateboard', 'a puzzle', 'cards', 'a board game', 'dice', 'a balloon', 'bubbles', 'a top'): up('toy', 4)
    if name in ('a door', 'a window', 'a drawer', 'a gate'): t['noise'] = 2
    elif g('vehicle') >= 3 and g('engine') >= 3 or name in ('a phone', 'a dog', 'a cat'): up('noise', 4)
    if (cat == 'A' and g('fur') >= 3) or name in ('bread', 'a pillow', 'a blanket', 'a teddy bear', 'a bun', 'a muffin', 'a marshmallow'): up('soft', 4)
    if name in ('a phone', 'a car', 'a dog', 'a ring', 'a cat', 'a horse', 'a laptop', 'a computer', 'a TV', 'a watch', 'a necklace', 'a house'): up('expensive', 4)
    return t

def matrix():
    keys = [k for k, _ in Q]
    M = []
    for name, cat, size, tags in OBJ:
        t = answers(name, cat, size, tags)
        M.append([t.get(k, 0) for k in keys])
    return M

if __name__ == '__main__':
    used = set()
    for name, cat, size, tags in OBJ:
        for w in tags.split(): used.add(w.lstrip('+~-'))
    keys = set(k for k, _ in Q)
    print(len(OBJ), 'things,', len(Q), 'questions')
    print('names in EXTRA not found:', sorted(EX_UNKNOWN))
    print('tags not asked about:', sorted(u for u in used if u not in keys and not u.endswith('_x')))
    print('questions no thing says yes to:', [k for k, _ in Q if all(r[i] < 3 for r in matrix() for i in [list(keys).index(k)] ) ] if False else '')
    M = matrix(); ks = [k for k, _ in Q]
    for i, k in enumerate(ks):
        n = sum(1 for r in M if r[i] >= 3)
        if n < 3: print('few yes:', k, n)
    long_q = [t for _, t in Q if len(t) > 40]
    print('long questions:', long_q)
    from collections import Counter
    c = Counter(tuple(r) for r in M)
    dup = [OBJ[i][0] for i, r in enumerate(M) if c[tuple(r)] > 1]
    print('identical rows:', dup)
