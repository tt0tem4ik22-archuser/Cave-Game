from ursina import Text, InputField, Button, color, camera, Entity, Vec2, Vec3
from ursina.prefabs.health_bar import HealthBar

from ProjectResources import models_texture, nunito, blocks_textures
from ProjectVariables import current_texture


class Hand(Entity):
    def __init__(self):
        super().__init__(
                parent=camera.ui,
                model=sword_model,
                scale=(0.2,0.4),
                texture=models_texture,
                rotation=Vec3(15, -310, -45),
                position=Vec2(0.65, -0.35)
        )


class CurrentBlock(Entity):
    def __init__(self):
        super().__init__(
                parent=camera.ui, 
                model="quad",
                scale=(0.1,0.1),
                color=color.rgb(230,230,230),
                texture=blocks_textures[current_texture],
                position=Vec2(-0.75, -0.35)
            ) 
    def update(self):
        self.texture = blocks_texture[current_texture]
    
    
def initHB(max_value, init_value):
    HB = HealthBar(max_value=max_value,value=init_value,parent=camera.ui,origin=(0,0),position=(0,-0.45), visible=True)