from ursina import Button, Entity


class InventorySection(Button):
    def __init__(self, position, texture):
        super().__init__(
            parent=inventory,
            color=color.white,
            texture=texture,
            position=position,
            scale=0.035
            )

    def input(self, key):
        global current_texture
        if self.hovered and key==BREAK and self.visible == True:
            current_texture = self.texture

    def update(self):
        self.visible = inventory.visible


class InventoryHandler(Entity):
    def __init__(self):
        super().__init__(
            parent=parent,
            model="quad",
            scale=(0.8,0.8),
            color=color.black
        )
    def input(self, key):
        global inv_opened_times, voxel, curr_block, current_texture, blocks_textures
        if game_going:
            if key == INV:
                inv_opened_times += 1

            if inv_opened_times % 2 == 1:
                curr_text.visible = True
                self.visible = True 
                player.cursor.visible = False
                mouse.locked = False
                player.mouse_sensitivity = Vec2(0,0)
            else:
                curr_text.visible = False
                self.visible = False
                player.cursor.visible = True
                mouse.locked = True
                mouse.position = (0,0)
                player.mouse_sensitivity = Vec2(120,120)

    def update(self):
        if inventory.visible == True:
            curr_text.text = [key for key, value in blocks_textures.items() if value == current_texture][0].capitalize()


def InitializeInvintory():
    inv_counter = 0
    inventory = InventoryHandler()
    for y in range(17):
        for x in range(17):
            if inv_counter < len(blocks):
                print(blocks_textures[blocks[inv_counter]])
                texture = blocks[inv_counter]
                section = InventorySection((x/2-4,y/2-4), blocks_textures[blocks[inv_counter]])
                inv_counter += 1
    curr_text = Text("Current texture", font=nunito, scale=2.5, origin=(0,0), position=(0,0), color=color.rgb(230,230,230))
    curr_text.visible = False
    inventory.visible = False
