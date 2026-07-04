from ursina import *
from sys import argv
from os import _exit, system
from random import randint as rni
from shutil import rmtree

from ursina.prefabs.pause_menu import PauseMenu

from ProjectVariables import *
from controls import *
from ProjectResources import *
from player import *
from voxel import Voxel
from generation import *
from UI import *


def exit_game():
    rmtree("TEMP")
    rmtree("__pycache__")
    rmtree("models_compressed")
    if not debug:
        system("clear")
    _exit(0)


app = Ursina(title="Cave Game | Singleplayer", use_ingame_console=debug, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)
window.fps_counter.enabled = True  
window.color=color.hex("#3BA5FF")

player = Player()
playerRepresent = PlayerRepresentation()

playerRepresent.visible = False



if argv[1] == "Enabled":
    world = GenTerrain(argv[1], seed, int(argv[3]), int(argv[4]) ,int(argv[5]), argv[6], argv[7], world_size, argv[9])
    seed = int(argv[2])
    world_size = int(argv[8])
else:
    world = GenTerrain("Disabled", 1, 1, 1, 1, "Disabled", "Disabled", 1, "Disabled")
    seed = 0
    world_size = 17

for voxel in world:
    vox=Voxel(position=(voxel[0], voxel[1], voxel[2]), init_texture=voxel[3], client="Generation")
    if vox.init_texture == "bedrock":
        vox.breakable = False 

poweredby = Text(f'''CaveGame [By TT0tem4ik22]\npowered by Ursina\nSeed: {seed}''', font=project_font, scale=3, origin=(0,0))
poweredby.appear(speed=.05)
poweredby.fade_out(delay=5, duration=1, curve=curve.linear)


def RandomTP():
    player.position = (rni(0,world_size-1), 20, rni(0,world_size-1))
    playSound("teleport")


def input(key):
    global current_texture
    if key == SET:
        A = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
        E = A.entity 
        if E:
            pos = E.position+mouse.normal
            if pos == E.position:
                print("WARNING: INTERSECTION BLOCKS")
            Voxel(pos, current_texture, client="Player")
            if current_texture in stone_sound:
                playSound("stone")
            if current_texture in wood_sound:    
                playSound("wood")
            if current_texture in grass_sound:
                playSound("dirt")
            if current_texture in gravel_sound:
                playSound("gravel")
            if current_texture in sand_sound:
                playSound("sand")
            if current_texture in amethyst_sound:
                playSound("amethyst")
            if current_texture in moss_sound:
                playSound("moss")
            if current_texture in water_sound:
                playSound("water")
            if current_texture in lava_sound:
                playSound("lava")

    if key == BREAK:
        Ray = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
        E = Ray.entity 
        if E and E.breakable:
            if E.init_texture in stone_sound:
                playSound("stone")
            if E.init_texture in wood_sound:    
                playSound("wood")
            if E.init_texture in grass_sound:
                playSound("dirt")
            if E.init_texture in gravel_sound:
                playSound("gravel")
            if E.init_texture in sand_sound:
                playSound("sand")
            if E.init_texture in amethyst_sound:
                playSound("amethyst")
            if E.init_texture in glass_sound:
                playSound("glass")
            if E.init_texture in moss_sound:
                playSound("moss")
            if E.init_texture in water_sound:
                playSound("water")
            if E.init_texture in lava_sound:
                playSound("lava")
            destroy(E)

    if key == COPY:
        A = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
        E = A.entity 
        if E:
            current_texture = E.init_texture

    if key == RTP:
        RandomTP()




def update():
    playerRepresent.position = player.position
    playerRepresent.rotation_y = camera.rotation_y
    if player.position[1] <= -110:
        RandomTP()
    exit_button.enabled = application.paused

if debug:
    MemoryCounter()

exit_button = Button(
    text="Exit",
    color = color.hex("#808080"),
    highlight_color = color.hex("#666666"),
    scale=(0.4, 0.1),
    origin = (0, 2),
    position=(0, -0.1),
    on_click = exit_game,
    ignore_paused = True,
)

CurrentBlock()
Hand()

PauseMenu()

app.run()