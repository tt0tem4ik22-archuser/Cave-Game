from ursina import *
from sys import argv
from os import _exit
from random import randint as rni

from ProjectVariables import *
from controls import *
from ProjectResources import *
from player import *
from voxel import Voxel
from generation import *


app = Ursina(title="Cave Game | Singleplayer", use_ingame_console=debug, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)
window.fps_counter.enabled = True  
window.color=color.hex("#3BA5FF")

player = Player()
playerRepresent = PlayerRepresentation()

playerRepresent.visible = False

seed = int(argv[2])
world_size = int(argv[8])

world = GenTerrain(argv[1], seed, int(argv[3]), int(argv[4]) ,int(argv[5]), argv[6], argv[7], world_size)

for voxel in world:
    vox=Voxel(position=(voxel[0], voxel[1], voxel[2]), init_texture=voxel[3])
    if vox.init_texture == "bedrock":
        vox.breakable = False 

poweredby = Text(f'''CaveGame [By TT0tem4ik22]\npowered by Ursina\nSeed: {seed}''', font=nunito, scale=3, origin=(0,0))
poweredby.appear(speed=.05)
poweredby.fade_out(delay=5, duration=1, curve=curve.linear)


def RandomTP():
    player.position = (rni(0,world_size-1), 20, rni(0,world_size-1))
    playSound("teleport")


def input(key):
    if key == EXIT:
        _exit(0)

    if key == SET:
        A = raycast(player.position+(0,2,0), camera.forward, distance=6, traverse_target=scene)
        E = A.entity 
        if E:
            pos = E.position+mouse.normal
            Voxel(pos, current_texture)
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
            if E.init_texture in moss_sound:
                playSound("moss")
            if E.init_texture in water_sound:
                playSound("water")
            if E.init_texture in lava_sound:
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

    if key == RTP:
        RandomTP()


def update():
    playerRepresent.position = player.position
    playerRepresent.rotation_y = camera.rotation_y
    if player.position[1] <= -110:
        RandomTP()

app.run()