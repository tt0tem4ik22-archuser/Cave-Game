from ursina import load_texture, load_model, Audio
from random import randint as rni

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
blocks = [
    "stone", # Камушки
    "cobblestone",
    "diorite",
    "andesite",
    "granite",
    "diorite smooth",
    "andesite smooth",
    "granite smooth",

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

    "weathered copper block",
    
    
    "flowering azalea leaves",

    "quartz bricks",
    "crimson wart",
    "warped wart",
    "birch leaves",
    "spruce leaves",
    "jungle leaves",
    "mangrove leaves",
    "azalea leaves",
    "acacia leaves",
    "dark oak leaves",
    "deepslate coal ore",
    "deepslate copper ore",
    "deepslate iron ore",
    "deepslate gold ore",
    "deepslate lapis ore",
    "deepslate redstone ore",
    "deepslate emerald ore",
    "deepslate diamond ore",
    "deepslate bricks",
    "cracked deepslate tiles",
    "cracked deepslate bricks",
    "deepslate",
    "magma",
    "purpur block",
    "amethyst",
    "dirt",
    "spawner",
    "sponge",
    "water",
    "stone brick",
    "nether gold ore",
    "red nether bricks",
    "redstone ore",
    "redstone block",
    "sand",
    "red sand",
    "oxidized copper block",
    "quartz ore",
    "nether bricks",
    "netherite block",
    "oak leaves",
    "moss",
    "mossy stone bricks",
    "mossy cobblestone",
    "lava",
    "lapis block",
    "lapis ore",
    "obsidian",
    "quartz",
    "netherrack",
    "iron ore",
    "iron ore block",
    "iron block",
    "grass",
    "gravel",
    "glass",
    "endstone",
    "exposed copper block",
    "gold ore block",
    "gold block",
    "gold ore",
    "endstone bricks",
    "emerald block",
    "emerald ore",
    "crying obsidian",
    "diamond block",
    "diamond ore",
    "bedrock",
    "chiseled nether bricks",
    "bricks",
    "coal block",
    "coal ore",
    "copper block",
    "copper ore block",
    "copper ore",
    "cracked nether bricks"
]
blocks_textures = {}
for block in blocks:
    blocks_textures[block] = f"assets/textures/blocks/{block}.png"

#sounds
teleport_sound = Audio("assets/sounds/teleport.mp3", loop=False, autoplay = False)
water_sound = Audio("assets/sounds/blocks/water/water{0}.mp3".format(rni(1,2)), loop=False, autoplay=False)
lava_sound = Audio("assets/sounds/blocks/lava/lava{0}.mp3".format(rni(1,2)), loop=False, autoplay=False)
stone_sound = Audio("assets/sounds/blocks/stone/stone{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
wood_sound = Audio("assets/sounds/blocks/wood/wood{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
dirt_sound = Audio("assets/sounds/blocks/dirt/dirt{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
glass_sound = Audio("assets/sounds/blocks/glass.mp3", loop=False, autoplay = False)
gravel_sound = Audio("assets/sounds/blocks/gravel/gravel{0}.ogg".format(rni(1,4)), loop=False, autoplay = False)
moss_sound = Audio("assets/sounds/blocks/moss/moss{0}.ogg".format(rni(1,5)), loop=False, autoplay = False)
amethyst_sound = Audio("assets/sounds/blocks/amethyst/amethyst{0}.ogg".format(rni(1,2)), loop=False, autoplay = False)
sand_sound = Audio("assets/sounds/blocks/sand/sand{0}.mp3".format(rni(1,4)), loop=False, autoplay = False)
music = Audio("assets/sounds/music/music_({0}).mp3".format(rni(0,42)), loop=False, autoplay = False, volume=1)
menu_music = Audio("assets/sounds/music/menu_({0}).mp3".format(rni(0,4)), loop=False, autoplay = True)

#font
nunito = "assets/fonts/Nunito.ttf"