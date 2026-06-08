voxel_list = []

def save_world():
    global voxel_list
    try:
        with open('save.save', 'w+') as save:
            save.truncate(0)
            save.write(str(voxel_list))

        saved_text = Text("Level saved succefully...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))

        saved_text.appear(speed=.05)
        saved_text.fade_out(delay=0.75, duration=1, curve=curve.linear)
    except:
        saved_text = Text("Level could not be saved...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))

        saved_text.appear(speed=.05)
        saved_text.fade_out(delay=0.75, duration=1, curve=curve.linear)


def load_world():
    global voxel_list 
    try:
        with open('save.save', 'r') as save:
            voxel_list = json.load(save)
            print(voxel_list)
        """DESTROY ALL EXISTING voxel"""
        for element in voxel_list:
            texture_value = element.get('texture')
            x_value = element.get('x')
            y_value = element.get('y')
            z_value = element.get('z')
            voxel = Voxel(texture=load_texture(f"assets/textures/blocks/{texture_value}"), position=(int(x_value), int(y_value), (z_value)))

        player.position=(0,10,0)
        loaded_text = Text("Level loaded succefully...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))
        loaded_text.appear(speed=.05)
        loaded_text.fade_out(delay=0.75, duration=1, curve=curve.linear)
    except:
        loaded_text = Text("Level could not be loaded...", font=nunito, scale=3.5, origin=(0,0), position=(0,0.3), color=color.rgb(230,230,230))
        loaded_text.appear(speed=.05)
        loaded_text.fade_out(delay=1.25, duration=1, curve=curve.linear)
