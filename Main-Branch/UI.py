from ursina import Text, InputField, Button, color, camera, Entity, Vec2, Vec3
from ProjectResources import sword_model, models_texture, nunito, blocks_textures

current_texture = blocks_textures["grass"]

class Menu:
	def InitMainMenu():
	    seed_text = Text("Input seed\nSingleplayer only", parent=camera.ui, font=nunito, color=color.white, scale=1, origin=(0, 2), position=(.5, .26))
	    seed_input_field = InputField(
	        y=.1,
	        x=.5,
	        limit_content_to="0123456789",
	        max_lines=1
	        )
	    single_start_button = Button(
	        text="Start Singleplayer Game",
	        color = color.hex("#808080"),
	        highlight_color = color.hex("#666666"),
	        scale=(0.4, 0.1),
	        origin_y = -1,
	        on_click = start_single_game
	        )

	    exit_button = Button(
	        text="Exit",
	        color = color.hex("#808080"),
	        highlight_color = color.hex("#666666"),
	        scale = (0.4, 0.1),
	        origin_y = 1.4,
	        on_click = close_game
	        )

	    open_website_button = Button(
	        text="Open my itch.io",
	        color = color.hex("#808080"),
	        highlight_color = color.hex("#666666"),
	        scale = (0.4, 0.1),
	        origin_y = 4,
	        origin_x = 1.85,
	        on_click = open_website
	        )

	    pre_multiplayer_button = Button(
	        text="Start Multiplayer Game",
	        color = color.hex("#808080"),
	        highlight_color = color.hex("#666666"),
	        scale = (0.4, 0.1),
	        origin_y = 0.2, 
	        on_click = pre_multiplayer_game
	        )
	    logo = Text("Cave Game", parent=camera.ui, font=nunito, color=color.white, scale=5, origin=(0, -2))


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