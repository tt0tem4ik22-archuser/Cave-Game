from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from ProjectResources import *

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mouse_sensitivity = (120, 120)
        self.jump_height = 1.5
        self.mouse_sensitivity = Vec2(120, 120)
        self.gravity = .5  
        self.cursor.texture=cursor_texture
        self.cursor.scale=0.08
        self.cursor.rotation = 0
        self.cursor.color=color.rgb(200,200,200) 
        camera.shader = camera_contrast_shader
        camera.fov = 120
        camera.clip_plane_far = 160

class PlayerRepresentation(Entity):
    def __init__(self, position = (0,5,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = player_stand_model,
            texture = models_texture,
            origin_y = 0,
            color = color.white,
            highlight_color = color.white,
        )
        self.sit = False

    def update(self):
        if self.sit == True:
            self.model = player_sit_model
        else:
            self.model = player_stand_model