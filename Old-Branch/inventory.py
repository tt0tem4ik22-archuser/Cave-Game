from ursina import Button, Entity, color, camera, Text, mouse
from ProjectResources import blocks, blocks_textures
from ProjectVariables import *
from controls import INV

inv_opened_times = 0
curr_text = Text("")

class InventorySection(Button):
    def __init__(self, parent, position, texture):
        super().__init__(
            parent=parent,
            color=color.white,
            texture=texture,
            position=position,
            scale=0.035
            )
        print(f"Init inventory section | {texture.replace("assets/textures/blocks/", "")} | {position} " if debug else "", end="")

    def input(self, key):
        global current_texture
        if self.hovered and key==BREAK and self.visible == True:
            current_texture = self.texture
            print(f"{current_texture} choosed" if debug else "", end="")

    def update(self):
        self.visible = self.parent.visible


class InventoryHandler(Entity):
    def __init__(self, parent=camera.ui):
        super().__init__(
            parent=parent,
            model="quad",
            scale=(0.8,0.8),
            color=color.gray
        )

        inv_counter = 0
        for y in range(17):
            for x in range(17):
                if inv_counter < len(blocks):
                    texture = blocks[inv_counter]
                    section = InventorySection(self, (x/2-4,y/2-4), blocks_textures[blocks[inv_counter]])
                    inv_counter += 1
        
        curr_text = Text("Current texture", font=nunito, scale=2.5, origin=(0,0), position=(0,0), color=color.rgb(230,230,230))
        curr_text.visible = False
        self.visible = False

        print("Inventory initialized successfully!" if debug else "", end="")

    def input(self, key):
        global inv_opened_times, game_going

        if game_going:
            if key == INV:
                inv_opened_times += 1

            if inv_opened_times % 2 == 1:
                print("Opened inventory" if debug else "", end="")
                curr_text.visible = True
                self.visible = True 
                mouse.locked = False
            else:
                print("Closed inventory" if debug else "", end="")
                curr_text.visible = False
                self.visible = False
                mouse.locked = True
                mouse.position = (0,0)

    def update(self):
        if self.visible == True:
            curr_text.text = current_texture.capitalize()