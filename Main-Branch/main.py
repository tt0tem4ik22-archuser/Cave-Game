# Cave Game
#
# By TT0tem4ik22


from os import system
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import camera_contrast_shader
from ursina.lights import DirectionalLight
import time

#from ursinanetworking import * #for multiplayer when i'm gonna do it

import json
from shutil import rmtree

from random import randint as rni, choice
from numpy import floor
from perlin_noise import PerlinNoise

from webbrowser import open as webopen


terrain = Entity(model=None, texture=None)
voxel_list = []
inv_opened_times = 0
saved_coord = (0,0,0)
debug = False
game_going = False

# controls
BREAK = "left mouse down"
SET = "right mouse down"
EXIT = "escape"
RTP = "g"
NOCLIP = "v"
SIT = "left shift"
SPRINT = "left control"
SAVE_COORD = "z"
LOAD_COORD = "x"
INV = "e"
INV_CHOOSE = "left mouse up"
FIRST_THIRD_PERSON = "f"
SAVE_LEVEL = "p"
LOAD_LEVEL = "l"
SHOW_CONTROLS = "m"
PLANT_TREE = "n"

time_delta = 0

app = Ursina(title="Cave Game", use_ingame_console=debug, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)
window.fps_counter.enabled = True  

#Resources
#textures
cursor_texture = load_texture("assets/textures/cursor.png")
model_texture = load_texture("assets/textures/models_texture.png")
none_texture = load_texture("no texture found.fuckit")
blocks = ["stone", "weathered copper block", "crimson wood", "dark oak vertical", "birch vertical", "acacia vertical", "crimson vertical", "mangrove vertical", "spruce vertical", "warped vertical", "jungle vertical", "dark oak horisontal", "birch horisontal", "acacia horisontal", "crimson horisontal", "mangrove horisontal", "spruce horisontal", "warped horisontal", "jungle horisontal", "flowering azalea leaves", "dark oak wood", "birch wood", "acacia wood", "crismon wood", "jungle wood", "mangrove wood", "spruce wood", "warped wood", "quartz bricks", "crimson wart", "warped wart", "birch leaves", "spruce leaves", "jungle leaves", "mangrove leaves", "azalea leaves", "acacia leaves", "dark oak leaves", "deepslate coal ore", "deepslate copper ore", "deepslate iron ore", "deepslate gold ore", "deepslate lapis ore", "deepslate redstone ore", "deepslate emerald ore", "deepslate diamond ore",  "deepslate bricks", "cracked deepslate tiles",  "cracked deepslate bricks",  "deepslate",  "oak wood", "magma", "purpur block", "amethyst", "dirt", "spawner", "sponge", "oak vertical", "water", "stone brick", "diorite smooth", "andesite smooth", "granite smooth", "nether gold ore", "red nether bricks", "redstone ore", "redstone block", "sand", "red sand",  "oxidized copper block", "quartz ore", "nether bricks", "netherite block", "oak leaves", "moss", "mossy stone bricks", "mossy cobblestone",  "oak horisontal", "lava", "lapis block", "lapis ore", "obsidian", "quartz", "netherrack", "iron ore", "iron ore block", "iron block", "grass", "granite", "gravel", "glass",  "endstone", "exposed copper block", "gold ore block", "gold block", "gold ore", "endstone bricks", "emerald block", "emerald ore",  "diorite", "crying obsidian",  "diamond block", "diamond ore", "andesite", "bedrock", "chiseled nether bricks", "bricks", "coal block", "coal ore", "cobblestone", "copper block", "copper ore block", "copper ore", "cracked nether bricks"]
blocks_textures = {}
for block in blocks:
    blocks_textures[block] = load_texture(f"assets/textures/blocks/{block}.png")
#sounds
teleport_sound = Audio("assets/sounds/teleport.mp3", loop=False, autoplay = False)
water_sound = Audio("assets/sounds/blocks/water/water{0}.mp3".format(rni(1,2)), loop=False, autoplay=False)
lava_sound = Audio("assets/sounds/blocks/lava/lava{0}.mp3".format(rni(1,2)), loop=False, autoplay=False)
stone_sound = Audio("assets/sounds/blocks/stone/stone{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
wood_sound = Audio("assets/sounds/blocks/wood/wood{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
dirt_sound = Audio("assets/sounds/blocks/dirt/dirt{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
glass_sound = Audio("assets/sounds/blocks/glass.mp3", loop=False, autoplay = False)
gravel_sound = Audio("assets/sounds/blocks/gravel/gravel{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
moss_sound = Audio("assets/sounds/blocksmoss/moss{0}.ogg".format(rni(1,5)), loop=False, autoplay = False)
amethyst_sound = Audio("assets/sounds/blocks/amethyst/amethyst{0}.ogg".format(rni(1,2)), loop=False, autoplay = False)
sand_sound = Audio("assets/sounds/blocks/sand/sand{0}.mp3".format(rni(1,4)), loop=False, autoplay = False)
music = Audio("assets/sounds/music/music_({0}).mp3".format(rni(0,42)), loop=False, autoplay = False, volume=1)
menu_music = Audio("assets/sounds/music/menu_({0}).mp3".format(rni(0,4)), loop=False, autoplay = True)
#models
sword_model = load_model("assets/models/diamond_sword.obj")
player_stand_model = load_model("assets/models/player_stand.obj")
player_sit_model = load_model("assets/models/player_sit.obj")
#font
nunito = "assets/fonts/Nunito.ttf"

Sky(color=color.hex("#3BA5FF"), texture=None)

current_texture = blocks_textures["grass"]


class InventorySection(Button):
    def __init__(self, position, texture):
        super().__init__(
            parent=inventory,
            color=color.white,
            texture=texture,
            position=position,
            scale=0.035
            )

    def input(self, key):
        global current_texture
        if self.hovered and key==BREAK and self.visible == True:
            current_texture = self.texture

    def update(self):
        self.visible = inventory.visible


class InventoryHandler(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.8,0.8),
            color=color.black
        )
    def input(self, key):
        global inv_opened_times, voxel, curr_block, current_texture, blocks_textures
        if game_going:
            if key == INV:
                inv_opened_times += 1

            if inv_opened_times % 2 == 1:
                curr_text.visible = True
                self.visible = True 
                player.cursor.visible = False
                mouse.locked = False
                player.mouse_sensitivity = Vec2(0,0)
            else:
                curr_text.visible = False
                self.visible = False
                player.cursor.visible = True
                mouse.locked = True
                mouse.position = (0,0)
                player.mouse_sensitivity = Vec2(120,120)

    def update(self):
        if inventory.visible == True:
            curr_text.text = [key for key, value in blocks_textures.items() if value == current_texture][0].capitalize()


def InitializeInvintory():
    inv_counter = 0
    inventory = InventoryHandler()
    for y in range(17):
        for x in range(17):
            if inv_counter < len(blocks):
                print(blocks_textures[blocks[inv_counter]])
                texture = blocks[inv_counter]
                section = InventorySection((x/2-4,y/2-4), blocks_textures[blocks[inv_counter]])
                inv_counter += 1
    curr_text = Text("Current texture", font=nunito, scale=2.5, origin=(0,0), position=(0,0), color=color.rgb(230,230,230))
    curr_text.visible = False
    inventory.visible = False

    


    



class CurrentBlock(Entity):
    def __init__(self, texture):
        super().__init__(
                parent=camera.ui, 
                model="quad",
                scale=(0.1,0.1),
                color=color.rgb(230,230,230),
                texture=texture,
                position=Vec2(-0.75, -0.35)
            ) 
    def update(self):
        self.texture = current_texture


class Hand(Entity):
    def __init__(self):
        super().__init__(
                parent=camera.ui,
                model=sword_model,
                scale=(0.2,0.4),
                texture=model_texture,
                rotation=Vec3(15, -310, -45),
                position=Vec2(0.65, -0.35)
        )

    
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=current_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            collider="box",
            origin_y=0,
            texture=texture,
            color=color.white,
            highlight_color = color.light_gray,
            default_shader=lit_with_shadows_shader,
            shader=lit_with_shadows_shader
        )
        voxel_list.insert(len(voxel_list), {'texture': str(texture), 'x': position[0], 'y': position[1], 'z': position[2]})
        

    def input(self, key):
        global current_texture, saved_coord, saved_rot, load_texture, amethyst_sound, moss_sound, water_sound, dirt_sound, sand_sound, stone_sound, wood_sound, voxel_list, gravel_sound, player, time_delta
        if self.hovered:
            if key == SET and not inventory.visible and not current_texture == none_texture and distance(self, player) <= 4:
                voxel = Voxel(position=self.position+mouse.normal, texture=current_texture)
                if voxel.texture == blocks_textures["deepslate gold ore"] or voxel.texture == blocks_textures["deepslate iron ore"] or voxel.texture == blocks_textures["deepslate emerald ore"] or voxel.texture == blocks_textures["deepslate diamond ore"] or voxel.texture == blocks_textures["deepslate lapis ore"] or voxel.texture == blocks_textures["deepslate redstone ore"] or voxel.texture == blocks_textures["deepslate copper ore"] or voxel.texture == blocks_textures["deepslate coal ore"] or voxel.texture == blocks_textures["cracked deepslate tiles"] or voxel.texture == blocks_textures["cracked deepslate bricks"] or voxel.texture == blocks_textures["deepslate bricks"] or voxel.texture == blocks_textures["deepslate"] or voxel.texture == blocks_textures["quartz bricks"] or voxel.texture == blocks_textures["quartz"] or voxel.texture == blocks_textures["purpur block"] or voxel.texture == blocks_textures["magma"] or voxel.texture == blocks_textures["obsidian"] or voxel.texture == blocks_textures["red nether bricks"] or voxel.texture == blocks_textures["endstone"] or voxel.texture == blocks_textures["endstone bricks"] or voxel.texture == blocks_textures["spawner"] or voxel.texture == blocks_textures["mossy stone bricks"] or voxel.texture == blocks_textures["bedrock"] or voxel.texture == blocks_textures["netherite block"] or voxel.texture == blocks_textures["chiseled nether bricks"] or voxel.texture == blocks_textures["cracked nether bricks"] or voxel.texture == blocks_textures["nether bricks"] or voxel.texture == blocks_textures["netherrack"] or voxel.texture == blocks_textures["crying obsidian"] or voxel.texture == blocks_textures["bricks"] or voxel.texture == blocks_textures["diamond block"] or voxel.texture == blocks_textures["emerald block"] or voxel.texture == blocks_textures["iron block"] or voxel.texture == blocks_textures["gold block"] or voxel.texture == blocks_textures["lapis block"] or voxel.texture == blocks_textures["redstone block"] or voxel.texture == blocks_textures["coal block"] or voxel.texture == blocks_textures["copper block"] or voxel.texture == blocks_textures["diamond ore"] or voxel.texture == blocks_textures["emerald ore"] or voxel.texture == blocks_textures["iron ore"] or voxel.texture == blocks_textures["gold ore"] or voxel.texture == blocks_textures["lapis ore"] or voxel.texture == blocks_textures["redstone ore"] or voxel.texture == blocks_textures["coal ore"] or voxel.texture == blocks_textures["copper ore"] or voxel.texture == blocks_textures["stone"] or voxel.texture == blocks_textures["cobblestone"] or voxel.texture == blocks_textures["glass"] or voxel.texture == blocks_textures["stone brick"] or voxel.texture == blocks_textures["nether gold ore"] or voxel.texture == blocks_textures["quartz ore"] or voxel.texture == blocks_textures["copper ore block"] or voxel.texture == blocks_textures["iron ore block"] or voxel.texture == blocks_textures["gold ore block"] or voxel.texture == blocks_textures["weathered copper block"] or voxel.texture == blocks_textures["exposed copper block"] or voxel.texture == blocks_textures["oxidized copper block"] or voxel.texture == blocks_textures["mossy cobblestone"] or voxel.texture == blocks_textures["andesite"] or voxel.texture == blocks_textures["andesite smooth"] or voxel.texture == blocks_textures["diorite"] or voxel.texture == blocks_textures["diorite smooth"] or voxel.texture == blocks_textures["granite"] or voxel.texture == blocks_textures["granite smooth"]:
                    stone_sound.play()
                    stone_sound = Audio("assets/sounds/blocks/stone/stone{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["oak wood"] or voxel.texture == blocks_textures["oak vertical"] or voxel.texture == blocks_textures["oak horisontal"] or voxel.texture == blocks_textures["dark oak wood"] or voxel.texture == blocks_textures["dark oak vertical"] or voxel.texture == blocks_textures["dark oak horisontal"] or voxel.texture == blocks_textures["birch wood"] or voxel.texture == blocks_textures["birch vertical"] or voxel.texture == blocks_textures["birch horisontal"] or voxel.texture == blocks_textures["acacia wood"] or voxel.texture == blocks_textures["acacia vertical"] or voxel.texture == blocks_textures["acacia horisontal"] or voxel.texture == blocks_textures["crimson wood"] or voxel.texture == blocks_textures["crimson vertical"] or voxel.texture == blocks_textures["crimson horisontal"] or voxel.texture == blocks_textures["warped wood"] or voxel.texture == blocks_textures["warped vertical"] or voxel.texture == blocks_textures["warped horisontal"] or voxel.texture == blocks_textures["jungle wood"] or voxel.texture == blocks_textures["jungle vertical"] or voxel.texture == blocks_textures["jungle horisontal"] or voxel.texture == blocks_textures["spruce wood"] or voxel.texture == blocks_textures["spruce vertical"] or voxel.texture == blocks_textures["spruce horisontal"] or voxel.texture == blocks_textures["mangrove wood"] or voxel.texture == blocks_textures["mangrove vertical"] or voxel.texture == blocks_textures["mangrove horisontal"]:
                    wood_sound.play()
                    wood_sound = Audio("assets/sounds/blocks/wood/wood{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["grass"] or voxel.texture == blocks_textures["dirt"] or voxel.texture == blocks_textures["oak leaves"] or voxel.texture == blocks_textures["sponge"] or voxel.texture == blocks_textures["dark oak leaves"] or voxel.texture == blocks_textures["birch leaves"] or voxel.texture == blocks_textures["acacia leaves"] or voxel.texture == blocks_textures["azalea leaves"] or voxel.texture == blocks_textures["flowering azalea leaves"] or voxel.texture == blocks_textures["mangrove leaves"] or voxel.texture == blocks_textures["jungle leaves"] or voxel.texture == blocks_textures["spruce leaves"]:
                    dirt_sound.play()
                    dirt_sound = Audio("assets/sounds/blocks/dirt/dirt{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["gravel"]:
                    gravel_sound.play()
                    gravel_sound = Audio("assets/sounds/blocks/gravel/gravel{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["sand"]or voxel.texture == blocks_textures["red sand"]:
                    sand_sound.play()
                    sand_sound = Audio("assets/sounds/blocks/sand/sand{0}.mp3".format(rni(1,4)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["amethyst"]:
                    amethyst_sound.play()
                    amethyst_sound = Audio("assets/sounds/blocks/amethyst/amethyst{0}.ogg".format(rni(1,2)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["moss"] or voxel.texture == blocks_textures["crimson wart"] or voxel.texture == blocks_textures["warped wart"]:
                    moss_sound.play()
                    moss_sound = Audio("assets/sounds/blocks/moss/moss{0}.ogg".format(rni(1,5)), loop=False, autoplay = False)
                if voxel.texture == blocks_textures["water"]:
                    water_sound.play()
                    water_sound = Audio("assets/sounds/blocks/water/water{0}.mp3".format(rni(1,2)), loop=False, autoplay=False)
                voxel_list.append({'texture': str(voxel.texture), 'x': voxel.position.x, 'y': voxel.position.y, 'z': voxel.position.z})
              
            if key == BREAK and not inventory.visible and not current_texture == none_texture and distance(self, player) <= 4:
                if self.texture == blocks_textures["glass"]:
                    glass_sound.play()
                if self.texture == blocks_textures["deepslate gold ore"] or self.texture == blocks_textures["deepslate iron ore"] or self.texture == blocks_textures["deepslate emerald ore"] or self.texture == blocks_textures["deepslate diamond ore"] or self.texture == blocks_textures["deepslate lapis ore"] or self.texture == blocks_textures["deepslate redstone ore"] or self.texture == blocks_textures["deepslate copper ore"] or self.texture == blocks_textures["deepslate coal ore"] or self.texture == blocks_textures["cracked deepslate tiles"] or self.texture == blocks_textures["cracked deepslate bricks"] or self.texture == blocks_textures["deepslate bricks"] or self.texture == blocks_textures["deepslate"] or self.texture == blocks_textures["quartz bricks"] or self.texture == blocks_textures["quartz"] or self.texture == blocks_textures["purpur block"] or self.texture == blocks_textures["magma"] or self.texture == blocks_textures["obsidian"] or self.texture == blocks_textures["red nether bricks"] or self.texture == blocks_textures["endstone"] or self.texture == blocks_textures["endstone bricks"] or self.texture == blocks_textures["spawner"] or self.texture == blocks_textures["mossy stone bricks"] or self.texture == blocks_textures["bedrock"] or self.texture == blocks_textures["netherite block"] or self.texture == blocks_textures["chiseled nether bricks"] or self.texture == blocks_textures["cracked nether bricks"] or self.texture == blocks_textures["nether bricks"] or self.texture == blocks_textures["netherrack"] or self.texture == blocks_textures["crying obsidian"] or self.texture == blocks_textures["bricks"] or self.texture == blocks_textures["diamond block"] or self.texture == blocks_textures["emerald block"] or self.texture == blocks_textures["iron block"] or self.texture == blocks_textures["gold block"] or self.texture == blocks_textures["lapis block"] or self.texture == blocks_textures["redstone block"] or self.texture == blocks_textures["coal block"] or self.texture == blocks_textures["copper block"] or self.texture == blocks_textures["diamond ore"] or self.texture == blocks_textures["emerald ore"] or self.texture == blocks_textures["iron ore"] or self.texture == blocks_textures["gold ore"] or self.texture == blocks_textures["lapis ore"] or self.texture == blocks_textures["redstone ore"] or self.texture == blocks_textures["coal ore"] or self.texture == blocks_textures["copper ore"] or self.texture == blocks_textures["stone"] or self.texture == blocks_textures["cobblestone"] or self.texture == blocks_textures["glass"] or self.texture == blocks_textures["stone brick"] or self.texture == blocks_textures["nether gold ore"] or self.texture == blocks_textures["quartz ore"] or self.texture == blocks_textures["copper ore block"] or self.texture == blocks_textures["iron ore block"] or self.texture == blocks_textures["gold ore block"] or self.texture == blocks_textures["weathered copper block"] or self.texture == blocks_textures["exposed copper block"] or self.texture == blocks_textures["oxidized copper block"] or self.texture == blocks_textures["mossy cobblestone"] or self.texture == blocks_textures["andesite"] or self.texture == blocks_textures["andesite smooth"] or self.texture == blocks_textures["diorite"] or self.texture == blocks_textures["diorite smooth"] or self.texture == blocks_textures["granite"] or self.texture == blocks_textures["granite smooth"]:
                    stone_sound.play()
                    stone_sound = Audio("assets/sounds/blocks/stone/stone{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if self.texture == blocks_textures["oak wood"] or self.texture == blocks_textures["oak vertical"] or self.texture == blocks_textures["oak horisontal"] or self.texture == blocks_textures["dark oak wood"] or self.texture == blocks_textures["dark oak vertical"] or self.texture == blocks_textures["dark oak horisontal"] or self.texture == blocks_textures["birch wood"] or self.texture == blocks_textures["birch vertical"] or self.texture == blocks_textures["birch horisontal"] or self.texture == blocks_textures["acacia wood"] or self.texture == blocks_textures["acacia vertical"] or self.texture == blocks_textures["acacia horisontal"] or self.texture == blocks_textures["crimson wood"] or self.texture == blocks_textures["crimson vertical"] or self.texture == blocks_textures["crimson horisontal"] or self.texture == blocks_textures["warped wood"] or self.texture == blocks_textures["warped vertical"] or self.texture == blocks_textures["warped horisontal"] or self.texture == blocks_textures["jungle wood"] or self.texture == blocks_textures["jungle vertical"] or self.texture == blocks_textures["jungle horisontal"] or self.texture == blocks_textures["spruce wood"] or self.texture == blocks_textures["spruce vertical"] or self.texture == blocks_textures["spruce horisontal"] or self.texture == blocks_textures["mangrove wood"] or self.texture == blocks_textures["mangrove vertical"] or self.texture == blocks_textures["mangrove horisontal"]:
                    wood_sound.play()
                    wood_sound = Audio("assets/sounds/blocks/wood/wood{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if self.texture == blocks_textures["grass"] or self.texture == blocks_textures["dirt"] or self.texture == blocks_textures["oak leaves"] or self.texture == blocks_textures["sponge"] or self.texture == blocks_textures["dark oak leaves"] or self.texture == blocks_textures["birch leaves"] or self.texture == blocks_textures["acacia leaves"] or self.texture == blocks_textures["azalea leaves"] or self.texture == blocks_textures["flowering azalea leaves"] or self.texture == blocks_textures["mangrove leaves"] or self.texture == blocks_textures["jungle leaves"] or self.texture == blocks_textures["spruce leaves"]:
                    dirt_sound.play()
                    dirt_sound = Audio("assets/sounds/blocks/dirt/dirt{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if self.texture == blocks_textures["gravel"]:
                    gravel_sound.play()
                    gravel_sound = Audio("assets/sounds/blocks/gravel/gravel{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
                if self.texture == blocks_textures["sand"] or self.texture == blocks_textures["red sand"]:
                    sand_sound.play()
                    sand_sound = Audio("assets/sounds/blocks/sand/sand{0}.mp3".format(rni(1,4)), loop=False, autoplay = False)
                if self.texture == blocks_textures["amethyst"]:
                    amethyst_sound.play()
                    amethyst_sound = Audio("assets/sounds/blocks/amethyst/amethyst{0}.ogg".format(rni(1,2)), loop=False, autoplay = False)
                if self.texture == blocks_textures["moss"] or self.texture == blocks_textures["crimson wart"] or self.texture == blocks_textures["warped wart"]:
                    moss_sound.play()
                    moss_sound = Audio("assets/sounds/blocks/moss/moss{0}.ogg".format(rni(1,5)), loop=False, autoplay = False)

                voxel_list.remove({'texture': str(self.texture), 'x': self.position.x, 'y': self.position.y, 'z': self.position.z})
                destroy(self)

    
def update():
    global current_texture, player, leaves_texture, music, dirt_sound, menu_music, time_delta, HB, hand

    #player.visible = not hand.visible

    if not game_going:
        if not menu_music.playing:
            menu_music = Audio("assets/sounds/music/menu_({0}).mp3".format(rni(0,4)), loop=False, autoplay = True)

    if game_going:
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
            player.position = (rni(0, terrain_width-1), 10, rni(0, terrain_width-1))
            teleport_sound.play()
            player.grounded = True
        Player_Raycast = raycast(origin=(player.x, player.y+player.height, player.z), direction=(0,0,0), distance=10, debug=debug, ignore=[player])
        #player.y_animate()
        if Player_Raycast.hit:
            #player.start_fall()
            print("hit")
        else:
            player.jumping = True
        #fly
        if player.gravity == 0:
            player.speed = 10
            if held_keys['space']:
                player.y += 0.35*35*time.dt
            if held_keys[SIT]:
                player.y -= 0.35*35*time.dt

        PlayerPos.text = """X: {0}\nY: {1}\nZ: {2}\nFPS: {3}\n{4} blocks""".format(round(player.x, 2), round(player.y-4.5+53, 2), round(player.z, 2), round(1/time.dt), len(voxel_list))
        if len(voxel_list) == 1:
            print(voxel_list)
        time_delta += 1
            
  
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
            ControlHelp = Text(controls, color=color.rgb(211,211,211), position=Vec2(0.25, 0.5), font=nunito)
            ControlHelp.appear(speed=.01)
            ControlHelp.fade_out(delay=15, duration=1, curve=curve.linear)

        if key == PLANT_TREE:
            tree_type = choice(["oak", "birch"])
            print(f"PLANTED TREE on {player.position} tree_type {tree_type}")
            create_tree(player.position, tree_type)

        if key == EXIT:
            if inventory.visible:
                inv_opened_times += 1
            else:
                close_game()
    

def create_tree(pos, type):
    for i in range(5):
        voxel = Voxel(position=(pos[0],pos[1]+i+1,pos[2]), texture=blocks_textures[f"{type} vertical"])

    voxel = Voxel(position=(pos[0],pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+7,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+7,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+7,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+6,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+5,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+4,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+6,pos[2]-2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+5,pos[2]-2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+4,pos[2]-2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+6,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+5,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+4,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+6,pos[2]+2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+5,pos[2]+2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0],pos[1]+4,pos[2]+2), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+7,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+7,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-2,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-2,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-2,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+2,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+2,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+2,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+4,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+5,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+6,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+4,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+5,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
    voxel = Voxel(position=(pos[0]-1,pos[1]+6,pos[2]-1), texture=blocks_textures[f"{type} leaves"])


def save_world():
    global voxel_list
    try:
        with open('save.save', 'w+') as save:
            save.truncate(0)
            save.write(str(voxel_list))

        saved_text = Text("Level saved succefully...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))

        saved_text.appear(speed=.05)
        saved_text.fade_out(delay=0.75, duration=1, curve=curve.linear)
    except:
        saved_text = Text("Level could not be saved...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))

        saved_text.appear(speed=.05)
        saved_text.fade_out(delay=0.75, duration=1, curve=curve.linear)


def load_world():
    global voxel_list 
    try:
        with open('save.save', 'r') as save:
            voxel_list = json.load(save)
            print(voxel_list)
        """DESTROY ALL EXISTING voxel"""
        for element in voxel_list:
            texture_value = element.get('texture')
            x_value = element.get('x')
            y_value = element.get('y')
            z_value = element.get('z')
            voxel = Voxel(texture=load_texture(f"assets/textures/blocks/{texture_value}"), position=(int(x_value), int(y_value), (z_value)))

        player.position=(0,10,0)
        loaded_text = Text("Level loaded succefully...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))
        loaded_text.appear(speed=.05)
        loaded_text.fade_out(delay=0.75, duration=1, curve=curve.linear)
    except:
        loaded_text = Text("Level could not be loaded...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))
        loaded_text.appear(speed=.05)
        loaded_text.fade_out(delay=1.25, duration=1, curve=curve.linear)


def start_single_game(advanced=not debug):
    global game_going, player, PlayerPos, voxel, curr_block, hand, menu_music, seed, noise, terrain
    
    octaves = 2
    noise = PerlinNoise(octaves=octaves, seed=seed)
    amp = 6
    period = 48
    start_player_y = 7
    #generation
    landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]
    for position in range(terrain_width**2):
        x = floor(position / terrain_width)
        z = floor(position % terrain_width)
        y = floor(noise([x/period, z/period])*amp)
        landscale[int(x)][int(z)] = int(y)
        
        voxel = Voxel(texture=blocks_textures["grass"], position=(x,int(y+7),z))
        if advanced:
            for i in range(4):
                voxel = Voxel(texture=blocks_textures["dirt"], position=(x,int(y+6-i),z))

            for j in range(100):
                random.seed((seed//y-x**z+j**4))
                block = rni(0,1000)
                if j <= 50:
                    if block <= 820:
                        voxel = Voxel(texture=blocks_textures["stone"], position=(x,int(y+2-j),z))
                    if block > 820 and block <= 860:
                        voxel = Voxel(texture=blocks_textures["copper ore"], position=(x,int(y+2-j),z))
                    if block > 860 and block <= 900:
                        voxel = Voxel(texture=blocks_textures["coal ore"], position=(x,int(y+2-j),z))
                    if block > 900 and block <= 935:
                        voxel = Voxel(texture=blocks_textures["iron ore"], position=(x,int(y+2-j),z))
                    if block > 935 and block <= 955:
                        voxel = Voxel(texture=blocks_textures["gold ore"], position=(x,int(y+2-j),z))
                    if block > 955 and block <= 975:
                        voxel = Voxel(texture=blocks_textures["redstone ore"], position=(x,int(y+2-j),z))
                    if block > 975 and block <= 990:
                        voxel = Voxel(texture=blocks_textures["lapis ore"], position=(x,int(y+2-j),z))
                    if block > 990 and block <= 995:
                        voxel = Voxel(texture=blocks_textures["emerald ore"], position=(x,int(y+2-j),z))
                    if block > 995 and block <= 1000:
                        voxel = Voxel(texture=blocks_textures["diamond ore"], position=(x,int(y+2-j),z))
                elif j > 50:
                    if block <= 820:
                        voxel = Voxel(texture=blocks_textures["deepslate"], position=(x,int(y+2-j),z))
                    if block > 820 and block <= 860:
                        voxel = Voxel(texture=blocks_textures["deepslate copper ore"], position=(x,int(y+2-j),z))
                    if block > 860 and block <= 900:
                        voxel = Voxel(texture=blocks_textures["deepslate coal ore"], position=(x,int(y+2-j),z))
                    if block > 900 and block <= 935:
                        voxel = Voxel(texture=blocks_textures["deepslate iron ore"], position=(x,int(y+2-j),z))
                    if block > 935 and block <= 955:
                        voxel = Voxel(texture=blocks_textures["deepslate gold ore"], position=(x,int(y+2-j),z))
                    if block > 955 and block <= 975:
                        voxel = Voxel(texture=blocks_textures["deepslate redstone ore"], position=(x,int(y+2-j),z))
                    if block > 975 and block <= 990:
                        voxel = Voxel(texture=blocks_textures["deepslate lapis ore"], position=(x,int(y+2-j),z))
                    if block > 990 and block <= 995:
                        voxel = Voxel(texture=blocks_textures["deepslate emerald ore"], position=(x,int(y+2-j),z))
                    if block > 995 and block <= 1000:
                        voxel = Voxel(texture=blocks_textures["deepslate diamond ore"], position=(x,int(y+2-j),z))

            voxel = Voxel(texture=blocks_textures["bedrock"], position=(x,int(y+2-100),z))    
            random.seed(x**z//seed)
            if rni(1,256) == 4:
                trees = ["oak", "birch"]
                tree = choice(trees)
                create_tree((x,y+7,z), tree)
        random.seed()

        if x == terrain_width//2 and z == x:
            start_player_y = y+8


    player = FirstPersonController(position=(terrain_width//2,start_player_y,terrain_width//2), model=player_stand_model, scale=0.65, texture=model_texture, shader=lit_with_shadows_shader)
    player.jump_height = 1.5
    player.mouse_sensitivity = Vec2(120, 120)
    player.gravity = .5  
    camera.fov = 120
    camera.clip_plane_far = 160

    scene.fog_density = (10,95)
    scene.fog_color = color.white

    curr_block = CurrentBlock(texture=current_texture)
    hand = Hand()

    player.cursor.texture=cursor_texture
    player.cursor.scale=0.08
    player.cursor.rotation = 0
    player.cursor.color=color.rgb(200,200,200) 

    PlayerPos = Text("", color=color.rgb(211,211,211), position=Vec2(-0.85, 0.45), font=nunito)
    ControlHelp = Text(controls, color=color.rgb(211,211,211), position=Vec2(0.25, 0.5), font=nunito)

    poweredby = Text('''CaveGame [By TT0tem4ik22]\npowered by Ursina\n\nSeed = {0}'''.format(seed), font=nunito, scale=3, origin=(0,0))
    poweredby.appear(speed=.05)
    poweredby.fade_out(delay=5, duration=1, curve=curve.linear)
    ControlHelp.appear(speed=.01)
    ControlHelp.fade_out(delay=15, duration=1, curve=curve.linear)

    sun = DirectionalLight(shadow_map_resolution=(2048,2048))
    sun.look_at(Vec3(1,-1,-1))
    if debug:
        sun._light.show_frustum()
    
    destroy(single_start_button)
    destroy(exit_button)
    destroy(open_website_button)
    destroy(logo)
    destroy(pre_multiplayer_button)
    menu_music.stop(destroy=True)
    game_going = True


def open_website():
    webopen("https://tt0tem4ik22.itch.io/", new=2)


def back_to_main_menu():
    global back_button, single_start_button, exit_button, open_website_button, pre_multiplayer_game
    single_start_button = Button(
        text="Start Singleplayer Game",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.4, 0.1),
        origin_y = -1,
        )
    single_start_button.on_click = start_single_game
    exit_button = Button(
        text="Exit",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.4, 0.1),
        origin_y = 1.4,
        )
    exit_button.on_click = close_game
    open_website_button = Button(
        text="Open website",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.4, 0.1),
        origin_y = 4,
        origin_x = 1.85
        )
    open_website_button.on_click = open_website
    pre_multiplayer_button = Button(
        text="Start Multiplayer Game",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.4, 0.1),
        origin_y = 0.2, 
        )
    pre_multiplayer_button.on_click = pre_multiplayer_game
    destroy(back_button)


def pre_multiplayer_game():
    # global back_button, pre_multiplayer_button
    
    # back_button = Button(
    #     text="Back",
    #     color = color.hex("#808080"),
    #     highlight_color = color.hex("#666666"),
    #     scale = (0.4, 0.1),
    #     origin_y = 1.4, 
    #     )
    # back_button.on_click = back_to_main_menu

    # destroy(single_start_button)
    # destroy(exit_button)
    # destroy(open_website_button)
    # destroy(pre_multiplayer_button)
    multiplayer_unavaiable = Text("Multiplayer is unavaiable right now", font=nunito, scale=2.5, origin=(0,0), position=(0,-0.35), color=color.rgb(230,230,230))
    multiplayer_unavaiable.appear(speed=.01)
    multiplayer_unavaiable.fade_out(delay=3, duration=1, curve=curve.linear)


def close_game():
    rmtree("models_compressed")
    quit()




seed = rni(0, 1000000)
terrain_width = 1


HB = HealthBar(max_value=20,value=20,name="HP",parent=camera.ui,origin=(0,0),position=(0,-0.45), visible=False)

controls = f"""W: Go front 
A: Go left
S: Go backward
D: Go Right
Space: jump

{BREAK}: remove block
{SET}: place block

{INV}: open/close inventory

{SAVE_COORD}: save player position and rotation (not saving world)
{LOAD_COORD}: load player position

{RTP}: random teleportation from 0 to {0} for x and z

{NOCLIP}: Noclip toggle

[Hold] {SIT}: duck
[Hold] {SPRINT}: run 

{FIRST_THIRD_PERSON}: turn on/off third person

{SAVE_LEVEL}: save world into save.save 
{LOAD_LEVEL}: load world (unable)

{PLANT_TREE}: plant tree

{SHOW_CONTROLS}: Open this text again""".format(terrain_width)

single_start_button = Button(
    text="Start Singleplayer Game",
    color = color.hex("#808080"),
    highlight_color = color.hex("#666666"),
    scale=(0.4, 0.1),
    origin_y = -1,
    )

single_start_button.on_click = start_single_game
exit_button = Button(
    text="Exit",
    color = color.hex("#808080"),
    highlight_color = color.hex("#666666"),
    scale = (0.4, 0.1),
    origin_y = 1.4,
    )
exit_button.on_click = close_game
open_website_button = Button(
    text="Open website",
    color = color.hex("#808080"),
    highlight_color = color.hex("#666666"),
    scale = (0.4, 0.1),
    origin_y = 4,
    origin_x = 1.85
    )
open_website_button.on_click = open_website
pre_multiplayer_button = Button(
    text="Start Multiplayer Game",
    color = color.hex("#808080"),
    highlight_color = color.hex("#666666"),
    scale = (0.4, 0.1),
    origin_y = 0.2, 
    )
pre_multiplayer_button.on_click = pre_multiplayer_game
logo = Text("Cave Game", parent=camera.ui, font=nunito, color=color.white, scale=5, origin=(0, -2))

camera.shader = camera_contrast_shader

app.run()
