# Corrections found in the Nov 13 review: plain facts the tag rules had missed (a basketball is a ball, the moon glows,
# a glass of water is made of glass, a phone has buttons, an alarm clock rings...). One line per question:
# "name" = yes, "name:3" usually, ":2" sometimes, ":1" rarely, ":0" no. _ stands for a space; leave off a / an / the.
# A name may be the thing's own name or the name Zandor says ("water" or "glass of water"). Applied before the
# survey answers, so a real player's answer still has the last word.
SPEC = {
 'ball': 'basketball tennis_ball bowling_ball stress_ball:3 marble:2 hockey_puck:1',
 'feet': 'ice_skates snowboard:2 skateboard:1',
 'rings': 'alarm_clock smartwatch:3 air_fryer:3 toaster_oven:3 cash_register:3 elevator:3 tablet:3 walkie-talkie:3 dryer:2 oven:2 washing_machine:2 dishwasher:2 baby_monitor:2 rice_cooker:2 bicycle:2 computer:2 laptop:2 gps:2',
 'battery': 'robot:3 golf_cart:3 toy_car:2 car:2 drill:3 wheelchair:2 clock:3 alarm_clock:2 headphones:3 computer_mouse:3 keyboard:2 toy_train:2 scale:2 thermometer:2 doorbell:2 thermostat:2 video_game_console:0 speaker:2',
 'appliance': 'kettle air_conditioner heater:3 iron:3 humidifier:3 fan:2 hair_dryer:2 tv:2 dvd_or_blu-ray_player:2 sewing_machine:2',
 'weapon': 'fly_swatter:3 fishing_hook:3 boxing_glove:2 pocket_knife:2 dart:2 water_gun:2 chainsaw:1',
 'plugin': 'battery:0 headphones:1 usb_stick:1 keyboard:2 computer_mouse:1 microphone:2 drill:2 hard_drive:2 robot:2 light_bulb:2 phone:2 tablet:2 smartwatch:1 vape:2',
 'screen': 'camera:3 alarm_clock:3 parking_meter:3 label_maker:3 microwave:2 thermostat:2 vending_machine:2 scale:2 video_game_console:2 baby_monitor:3 watch:1 dvd_or_blu-ray_player:1 projector:1',
 'internet': 'tv:3 video_game_console printer:3 vr_headset webcam:2 baby_monitor:2 thermostat:2 doorbell:2 robot:2 drone:2 camera:2 gps:2 speaker:2',
 'music': 'phone:3 computer:2 tablet:2 laptop:2 whistle:2 tv:1 wind_chime:2',
 'pairs': 'dice:3 grapes:0 cherry:1 peas:0 safety_goggles:0 swim_goggles:0',
 'hot': 'blender:0 mixer:0 hot_sauce:1 thermos:2 vape:2',
 'sharp': 'elbow:0',
 'vehicle': 'ice_skates:1',
 'wear': 'shoulder:0 diamond:2',
 'buttons': 'phone:3 dishwasher dryer stove:3 oven:3 toaster_oven:3 rice_cooker:3 slow_cooker:3 smartwatch:3 hair_dryer:3 fan:3 heater:3 air_conditioner:3 hand_dryer:3 parking_meter:3 coat:3 jeans:3 projector:3 monitor:3 flashlight:3 baby_monitor:3 vr_headset:3 humidifier:3 ring_light:3 vape:3 jacket:2 toaster:2 gps:2 tablet:2 watch:2 record_player:2 router:2 drill:2 paper_shredder:2 hearing_aid:2 leaf_blower:2 camera:4 car:3 treadmill',
 'talk': 'webcam:3 tablet:2 laptop:2 computer:2 smartwatch:2 baby_monitor:2',
 'write': 'coloring_book:3 keyboard:2 clipboard:2 protractor:2 ruler:2',
 'read': 'billboard stop_sign license_plate:3 poster:3 phone:3 tablet:3 bulletin_board:3 whiteboard:3 chalkboard:3 sticky_note:3 notebook:3 smartwatch:3 gps:3 monitor:3 laptop:3 cereal_box:2 id_card:2 computer:2 clock:2 thermometer:2 scale:2 tape_measure:2 ruler:2 sheet_of_paper:2 parking_meter:2 watch:2 compass:2 calculator:2 coloring_book:1 photo_album:1 credit_card:1 tv:1',
 'light': 'moon laptop tablet monitor smartwatch motorcycle taxi pickup_truck school_bus van garbage_truck snowmobile atv subway camper computer:3 alarm_clock:3 gps:3 vr_headset:3 robot:3 drone:3 tractor:3 zamboni:3 forklift:3 helicopter:3 cruise_ship:3 video_game_console:2 baby_monitor:2 smoke_alarm:2 doorbell:2 oven:2 treadmill:2 cash_register:2 parking_meter:2 elevator:2 golf_cart:2 stove:2 ceiling_fan:2 bicycle:1 calculator:1 charger:1 keyboard:1 clock:1 security_camera:1',
 'clean': 'dish_rack:2 dryer_sheet:2 garbage_can:2 bucket:2 hose:2',
 'cook': 'kettle:3 peeler:3 kitchen_timer:3 flour sugar:3 salt butter egg:3 garlic onion:3 ginger:3 soy_sauce:3 vinegar:3 aluminum_foil:3 can_opener:2 pizza_cutter:2 coffee_maker:2 bowl:2 hot_sauce:2 measuring_cup:3',
 'eatwith': 'baby_bottle thermos:3 water_bottle:3 teapot:2 pitcher:2 napkin:2 pop_can:2 juice_box:2 bottle:2 placemat:2 tongs:2 lunchbox:2 toothpick:2 bib:2 table:2',
 'tool': 'flashlight:3 ruler:3 letter_opener:3 snow_brush:3 leaf_blower:3 weed_whacker:3 lawn_mower:3 needle:3 potato_masher:3 broom:2 mop:2 calculator:2 whisk:2 fly_swatter:2 lint_roller:2 scrub_brush:2 hose:2 bucket:2 sewing_machine:2 toolbox:2 compass:2 thermometer:2 scale:2 label_maker:2',
 'glass': 'kaleidoscope:2 glass_of_water glass_of_milk glass_of_orange_juice glass_of_lemonade glass_of_apple_juice glass_of_iced_tea glass_of_soda bottle_of_wine bottle_of_beer:3 house school restaurant church:3 car bus taxi van truck pickup_truck school_bus ambulance fire_truck police_car garbage_truck camper train:3 subway:3 airplane:3 helicopter:3 tractor:2 boat:2 tv:3 phone:3 tablet:3 monitor:3 smartwatch:3 watch:3 clock:3 camera:3 microwave:3 oven:3 flashlight:3 lamp:3 street_light:3 traffic_light:3 webcam:3 security_camera:3 vr_headset:2 cookie_jar:3 medicine_cabinet:3 shower:3 gps:3 projector:3 pitcher:3 measuring_cup:3 laptop:2 door:2 coffee_table:2 cabinet:2 butter_dish:2 thermostat:2 scale:2 teapot:2 bottle:3 jar_of_jam:3 jar_of_peanut_butter:2 jar_of_honey:3 jar_of_salsa:3 jar_of_mayonnaise:2 bottle_of_hot_sauce:3 bottle_of_soy_sauce:3 bottle_of_vinegar:3 bottle_of_olive_oil:3 bottle_of_maple_syrup:3 bottle_of_ketchup:2 mug:1 skyscraper',
 # what things are made of (131 man-made things had no material at all), and whether they are hard
 'metal': 'cruise_ship forklift chainsaw ski_pole hockey_net rake:3 pencil_sharpener:3 sprinkler:3 seesaw:3 lawn_chair:3 stroller:3 wagon:3 dart:3 billboard:3 trampoline:3 weed_whacker:3 tire_pump:3 jack-in-the-box:3 shed:3 jet_ski:2 clipboard:2 fishing_rod:2 tennis_racket:2 briefcase:2 suitcase:2 belt:2 first_aid_kit:2 leaf_blower:2 watering_can:2 paint_roller:2 skis:2 pool_table:2 fountain:2',
 'plastic': 'bottle_of_glue bottle_of_dish_soap jug_of_detergent jug_of_bleach tube_of_toothpaste bottle_of_shampoo bottle_of_lotion bottle_of_sunscreen bottle_of_mouthwash pack_of_dental_floss:3 tube_of_lipstick:3 makeup_kit:3 sprinkler:3 sandbox:3 lawn_chair:3 stroller:3 snowboard:3 spinning_top:3 dollhouse:3 chess_set:3 domino:3 mask:3 jet_ski:3 suitcase:3 clipboard:3 whiteboard:3 pencil_sharpener:3 pencil_case:3 first_aid_kit:3 watering_can:3 leaf_blower:3 weed_whacker:3 kaleidoscope:3 tub_of_play_dough:3 loofah:3 paint_roller:3 fishing_rod:3 golf_ball:3 bowling_ball:3 piggy_bank:2 q-tip:2 wagon:2 life_jacket:2 board_game:2 surfboard:2 skis:2 ski_pole:2 tennis_racket:2 coaster:2 tire_pump:2 jack-in-the-box:2 flower_pot:2 feather_duster:2 mop:2 rake:2 ball:2 yoga_mat:2 dart:2 soccer_ball:1 basketball:1 volleyball:1 football:1 mouse_pad:1 bungee_cord:1 pool_noodle:1 hair_tie:1 earplugs:1 stress_ball:1 hockey_net:1',
 'wood': 'pool_table basket:3 shed:3 sandbox:3 dollhouse:3 chess_set:3 bulletin_board:3 jewelry_box:3 wall:3 chalkboard:2 clipboard:2 seesaw:2 domino:2 painting:2 incense_stick:2 mop:2 rake:2 spinning_top:2 wagon:2 dreamcatcher:2 ceiling:2 feather_duster:2 coaster:2 board_game:1 paint_roller:1 dart:1 lawn_chair:1 tennis_racket:1',
 'paper': 'board_game:3 present:3 firework:3 bag_of_flour:3 billboard:3 painting:2 q-tip:2 mask:2 kaleidoscope:2 bandage:1 dryer_sheet:1 incense_stick:1 jack-in-the-box:1',
 'cloth': 'bean_bag_chair mop:3 suitcase:3 trampoline:3 sneakers:3 bandage:3 life_jacket:3 mask:3 mattress:3 cotton_ball:3 dryer_sheet:3 pencil_case:3 mouse_pad:3 bungee_cord:3 dreamcatcher:3 stroller:3 lawn_chair:3 hockey_net:3 hair_tie:3 tennis_ball:3 painting:3 wallet:2 belt:2 boxing_glove:2 loofah:2 pool_table:2 briefcase:2 baseball:2 jump_rope:2 first_aid_kit:2 sponge:1 yoga_mat:1 feather_duster:1 hot_water_bottle:1 jewelry_box:1',
 '$hard': 'toilet bathtub forklift cruise_ship jet_ski chainsaw brick pebble boulder bowling_ball golf_ball hockey_puck urinal chalkboard whiteboard billboard sidewalk road wall ceiling fountain chimney shed pool_table domino chess_set dart ski_pole skis snowboard seesaw sprinkler wagon flower_pot birdbath leaf_blower weed_whacker tire_pump watering_can jewelry_box kaleidoscope spinning_top rake clipboard pencil_sharpener piggy_bank:3 surfboard:3 stroller:3 hockey_net:3 tennis_racket:3 baseball:3 coaster:3 crayon:3 candle:3 bar_of_soap:3 stick_of_chalk:3 pill:3 dollhouse:3 paint_roller:3 fishing_rod:3 suitcase:3 briefcase:3 firework:3 first_aid_kit:3 jack-in-the-box:3 bulletin_board:3 basketball:3 soccer_ball:3 tire:3 incense_stick:3 volleyball:2 football:2 trampoline:2 snowman:2 sponge:0 cotton_ball:0 loofah:0 bean_bag_chair:0 dryer_sheet:0 earplugs:0 hair_tie:0 rubber_band:0 whoopee_cushion:0 bandage:0 stress_ball:1 pool_noodle:1 mattress:1 yoga_mat:1 mouse_pad:1 hot_water_bottle:1 feather_duster:1 life_jacket:1 boxing_glove:1 wallet:1 belt:1 sneakers:1 mop:1 mask:1 tennis_ball:1 bungee_cord:1 jump_rope:1 dreamcatcher:1 pencil_case:1',
}

# Nov 13: a light switch was being guessed as an outlet (the switch's entry was thin: not white, not in every home, not used today...)
for _k, _v in {
 'white': 'light_switch:3', '$indoors': 'light_switch', 'everyday': 'light_switch', '$household': 'light_switch', '$home': 'light_switch',
 'hardware': 'light_switch outlet', 'plugin': 'light_switch:0 outlet:1', 'cord': 'light_switch:0 outlet:0', 'hang': 'light_switch:1 outlet:1',
 'dangerous': 'light_switch:1 outlet:3', '$movable': 'light_switch:1 outlet:1', 'light': 'light_switch:1',
}.items(): SPEC[_k] = (SPEC.get(_k, '') + ' ' + _v).strip()
SPEC['buttons'] = SPEC['buttons'].replace(' light_switch', '') + ' light_switch outlet:1'

# Nov 13: a TV remote was guessed as a webcam (the remote's entry said it would not fit in a pocket, and was often outdoors)
for _k, _v in {
 'pocket': 'remote_control:3', '$outdoors': 'remote_control:0', '$bring': 'remote_control:1', 'black': 'remote_control:3',
 'info': 'remote_control:0', 'rings': 'remote_control:0', 'drawer': 'remote_control:2', 'bedroom': 'remote_control:3',
 'withpc': 'remote_control:0', 'office2': 'remote_control:1', 'smooth': 'remote_control:3', 'hardware': 'remote_control:1',
}.items(): SPEC[_k] = (SPEC.get(_k, '') + ' ' + _v).strip()

# Nov 14: "Does almost every home have one?" had been yes for any made thing kept indoors (489 things, a jack-in-the-box among them).
# The everyday ones stay yes; these are the realistic answers for the rest. 0 none (a urinal), 1 almost none, 2 some, 3 most.
for _v, _names in {0: """hand_dryer urinal""",
 1: """water_cooler hamster_wheel scratching_post jack-in-the-box kaleidoscope whoopee_cushion pinata snorkel hearing_aid piano rocking_chair crib fish_tank high_chair nutcracker label_maker paper_shredder letter_opener protractor lanyard bottle_of_white-out stylus dumbbell
       dvd_or_blu-ray_player baby_monitor fidget_spinner stress_ball incense_stick sewing_machine safety_goggles feather_duster wind_chime pool_noodle
       hot_water_bottle humidifier dog_bed thimble ashtray swim_goggles security_camera bean_bag_chair baby_gate safe coloring_book tub_of_play_dough
       toy_block bubble_wand glow_stick bubble_wrap ring_light vr_headset tripod inhaler hourglass music_box dreamcatcher mouthguard vape loofah shower_cap
       bath_bomb rubber_duck piggy_bank bib diary picnic_table bench filing_cabinet water_heater_x""",
 2: """waffle_iron rice_cooker slow_cooker air_fryer mixer freezer wok salad_spinner garlic_press potato_masher butter_dish cookie_jar napkin_holder serving_tray
       placemat kitchen_timer chip_clip coffee_filter juice_box pizza_box dishwasher_pod candy_wrapper tack_or_pin staple_remover mouse_pad webcam pencil_case
       bookmark ironing_board lint_roller doorstop dryer_sheet snow_brush dvd_or_blu-ray watering_can fly_swatter jewelry_box photo_album earplugs shoe_rack
       zip_tie sticker christmas_stocking cotton_ball nail_file bobby_pin can_of_hairspray teddy_bear makeup_kit curling_iron tube_of_lipstick wine_glass
       corkscrew pitcher teapot ice_cream_scoop funnel toaster_oven lawn_chair coat_rack nightlight sheet_of_sandpaper apron quilt tablecloth binder poster
       garden barbecue_x""",
 3: """ice_cube_tray dish_rack cereal_box egg_carton milk_carton scrub_brush phone_case id_card keychain power_bar air_freshener flower_pot furnace bra
       first_aid_kit medicine_cabinet towel_rack hand_sanitizer pill_bottle colander peeler grater measuring_cup whisk ladle baking_sheet staircase bath_mat
       scale robe tea_bag fire_extinguisher bookshelf desk vase candle""",
 4: """food_container zip-top_bag water_heater shower_head toilet_brush closet plunger dresser"""}.items():
    SPEC['$household'] = (SPEC.get('$household', '') + ' ' + ' '.join(n + ':' + str(_v) for n in _names.split() if not n.endswith('_x'))).strip()
# ...and a second pass (Nov 14): "sometimes" had become a catch-all, even for an escalator. Things you only see out in the world are no;
# things plenty of homes have but plenty don't are "rarely" or "sometimes"; things nearly everyone has are yes. (Later entries win.)
for _v, _names in {0: """cow pig chicken turkey crab lobster traffic_light crane elevator escalator sidewalk road stop_sign street_light fire_hydrant parking_meter
       billboard vending_machine exit_sign mannequin cash_register price_tag dock buoy conveyor_belt hockey_net statue slide seesaw chalkboard windshield
       steering_wheel license_plate bowling_pin pole braces surfboard""",
 1: """sandbox hot_tub chandelier stethoscope syringe dartboard bowling_ball golf_club hockey_puck medal cigarette treehouse doghouse birdhouse barrel crate
       sign wheel fishing_hook life_jacket ski_pole skis hula_hoop gate fireplace trampoline hammock wheelbarrow chainsaw crowbar drone projector walkie-talkie
       gps binoculars compass contact_lenses pacifier baby_bottle sippy_cup rattle car_seat diaper litter_box birdcage yoga_mat treadmill record_player whiteboard
       chalk hard_drive globe mask party_hat pinwheel handrail golf_ball dart boxing_glove fishing_rod snow_globe ukulele xylophone recorder violin flute
       trumpet drum harmonica telescope microphone robot trophy tent_x hockey_stick_x lobster sushi_x a_x shed_x""",
 2: """dog_bowl leash shed tent sleeping_bag lawn_mower hockey_stick coat_rack fence chimney garage backyard speaker dishwasher blender chopsticks lunchbox
       rolling_pin pizza_cutter ice_pack hot_sauce toothpick robe fire_extinguisher telephone monitor printer cd lighter can_of_hairspray computer wine_glass
       tie lock ruler stapler paper_clip safety_pin needle button nail ceiling_fan heater glasses lemon passport suitcase_x tablet game_controller video_game_console
       guitar ladder drill toolbox wrench pliers tape_measure glue hose rake shovel paintbrush basketball soccer_ball football baseball_bat tennis_ball""",
 3: """tv book pencil tape battery flashlight doorbell jacket coat jeans sweater hat sneakers belt gloves hammer screwdriver bleach laptop headphones water_bottle
       envelope notebook backpack suitcase money credit_card mailbox freezer apple banana potato onion carrot garlic basket washing_machine dryer toaster kettle
       mop bathtub iron tongs salt_shaker soap_dispenser honey soy_sauce olive_oil pill sunscreen mouthwash doormat router boots shorts hoodie scarf socks_x""",
 4: """door window phone key paper pen scissors smoke_alarm doorknob shoe garbage_bag charger calendar light_switch outlet wallet"""}.items():
    SPEC['$household'] = (SPEC.get('$household', '') + ' ' + ' '.join(n + ':' + str(_v) for n in _names.split() if not n.endswith('_x'))).strip()
for _v, _names in {1: """flag chain brick pebble stamp car_jack workbench weed_whacker leaf_blower gas_can tire_pump pocket_knife level glue_gun axe whistle name_tag briefcase
       door_chain slinky puppet net dollhouse webcam roller_skates tennis_racket balloon""",
 3: """coin rubber_band pop_can marker lip_balm extension_cord thermometer"""}.items():
    SPEC['$household'] = (SPEC.get('$household', '') + ' ' + ' '.join(n + ':' + str(_v) for n in _names.split() if not n.endswith('_x'))).strip()

def _bare(n):
    n = n.lower()
    for p in ('a ', 'an ', 'the '):
        if n.startswith(p): return n[len(p):]
    return n

FIX = {}                                                       # bare name -> {question: answer}
for _k, _s in SPEC.items():
    for _w in _s.split():
        _n, _, _v = _w.partition(':')
        FIX.setdefault(_n.replace('_', ' '), {})[_k] = int(_v) if _v else 4

# Nov 13 review: the everyday things he missed most in pretend games had thin entries. Plain facts, thing by thing.
THING = {
 'swing': '$outdoors $indoors:0 metal:2 wood:2 plastic:2 strings:2 vehicle:2 school:2 $heavy:2 $home:1 $household:1 everyday:0 rolls:0 $microwave:4',
 'crowbar': 'garage beltloop:2 fix:3 weapon:1 $heavy:1 dangerous:2 black:2 red:2 sharp:1 $steal:1 $outdoors:1 $indoors:2 hit:1',
 'binder': 'colorful:3 opens container:3 flat:3 $bring:2 info:3 read:2 drawer:1 $home:3 $household:3 hole:1 $indoors $outdoors:0',
 'globe': '$indoors decor:2 gift:2 plastic:3 metal:2 writing read:2 rolls:1 info:3 $home:2',
 'ice cube tray': 'plastic water:3 wet:3 washable seethrough:2 white:2 hasliquid:2 grocery:2 hardware:1',
 'seatbelt': 'wear:3 cloth:3 black:3 plastic:2 metal:2 buttons:2 $indoors:0 $outdoors:1 travel:2 everyday:3 $home:0 $household:0 public:3 fold:2 $steal:0 dangerous:0',
 'bowling pin': '$outdoors:0 $indoors plastic:3 wood:2 smooth shiny:3 red:3 stripes:3 set game:2 $pound throw:0 hit:1 payuse:2',
 'toy train': '$indoors metal:2 colorful:3 electric:2 battery:2 rolls:3 gift:3 baby:2 noise:2 long:2 floor:2',
 'pinwheel': 'moves:2 long:3 round:2 $outdoors:3 beach:2 paper:2 cute:2 gift:1 wood:1',
 'shopping bag': 'plastic:3 paper:2 cloth:2 grocery:3 writing:3 float:2 $indoors:2 $outdoors:2 kitchen:2 $household $home everyday:3 $pound:0 $light:3 soft:2',
 'air freshener': 'hasliquid:3 tube:3 plugin:2 electric:1 drugstore:3 hardware:2 colorful:2 bathroom kitchen:2 bedroom:2 everyday:2 wall:2',
 'dress': 'lower:3 soft:3 gift:2 bedroom:3 $household:3 $home:3 selfsee:3 expensive:2',
 'thermos': 'metal hasliquid:3 eatwith:3 $bring:3 school:2 camping:3 long:2 lid shiny:3 kitchen:3 dangerous:0 $indoors:2 $outdoors:2 smooth:3 everyday:2 $home:3',
 'paintbrush': 'write:3 wood:3 soft:1 metal:2 school:3 wet:3 washable colorful:2 garage:3 drawer:2 $home:3 $household:2',
 'tennis racket': 'metal:2 plastic:2 garage:3 team:0 hit:1 long:2 round:2 gift:2',
 'helmet': 'round:3 shiny:2 garage:2 dangerous:0 selfsee:1',
 'statue': '$outdoors:3 rock:2 metal:3 decor face:3 $pickup:1 $movable:0 scary:2 cold:2',
 'ukulele': 'noise gift:3 handle:2 long:2 $indoors:3 fragile:2 brown:3',
 'net': 'water:2 cloth:2 plastic:2 metal:2 white:3 garage:2',
 'steering wheel': 'handle:3 plastic:3 black:3 travel:3 $indoors:0 $outdoors:2 everyday:3 public:3 buttons:3 noise:3 $pickup:2 $movable:2',
 'spinning top': 'rolls:2 moves:2 colorful:3 wood:2 metal:1 gift:2 baby:1 game:2 floor:2 blade:1',
 'board game': 'game colorful opens:3 $indoors flat:3 gift writing read:3 school:2',
 'gas can': 'plastic:3 metal:2 dangerous:3 burn:3',
 'birdbath': 'decor:3 rock:3 container:3 round:3 floor:3',
 'workbench': 'wood:3 metal:3 tool:2 furniture:3 flat:3 $indoors:3',
 'doll': 'soft:2 plastic:3 cloth:3 colorful:3 $indoors bedroom baby:3 comfort:3 two_legs:3 $legs:3 scary:2 $home:3',
 'kite': 'paper:2 plastic:3 cloth:2 tail:3 flat:3 beach:3 fragile:2 long:2',
 'drum': 'wood:2 metal:2 plastic:2 school:3 $indoors:3 gift:2 expensive:2',
 'mop': 'kitchen:3 bathroom:2 garage:2 $indoors $household $home wood:2 plastic:3 metal:2 $heavy:1 $pound:3 everyday:1',
 'zipper': 'clothes:2 wear:2 cloth:2 plastic:3 long:3 shiny:2 noise:2 selfsee:3 zipper',
 'wallet': 'brown:3 black:3 cloth:2 flat:3 soft:2 everyday $home $household expensive:2 gift:3 public:3 lower:3 info:2',
 'mailbox': '$outdoors $indoors:0 container writing:2 wood:2 black:2 everyday:2 $home:3 $household:3 handle:2 lid:2',
 'flashlight': 'electric tool:3 long:3 metal:2 black:3 $bring:2 drawer:3 garage:3 handle:2',
 'calendar': 'writing read wall:3 hang:3 info colorful:2 kitchen:3 everyday:3 $household $home desk:3 gift:2 $indoors',
 'candle': 'melt white:3 gift:3 dangerous:2 decor:3 kitchen:2 bedroom:2 bathroom:2',
 'tongs': 'metal long:3 handle:3 eatwith:2 shiny:3 washable $outdoors:2 hardware:2',
 'projector': 'expensive:3 withpc:3 withtv:1 noise:2 plastic:3 white:2 black:2 $pound $heavy:1',
 'an iron': 'plastic:3 handle water:2 hasliquid:2 clean:2 flat:2 dangerous:3 everyday:1 $household $home shiny:2 $pound:3 bedroom:2 $indoors',
 # from a line-by-line read of the 315 things almost every home has
 'jack-in-the-box': 'face:3 handle:3 gift scary:3 metal:3 baby:2',
 'shopping cart': 'handle:4 $indoors:3 $outdoors:3 garage:0 expensive:1 $steal:1 travel:0 $pickup:1 vehicle:3 baby:2 floor:0 hardware:0 money:1 grocery:0 traveller:0 carry:2',
 'luggage cart': 'travel:0 traveller:4 carry:4 vehicle:2 $indoors:3 $outdoors:2 money:1 floor:0',
 'knife': 'metal', 'fork': 'metal', 'refrigerator': 'everyday', 'microwave': 'everyday:3', 'stove': 'everyday:2', 'frying pan': 'everyday:2',
 'shower': 'everyday:3', 'lamp': 'everyday:3 $bring:0', 'clock': 'everyday:2 $outdoors:1', 'curtain': '$hard:0 soft:3 $outdoors:1',
 'picture frame': '$outdoors:0', 'napkin holder': '$outdoors:1', 'doorstop': '$outdoors:1', 'dumbbell': '$outdoors:1', 'vase': '$outdoors:1', 'stool': '$outdoors:1',
 'power bar': '$outdoors:0 office2', 'light switch': 'pocket:0 $outdoors:1', 'outlet': 'pocket:0',
 'jug of detergent': '$indoors $outdoors:0', 'toilet': 'opens:3 lid',
 'broom': 'garage:3 kitchen:3', 'sponge': 'bathroom:2', 'soap dispenser': 'kitchen:3', 'egg carton': '$pound:1',
 'vr headset': '$bring:1', 'fan': '$bring:0', 'alarm clock': '$bring:0', 'piggy bank': '$bring:0', 'hair dryer': '$bring:1',
}
# Twins: pairs he kept mixing up in practice games (Nov 14). Each gets the plain facts that tell it from its twin.
TWINS = {
 'ceiling': 'sky:4 floor:0 hang:0 lower:0', 'wall': 'sky:0 floor:2 hang:0',
 'comic book': 'gift:3 colorful:4 bedroom:3 set:3 money:0 kitchen:0', 'menu': 'money:3 gift:0 bedroom:0 set:0 kitchen:1 $household:1 colorful:2',
 'lake': 'beach:3 swimin:4 farm:1 cold_place:2', 'pond': 'beach:0 swimin:1 farm:3',
 'slow cooker': 'lid:4 glass:3 hasliquid:3 buttons:1 noise:0 plastic:1', 'air fryer': 'lid:0 glass:0 hasliquid:0 buttons:4 noise:3 plastic:4 black:3',
 'cardboard box': 'brown:4 flat:0 garage:3 kitchen:1 writing:2 carry:2', 'pizza box': 'flat:4 kitchen:3 smell:2 garage:0 white:3 brown:2 writing:3',
 'hoodie': 'onhead:2 comfort:3 soft:3 buttons:0 zipper:2 winter:2', 'jacket': 'onhead:0 comfort:1 soft:1 buttons:3 zipper:4 winter:4',
 'shoulder': 'lower:0', 'knee': 'lower:4',
 'doorstop': 'floor:4 water:0 wet:0 $outdoors:0', 'sprinkler': 'water:4 wet:4 $outdoors:4 floor:0',
 'napkin holder': 'cook:0 container:3 flat:0 hot:0 decor:2', 'baking sheet': 'cook:4 hot:3 metal:4 flat:4 container:1',
 'bra': 'bedroom:4 kitchen:0 cook:0 pairs:2', 'apron': 'kitchen:4 cook:4 bedroom:0 pairs:0',
 'iced tea': 'fizzy:0 sweet:3 dangerous:0 cold:4', 'beer': 'fizzy:4 sweet:0 dangerous:2 smell:3',
 'stamp': 'money:3 envelope:4 sticky:3 yellow:0 office2:2', 'sticky note': 'yellow:4 desk:4 office2:4 sticky:4 money:0 envelope:2',
 'nose': 'onhead:4 lower:0 five:0 smell:0', 'toe': 'onhead:0 lower:4 five:4',
 'skirt': 'lower:4 onhead:0', 'bow tie': 'lower:0 black:3 pairs:0',
 'playing cards': 'game:4 set:4 played:4 sticky:0 money:2', 'sticker': 'sticky:4 game:0 played:0 set:2 colorful:4 disposable:3',
 'gate': '$outdoors:4 $indoors:0 seethrough:3 farm:3', 'door': '$indoors:4 seethrough:0 farm:1 handle:4',
 'chocolate': 'gift:3 holiday:3 set:2', 'chocolate bar': 'flat:3 long:2 writing:3 pocket:4',
}
from fill import FILL, BURNFIX, EXTRA
for _n, _s in list(FILL.items()) + list(BURNFIX.items()) + list(THING.items()) + list(TWINS.items()):   # (FILL first: older, surveyed fixes win)
    for _w in _s.split():
        _k, _, _v = _w.partition(':')
        FIX.setdefault(_n, {})[_k] = int(_v) if _v else 4

for _n, _s in EXTRA.items():                                  # (last word: fill.py EXTRA)
    for _w in _s.split():
        _k, _, _v = _w.partition(':'); FIX.setdefault(_bare(_n), {})[_k] = int(_v) if _v else 4
def fixes_for(name, shown=None):                               # the corrections for a thing, by its own name or the name he says
    out = dict(FIX.get(_bare(shown), {})) if shown else {}
    out.update(FIX.get(_bare(name), {}))
    out.update(FIX.get(name.lower(), {}))                       # (a key with its a / an kept, for names that clash: 'an iron')
    return out
