from ursina import *
from ursina.prefabs.slider import Slider

from random import randint as rni
from os import system as sys, _exit
from sys import argv
from time import sleep

import subprocess

from ProjectVariables import debug
from ProjectResources import project_font, sounds


def close_menu():
    _exit(0)


def StartSingleplayer():
    global toggle_noise_button, world_size_input_slider,seed_input_field, amp_input_slider, period_input_slider, octaves_input_slider, toggle_ores_button, toggle_trees_button
    if not seed_input_field.text == "":
        seed = int(seed_input_field.text)
    else:
        seed = rni(0,999999999999999999999999)

    noise_enabled = toggle_noise_button.text
    ores_enabled = toggle_ores_button.text
    trees_enabled = toggle_trees_button.text
    gen_only_terrain_enabled = toggle_gen_only_terrain_button.text

    world_size_input = world_size_input_slider.value

    octaves = int(octaves_input_slider.value)
    amp = int(amp_input_slider.value)
    period = int(period_input_slider.value)

    command = ["python3", "singleplayer.py", f"{noise_enabled}", f"{seed}", f"{octaves}", f"{amp}", f"{period}", f"{ores_enabled}", f"{trees_enabled}", f"{world_size_input}", f"{gen_only_terrain_enabled}"]
    s_game = subprocess.Popen(command)
    close_menu()


def StartMultiplayer():
    pass


def JoinMultiplayer():
    pass


def toggle_noise():
    global toggle_noise_button, toggle_gen_only_terrain_button, gen_only_terrain_text, world_size_text, world_size_input_slider, seed_text, seed_input_field, amp_text, amp_input_slider, period_text, period_input_slider, octaves_text, octaves_input_slider, toggle_ores_button, toggle_trees_button, ores_text, trees_text
    if toggle_noise_button.text == "Enabled":
        toggle_noise_button.text = "Disabled"
        set_to_default_button.visible = False
        seed_text.visible = False
        seed_input_field.visible = False
        amp_text.visible = False
        amp_input_slider.visible = False
        period_text.visible = False
        period_input_slider.visible = False
        octaves_text.visible = False
        octaves_input_slider.visible = False
        ores_text.visible = False
        toggle_ores_button.visible = False
        trees_text.visible = False
        toggle_trees_button.visible = False
        gen_only_terrain_text.visible = False
        toggle_gen_only_terrain_button.visible = False
        world_size_text.visible = False
        world_size_input_slider.visible = False
    else:
        toggle_noise_button.text = "Enabled"
        set_to_default_button.visible = True
        world_size_text.visible = True
        world_size_input_slider.visible = True
        seed_text.visible = True
        seed_input_field.visible = True
        amp_text.visible = True
        amp_input_slider.visible = True
        period_text.visible = True
        period_input_slider.visible = True
        octaves_text.visible = True
        octaves_input_slider.visible = True
        ores_text.visible = True 
        toggle_ores_button.visible = True
        gen_only_terrain_text.visible = True
        toggle_gen_only_terrain_button.visible = True
        trees_text.visible = True 
        toggle_trees_button.visible = True


def toggle_ores():
    global toggle_ores_button
    if toggle_ores_button.text == "Enabled":
        toggle_ores_button.text = "Disabled"
    else:
        toggle_ores_button.text = "Enabled"


def toggle_trees():
    global toggle_trees_button
    if toggle_trees_button.text == "Enabled":
        toggle_trees_button.text = "Disabled"
    else:
        toggle_trees_button.text = "Enabled"

def toggle_gen_only_terrain():
    global toggle_gen_only_terrain_button
    if toggle_gen_only_terrain_button.text == "Enabled":
        toggle_gen_only_terrain_button.text = "Disabled"
    else:
        toggle_gen_only_terrain_button.text = "Enabled"


def update():
    if not sounds["menu_music"].playing:
        sounds["menu_music"].play()


def SetToDefault():
    global toggle_noise_button, toggle_gen_only_terrain_button, world_size_input_slider, seed_input_field, amp_input_slider, period_input_slider, octaves_input_slider, toggle_ores_button, toggle_trees_button
    seed_input_field.text = ""

    octaves_input_slider.value = 2
    amp_input_slider.value = 6
    period_input_slider.value = 48
    world_size_input_slider.value = 2

    toggle_noise_button.text = "Enabled"
    toggle_ores_button.text = "Enabled"
    toggle_trees_button.text = "Enabled"
    toggle_gen_only_terrain_button.text = "Disabled"


def main():
    global toggle_noise_button, toggle_gen_only_terrain_button, gen_only_terrain_text, world_size_text, world_size_input_slider, set_to_default_button, seed_text, seed_input_field, amp_text, amp_input_slider, period_text, period_input_slider, octaves_text, octaves_input_slider, toggle_ores_button, toggle_trees_button, ores_text, trees_text
    app = Ursina(title="Cave Game | Main Menu", use_ingame_console=False, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)
    window.fps_counter.enabled = False
    window.color=color.hex("#3BA5FF")

    logo = Text("Cave Game", parent=camera.ui, font=project_font, color=color.white, scale=5, origin=(0, -2.5))

    conf = Text("Configure generation", parent=camera.ui, font=project_font, color=color.white, scale=1.5, origin=(0,2), position=(-.75, 0.4))

    seed_text = Text("Seed:", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0, 2), position=(-1.05, .2))
    seed_input_field = InputField(
        y=.15,
        x=-.75,
        limit_content_to="0123456789",
        max_lines=1, 
        color=color.gray,
    )

    octaves_text = Text("Octaves:", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0, 2), position=(-1.06, .1))
    octaves_input_slider = Slider(parent=camera.ui, min=1, max=10, y=0.05, x=-.95, step=1, default=2)

    amp_text = Text("Amplitude:", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0, 2), position=(-1.08, 0.03))
    amp_input_slider = Slider(parent=camera.ui, min=1, max=20, y=-0.02, x=-.95, step=1, default=6)

    period_text = Text("Period:", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0, 2), position=(-1.06, -.04))
    period_input_slider = Slider(parent=camera.ui, min=1, max=100, y=-0.09, x=-.95, step=1, default=48)

    world_size_text = Text("World size:", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0, 2), position=(-1.08, -.1))
    world_size_input_slider = Slider(parent=camera.ui, min=1, max=64, y=-0.16, x=-.95, step=1, default=2)

    adv_text = Text("Advanced: ", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0,2), position=(-1.07, 0.29))
    toggle_noise_button = Button(
        text="Enabled",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.24, 0.05),
        origin = (0, 2),
        position=(-0.88, 0.34),
        on_click = toggle_noise
    )

    gen_only_terrain_text = Text("Generate only terrain: ", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0,2), position=(-1.05, -.18))
    toggle_gen_only_terrain_button = Button(
        text="Disabled",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.2, 0.05),
        origin = (0, 2),
        position=(-0.9, -0.13),
        on_click = toggle_gen_only_terrain
    )

    ores_text = Text("Ores: ", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0,2), position=(-1.05, -.26))
    toggle_ores_button = Button(
        text="Enabled",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.2, 0.05),
        origin = (0, 2),
        position=(-0.9, -0.21),
        on_click = toggle_ores
    )

    trees_text = Text("Trees: ", parent=camera.ui, font=project_font, color=color.white, scale=1, origin=(0,2), position=(-1.05, -.34))
    toggle_trees_button = Button(
        text="Enabled",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.2, 0.05),
        origin = (0, 2),
        position=(-0.9, -0.29),
        on_click = toggle_trees
    )

    set_to_default_button = Button(
        text="Set to default",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.24, 0.05),
        origin = (0, 2),
        position=(-0.62, 0.34),
        on_click = SetToDefault
    )


    single_start_button = Button(
        text="Start Singleplayer Game",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale=(0.4, 0.1),
        origin_y = -1,
        on_click = StartSingleplayer
    )

    exit_button = Button(
        text="Exit",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.4, 0.1),
        origin_y = 1.4,
        on_click = close_menu
        )

    join_multiplayer_button = Button(
        text="Join",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.18, 0.1),
        origin_y = 0.2,
        position = (-.11,0),
        on_click = JoinMultiplayer
        )

    start_multiplayer_button = Button(
        text="Start",
        color = color.hex("#808080"),
        highlight_color = color.hex("#666666"),
        scale = (0.18, 0.1),
        origin_y = 0.2,
        position = (0.11,0),
        on_click = StartMultiplayer
        )

    app.run()


if __name__ == "__main__":
    main()