from ursina import Vec2, color, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from ProjectResources import *

def CreatePlayer():
    player = FirstPersonController(position=(terrain_width//2,start_player_y,terrain_width//2), model=player_stand_model, scale=0.65, texture=models_texture, shader=lit_with_shadows_shader)
    player.jump_height = 1.5
    player.mouse_sensitivity = Vec2(120, 120)
    player.gravity = .5  
    player.cursor.texture=cursor_texture
    player.cursor.scale=0.08
    player.cursor.rotation = 0
    player.cursor.color=color.rgb(200,200,200) 

    camera.fov = 120
    camera.clip_plane_far = 160
    camera.shader = camera_contrast_shader

if __name__ == "__main__":
	player = CreatePlayer()