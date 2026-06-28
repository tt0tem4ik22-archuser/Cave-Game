# Cave Game
#
# By TT0tem4ik22

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursinanetworking import * #for multiplayer when i'm gonna do it



    
def update():
    global current_texture, player, music, menu_music, HB, hand

    if not game_going:
        if not menu_music.playing:
            menu_music = Audio("assets/sounds/music/menu_({0}).mp3".format(rni(0,4)), loop=False, autoplay = True)

    if game_going:
        player.visible = not hand.visible
        HB.visible = True
        if not music.playing:
            music = Audio("assets/sounds/music/music_({0}).mp3".format(rni(0,42)), loop=False, autoplay = True, volume=1)
        #Sit
        if held_keys[SIT]:
            player.camera_pivot.y = 1.80
            player.height = 1.45
            player.speed = 3
            player.model = player_sit_model
        else:
            player.camera_pivot.y = 2.3
            player.height = 1.95
            player.model = player_stand_model

        # Sprint
        if held_keys[SPRINT] and not player.gravity == 0:
            player.speed = 8
        else:
            if not held_keys[SIT]:
                player.speed = 5
            else:
                player.speed = 3

        if held_keys[BREAK] or held_keys[SET]:
            hand.rotation = Vec3(0, 0, 0)
        else:
            hand.rotation = Vec3(10, -310, -45)

        if player.position.y <= -110:
            player.position = (rni(0, generation.terrain_width-1), 10, rni(0, generation.terrain_width-1))
            teleport_sound.play()
            player.grounded = True
        Player_Raycast = raycast(origin=(player.x, player.y+player.height, player.z), direction=(0,1,0), distance=10, debug=debug, ignore=[player])
        #player.y_animate()
        # if Player_Raycast.hit:
        #     #player.start_fall()
        #     print("hit")
        # else:
        #     player.jumping = True
        #fly
        if player.gravity == 0:
            player.speed = 10
            if held_keys['space']:
                player.y += 0.35*35*time.dt
            if held_keys[SIT]:
                player.y -= 0.35*35*time.dt

        PlayerPos.text = """X: {0}\nY: {1}\nZ: {2}\nFPS: {3}\n{4} blocks""".format(round(player.x, 2), round(player.y-4.5+53, 2), round(player.z, 2), round(1/time.dt), len(voxel_list))
            
  
def input(key):    
    global saved_coord, saved_rot, inv_opened_times
    if game_going:
        if key == RTP:
            player.position = (rni(0, terrain_width-1), 10, rni(0, terrain_width-1))
            teleport_sound.play()

        if key == SAVE_COORD:
            saved_coord = (player.position.x, player.position.y, player.position.z)
        if key == LOAD_COORD:
            player.position = Vec3(saved_coord)
            teleport_sound.play()

        if key == FIRST_THIRD_PERSON:
            if camera.x == 0 and camera.z == 0:
                camera.z = -5
                camera.rotation = Vec3(0, 0, 0)
                camera.x = 1
                hand.visible = False
            elif camera.x == 1 and camera.z == -5:
                camera.z = 5
                camera.rotation = Vec3(0, 180, 0)
                camera.x = -1
                hand.visible = False
            else:
                camera.x = 0
                camera.rotation = Vec3(0, 0, 0)
                camera.z = 0
                hand.visible = True

        if key == SAVE_LEVEL:
            save_world()
        if key == LOAD_LEVEL:
            load_world()

        if key == NOCLIP:
            if not player.gravity == 0:
                player.gravity = 0
            else:
                player.gravity = 1

        if key == SHOW_CONTROLS:
            ControlHelp = Text(controls_text, color=color.rgb(211,211,211), position=Vec2(0.25, 0.5), font=nunito)
            ControlHelp.appear(speed=.01)
            ControlHelp.fade_out(delay=15, duration=1, curve=curve.linear)

        if key == PLANT_TREE:
            tree_type = choice(["oak", "birch"])
            tree_cord = generation.createTree(player.position, tree_type)
            player.position.x += 1
            for block in tree_cord:
                voxel = Voxel(texture=block[3], position=(block[0], block[1], block[2]))

        if key == EXIT:
            if inventoryHandler.visible:
                inv_opened_times += 1
            else:
                close_game()
    

# def start_single_game():
#     global game_going, player, PlayerPos, voxel, curr_block, hand, menu_music, seed, noise, inventoryHandler
    # if seed_input_field.text != "":
    #     seed = int(seed_input_field.text)
    # else:
    #     seed = rni(1, 1000000)
seed = 100
generated_terrain = generation.genTerrain(seed=seed, advanced=not debug)
for block in generated_terrain:
    voxel = Voxel(texture=block[3], position=(int(block[0]), int(block[1]), int(block[2])))

player = FirstPersonController(position=(generation.terrain_width//2, generation.start_player_y, generation.terrain_width//2), model=player_stand_model, scale=0.65, texture=models_texture)
player.jump_height = 1.5
player.mouse_sensitivity = Vec2(120, 120)
player.gravity = .5  
camera.fov = 120
camera.clip_plane_far = 160

scene.fog_density = (10,95)
scene.fog_color = color.white

player.cursor.texture=cursor_texture
player.cursor.scale=0.08
player.cursor.rotation = 0
player.cursor.color=color.rgb(200,200,200) 

curr_block = UI.CurrentBlock()
hand = UI.Hand()

inventoryHandler = inventory.InventoryHandler()

PlayerPos = Text("", color=color.rgb(211,211,211), position=Vec2(-0.85, 0.45), font=nunito)
ControlHelp = Text(controls_text, color=color.rgb(211,211,211), position=Vec2(0.25, 0.5), font=nunito)

poweredby = Text('''CaveGame [By TT0tem4ik22]\npowered by Ursina\n\nSeed = {0}'''.format(seed), font=nunito, scale=3, origin=(0,0))
poweredby.appear(speed=0.025)
poweredby.fade_out(delay=5, duration=1, curve=curve.linear)

ControlHelp.appear(speed=.01)
ControlHelp.fade_out(delay=15, duration=1, curve=curve.linear)

sun = DirectionalLight(shadow_map_resolution=(2048,2048))
sun.look_at(Vec3(1,-1,-1))

if debug:
    sun._light.show_frustum()
    
    # destroy(single_start_button)
    # destroy(exit_button)
    # destroy(logo)
    # destroy(pre_multiplayer_button)
    # destroy(seed_input_field)
    # destroy(seed_text)

    menu_music.stop(destroy=True)
    game_going = True


def pre_multiplayer_game():
    multiplayer_unavaiable = Text("Multiplayer is unavaiable right now", font=nunito, scale=2.5, origin=(0,0), position=(0,-0.35), color=color.rgb(230,230,230))
    multiplayer_unavaiable.appear(speed=.01)
    multiplayer_unavaiable.fade_out(delay=3, duration=1, curve=curve.linear)


def close_game():
    rmtree("models_compressed")
    quit()

HB = UI.HB

#Menu.InitMainMenu()

# seed_text = Text("Input seed\nSingleplayer only", parent=camera.ui, font=nunito, color=color.white, scale=1, origin=(0, 2), position=(.5, .26))
# seed_input_field = InputField(
#     y=.1,
#     x=.5,
#     limit_content_to="0123456789",
#     max_lines=1, 
#     color=color.gray
#     )
# single_start_button = Button(
#     text="Start Singleplayer Game",
#     color = color.hex("#808080"),
#     highlight_color = color.hex("#666666"),
#     scale=(0.4, 0.1),
#     origin_y = -1,
#     on_click = start_single_game
#     )

# exit_button = Button(
#     text="Exit",
#     color = color.hex("#808080"),
#     highlight_color = color.hex("#666666"),
#     scale = (0.4, 0.1),
#     origin_y = 1.4,
#     on_click = close_game
#     )

# pre_multiplayer_button = Button(
#     text="Start Multiplayer Game",
#     color = color.hex("#808080"),
#     highlight_color = color.hex("#666666"),
#     scale = (0.4, 0.1),
#     origin_y = 0.2, 
#     on_click = pre_multiplayer_game
#     )
logo = Text("Cave Game", parent=camera.ui, font=nunito, color=color.white, scale=5, origin=(0, -2))

app.run()