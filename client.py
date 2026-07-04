from sys import argv

from ursinanetworking import *
from ursina import *
from random import *

from os import _exit

from player import *
from voxel import *
from controls import *
from ProjectResources import *
from ProjectVariables import *


app = Ursina(title="Cave Game | Multiplayer", use_ingame_console=debug, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)
window.fps_counter.enabled = True  
window.color=color.hex("#3BA5FF")

poweredby = Text(f'''CaveGame [By TT0tem4ik22]\npowered by Ursina''', font=project_font, scale=3, origin=(0,0))
poweredby.appear(speed=.05)
poweredby.fade_out(delay=5, duration=1, curve=curve.linear)




client = UrsinaNetworkingClient(argv[1], int(argv[2]))
Easy = EasyUrsinaNetworkingClient(client)

reasons = {111: "No servers found"}

Blocks = {}
Players = {}
PlayersTargetPos = {}
PlayersTargetRot = {}
PlayersTargetSit = {}

selfId = -1

Sit = False

info = Text("", parent=camera.ui, scale=1, font=project_font, position=(-1.15,.45))


def esc():
    client.send_message("onClientDisconnected", client)
    _exit(0)


@client.event 
def onConnectionEstablished():
    ControlHelp = Text(controls_text, color=color.rgb(211,211,211), position=Vec2(0.25, 0.5), font=project_font)
    ControlHelp.appear(speed=.01)
    ControlHelp.fade_out(delay=15, duration=1, curve=curve.linear)



@client.event
def GetTerrainWidth(width):
    global terrain_width
    print(width)
    terrain_width = width


@client.event 
def onConnectionError(Reason):
    print(f"\033[91mConnection error! \033[93mReason: {Reason}\033[0m")
    destroy(player)
    if Reason in reasons:
        NoConnection = Text(f"Connection to {argv[1]}:{argv[2]} error!\nReason: {reasons[Reason]}", parent=camera.ui, font=project_font, color=color.white, scale=3, origin=(0, -2))
    else:
        NoConnection = Text(f"Connection to {argv[1]}:{argv[2]} error!\nReason: {Reason}", parent=camera.ui, font=project_font, color=color.white, scale=3, origin=(0, -2))
    exit_button = Button(
        text="Exit",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.4, 0.1),
        origin_y = 1.4,
        on_click = _exit
    )


@client.event
def GetID(Id):
    global selfId
    selfId = Id 
    print(f"Client ID is: {selfId}")


@client.event 
def GetSeed(seed):
    global level_seed
    level_seed = seed


@Easy.event 
def onReplicatedVariableCreated(variable):
    global client, Blocks
    variable_name = variable.name 
    variable_type = variable.content["type"]
    if variable_type == "voxel":
        voxel_type = variable.content["voxel_type"]
        new_voxel = Voxel(init_texture=voxel_type)
        new_voxel.name = variable_name
        new_voxel.position = variable.content["position"] 
        new_voxel.client = client
        Blocks[variable_name] = new_voxel
        if variable.content["source"] == "client":
            if variable.content['voxel_type'] in stone_sound:
                playSound("stone")
            if variable.content['voxel_type'] in wood_sound:    
                playSound("wood")
            if variable.content['voxel_type'] in grass_sound:
                playSound("dirt")
            if variable.content['voxel_type'] in gravel_sound:
                playSound("gravel")
            if variable.content['voxel_type'] in sand_sound:
                playSound("sand")
            if variable.content['voxel_type'] in amethyst_sound:
                playSound("amethyst")
            if variable.content['voxel_type'] in moss_sound:
                playSound("moss")
            if variable.content['voxel_type'] in water_sound:
                playSound("water")
            if variable.content['voxel_type'] in lava_sound:
                playSound("lava")
    elif variable_type == "player":
        PlayersTargetPos[variable_name] = Vec3(0, 0, 0)
        PlayersTargetSit[variable_name] = False
        PlayersTargetRot[variable_name] = 0
        Players[variable_name] = PlayerRepresentation()
        if selfId == int(variable.content["id"]):
            Players[variable_name].color = color.red 
            Players[variable_name].visible = False


@Easy.event 
def onReplicatedVariableUpdated(variable):
    PlayersTargetPos[variable.name] = variable.content['position']
    PlayersTargetSit[variable.name] = variable.content['sit']
    PlayersTargetRot[variable.name] = variable.content['rot']


@Easy.event 
def onReplicatedVariableRemoved(variable):
    variable_name = variable.name
    variable_type = variable.content['type']
    if variable_type == "voxel":
        voxel_type = variable.content["voxel_type"]
        destroy(Blocks[variable_name])
        del Blocks[variable_name]
        if variable_type in stone_sound:
            playSound("stone")
        if variable_type in wood_sound:    
            playSound("wood")
        if variable_type in grass_sound:
            playSound("dirt")
        if variable_type in gravel_sound:
            playSound("gravel")
        if variable_type in sand_sound:
            playSound("sand")
        if variable_type in amethyst_sound:
            playSound("amethyst")
        if variable_type in glass_sound:
            playSound("glass")
        if variable_type in moss_sound:
            playSound("moss")
        if variable_type in water_sound:
            playSound("water")
        if variable_type in lava_sound:
            playSound("lava")

    elif variable_type == "player":
        print("Deleted player")
        destroy(Players[variable_name])
        del Players[variable_name]
        del PlayersTargetPos[variable_name]


player = Player()

def RandomTP(player=player):
    player.position = (rni(0, terrain_width-1),10,rni(0, terrain_width-1))
    playSound("teleport")

# make inventory here

def input(key):
    global Sit
    if player:
        if key == SET:
            A = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
            E = A.entity 
            if E:
                pos = E.position+mouse.normal
                client.send_message("request_spawn_voxel", {"voxel_type":current_texture, "x":pos[0], "y":pos[1], "z":pos[2]})

        if key == BREAK:
            A = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
            E = A.entity 
            if E and E.breakable:
                client.send_message("request_destroy_voxel", E.name)

        if key == EXIT:
            esc()

        if key == RTP:
            RandomTP()


def update():
    global Sit, ingame_music
    if player:
        if held_keys[SIT]:
            Sit = True
        else:
            Sit = False

        if player.position[1] < -70:
            RandomTP()

        if not ingame_music.playing:
            ingame_music = Audio(f"assets/sounds/music/ingame_music/ingame_music{rni(1,43)}.mp3", loop=False, autoplay=False, pitch=1)
            ingame_music.play()

        info.text = f"""X: {round(player.x, 2)}\nY: {round(player.y, 2)}\nZ: {round(player.z, 2)}\nFPS: {round(1/time.dt, 1)}\nPlaying on {argv[1]}:{argv[2]}\nYou are #{selfId}"""

 

        for p in Players:
            try:
                Players[p].position = PlayersTargetPos[p]
            except Exception as e: print(f"\033[91mError updating player position: \033[93m{e}\033[0m")
            try:
                Players[p].rotation_y = PlayersTargetRot[p]
            except Exception as e: print(f"\033[91mError updating player rotation: \033[93m{e}\033[0m")
            try:
                if PlayersTargetSit[p] == True:
                    Players[p].model = player_sit_model
                else:
                    Players[p].model = player_stand_model
            except Exception as e: print(f"\033[91mError updating player model: \033[93m{e}\033[0m")

        client.send_message("UpdatePosition", player.position)
        client.send_message("UpdateSit", Sit)
        client.send_message("UpdateRot", player.rotation_y)

        Easy.process_net_events()




# a = Text("Test", parent=scene, position = (10, 2, 10))

if debug:
    MemoryCounter()

app.run()
