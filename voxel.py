from ursina import *

from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import camera_contrast_shader
from ursina.lights import DirectionalLight

from ProjectResources import *
from ProjectVariables import current_texture, debug


class Voxel(Button):
    def __init__(self, position=(0,0,0), init_texture=current_texture, breakable=True, client="Client"):
        try:
            super().__init__(
                parent=scene,
                position=position,
                model="cube",
                collider="box",
                origin_y=-.5,
                texture=blocks_textures[init_texture],
                color=color.white,
                highlight_color = color.light_gray,
                default_shader=lit_with_shadows_shader,
                shader=lit_with_shadows_shader
            )
        except KeyError:
            super().__init__(
                parent=scene,
                position=position,
                model="cube",
                collider="box",
                origin_y=-.5,
                texture=error_texture,
                color=color.white,
                highlight_color = color.light_gray,
                default_shader=lit_with_shadows_shader,
                shader=lit_with_shadows_shader
            )
        self.init_texture = init_texture
        self.name = "unnamed_block"
        self.client = None
        self.breakable = breakable


def main():
    app = Ursina(title="Cave Game | Voxel test", use_ingame_console=debug, borderless=False, fullscreen=False, icon="assets/textures/icon.ico", development_mode=debug)

    cam = EditorCamera()

    for x in range(4):
        for z in range(4):
            voxel = Voxel((x-2, 0, z-2))

    app.run()


if __name__ == "__main__":
    main()