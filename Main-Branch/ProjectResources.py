from ursina import load_texture, load_model, Audio, color
from random import randint as rni, uniform
from os.path import isfile

#shaders
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import camera_contrast_shader
from ursina.lights import DirectionalLight


# models
sword_model = load_model("assets/models/diamond_sword.obj")
player_stand_model = load_model("assets/models/player_stand.obj")
player_sit_model = load_model("assets/models/player_sit.obj")

#textures
cursor_texture = load_texture("assets/textures/cursor.png")
models_texture = load_texture("assets/textures/models_texture.png")
none_texture = load_texture("no texture found.fuckit")
error_texture = load_texture("assets/textures/error.png")

blocks_colors = {
    "white": color.white, 
    "gray": color.gray, 
    "dark gray": color.dark_gray, 
    "black": color.black, 
    "red": color.red, 
    "pink": color.pink, 
    "orange": color.orange, 
    "brown": color.brown, 
    "yellow": color.yellow, 
    "lime": color.lime, 
    "green": color.green, 
    "light blue": color.azure, 
    "blue": color.blue, 
    "cyan": color.cyan, 
    "purple": color.violet, 
    "magenta": color.magenta
}

blocks = [
    "stone", # Камушъки
    "cobblestone",
    "mossy cobblestone",
    "deepslate",
    "diorite",
    "diorite smooth",
    "andesite",
    "andesite smooth",
    "granite",
    "granite smooth",
    "amethyst",
    "obsidian",
    "crying obsidian",
    "bedrock",
    "netherrack",
    "endstone",
    "purpur block",

    "quartz bricks", # Кирпичи
    "bricks",
    "stone brick",
    "mossy stone bricks",
    "cracked deepslate tiles",
    "deepslate bricks",
    "cracked deepslate bricks",
    "nether bricks",
    "red nether bricks",
    "chiseled nether bricks",
    "cracked nether bricks"
    "endstone bricks",

    "coal ore", # Руды
    "copper ore",
    "iron ore",
    "gold ore",
    "lapis ore",
    "redstone ore",
    "emerald ore",
    "diamond ore",

    "deepslate coal ore", # Глубокие руды
    "deepslate copper ore",
    "deepslate iron ore",
    "deepslate gold ore",
    "deepslate lapis ore",
    "deepslate redstone ore",
    "deepslate emerald ore",
    "deepslate diamond ore",

    "copper ore block", # Скомпонованые руды
    "iron ore block",
    "gold ore block",

    "nether gold ore", # Адские руды
    "quartz ore",

    "coal block", # Драгоценные блоки
    "copper block",
    "exposed copper block",
    "weathered copper block",
    "oxidized copper block",
    "iron block",
    "gold block",
    "lapis block",
    "redstone block",
    "emerald block",
    "diamond block",
    "netherite block",
    "quartz",

    "dark oak vertical", # Древесина вертикальная
    "birch vertical",
    "oak vertical",
    "acacia vertical",
    "crimson vertical",
    "mangrove vertical",
    "spruce vertical",
    "warped vertical",
    "jungle vertical",

    "dark oak horisontal", # Древесина горизонтальная
    "birch horisontal",
    "oak horisontal",
    "acacia horisontal",
    "crimson horisontal",
    "mangrove horisontal",
    "spruce horisontal",
    "warped horisontal",
    "jungle horisontal",

    "dark oak wood", # Доски
    "birch wood",
    "oak wood",
    "acacia wood",
    "crimson wood",
    "jungle wood",
    "mangrove wood",
    "spruce wood",
    "warped wood",

    "crimson wart", # Листочьки
    "warped wart",
    "birch leaves",
    "oak leaves",
    "spruce leaves",
    "jungle leaves",
    "mangrove leaves",
    "azalea leaves",
    "acacia leaves",
    "dark oak leaves",
    "flowering azalea leaves",

    "water", # Жидкости
    "lava",

    "sand", # Природные верхние
    "red sand",
    "gravel",
    "dirt",
    "moss",
    "grass",

    "magma", # Другое
    "spawner",
    "sponge",
    "glass",

    "wool",
    "concrete", 
    "concrete powder"
]

for block_color in blocks_colors:
    blocks.append(f"{block_color} glazed terracota")

blocks_textures = {}
for block in blocks:
    if isfile(f"assets/textures/blocks/{block}.png"):
        blocks_textures[block] = f"assets/textures/blocks/{block}.png"

def loadSound(name, type, amount):
    if not type == "music":
        sounds[name] = Audio(f"assets/sounds/{type}/{name}/{name}{rni(1,amount)}.mp3", loop=False, autoplay=False, pitch=uniform(0.8, 1.2))
    else:
        sounds[name] = Audio(f"assets/sounds/{type}/{name}/{name}{rni(1,amount)}.mp3", loop=False, autoplay=False, pitch=1)
    
sounds_list = [
    ["teleport", "others", 1],
    ["water", "blocks", 2],
    ["lava", "blocks", 1],
    ["stone", "blocks", 4],
    ["wood", "blocks", 4],
    ["dirt", "blocks", 4],
    ["glass", "blocks", 1],
    ["gravel", "blocks", 4],
    ["moss", "blocks", 5],
    ["amethyst", "blocks", 2],
    ["sand", "blocks", 4],
    ["menu_music", "music", 5],
]
sounds = {}

for sound in sounds_list:
    loadSound(sound[0], sound[1], sound[2])


def playSound(name):
    sounds[name].play()
    for sound in sounds_list:
        if sound[0] == name:
            loadSound(sound[0], sound[1], sound[2])
            break

stone_sound = ["deepslate gold ore", "deepslate iron ore", "deepslate emerald ore", "deepslate diamond ore", "deepslate lapis ore", "deepslate redstone ore", "deepslate copper ore", "deepslate coal ore", "cracked deepslate tiles", "cracked deepslate bricks", "deepslate bricks", "deepslate", "quartz bricks", "quartz", "purpur block", "magma", "obsidian", "red nether bricks", "endstone", "endstone bricks", "spawner", "mossy stone bricks", "bedrock", "netherite block", "chiseled nether bricks", "cracked nether bricks", "nether bricks", "netherrack", "crying obsidian", "bricks", "diamond block", "emerald block", "iron block", "gold block", "lapis block", "redstone block", "coal block", "copper block", "diamond ore", "emerald ore", "iron ore", "gold ore", "lapis ore", "redstone ore", "coal ore", "copper ore", "stone", "cobblestone", "glass", "stone brick", "nether gold ore", "quartz ore", "copper ore block", "iron ore block", "gold ore block", "weathered copper block", "exposed copper block", "oxidized copper block", "mossy cobblestone", "andesite", "andesite smooth", "diorite", "diorite smooth", "granite", "granite smooth"]
wood_sound = ["oak wood", "oak vertical", "oak horisontal", "dark oak wood", "dark oak vertical", "dark oak horisontal", "birch wood", "birch vertical", "birch horisontal", "acacia wood", "acacia vertical", "acacia horisontal", "crimson wood", "crimson vertical", "crimson horisontal", "warped wood", "warped vertical", "warped horisontal", "jungle wood", "jungle vertical", "jungle horisontal", "spruce wood", "spruce vertical", "spruce horisontal", "mangrove wood", "mangrove vertical", "mangrove horisontal"]
grass_sound = ["grass", "dirt", "oak leaves", "sponge", "dark oak leaves", "birch leaves", "acacia leaves", "azalea leaves", "flowering azalea leaves", "mangrove leaves", "jungle leaves", "spruce leaves"]
gravel_sound = ["gravel"]
glass_sound = ["glass"]
sand_sound = ["sand", "red sand"]
amethyst_sound = ["amethyst"]
moss_sound = ["moss", "crimson wart", "warped wart"]
water_sound = ["water"]
lava_sound = ["lava"]

ingame_music = Audio(f"assets/sounds/music/ingame_music/ingame_music{rni(1,43)}.mp3", loop=False, autoplay=False, pitch=1)

#font
nunito = "assets/fonts/Nunito.ttf"