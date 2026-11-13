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

def fixes_for(name, shown=None):                               # the corrections for a thing, by its own name or the name he says
    out = dict(FIX.get(_bare(shown), {})) if shown else {}
    out.update(FIX.get(_bare(name), {}))
    return out
