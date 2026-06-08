from ursina import Vec2, color
from ursina.prefabs.first_person_controller import FirstPersonController

from ProjectResources import *
from generation import terrain_width, start_player_y
import inventory


class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            position=(terrain_width//2+1,start_player_y,terrain_width//2), 
            model=player_stand_model,
            scale=0.65,
            texture=models_texture,
            shader=lit_with_shadows_shader,
            jump_height = 1.5,
            mouse_sensitivity = Vec2(120, 120),
            gravity = .5,
            )
        #self.cursor.texture=cursor_texture,
        #self.cursor.scale=0.08,
        #self.cursor.rotation = 0,
        #self.cursor.color=color.rgb(200,200,200) ,

        camera.fov = 120
        # camera.clip_plane_far = 160
        # camera.shader = camera_contrast_shader
    def update(self):
        if inventory.inv_opened_times % 2 == 0:
            self.mouse_sensitivity = Vec2(120,120)
        else:
            self.mouse_sensitivity = Vec2(0,0)
