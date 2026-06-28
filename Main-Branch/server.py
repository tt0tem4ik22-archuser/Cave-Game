from ursinanetworking import * 

from os import system
from sys import argv

from generation import GenTerrain
from ProjectVariables import debug


print("\033[95mStarting Cave Game server...\033[0m")

Server = UrsinaNetworkingServer(argv[1], int(argv[2]))
Easy = EasyUrsinaNetworkingServer(Server)

terrain = {}


def destroy_voxel(voxel_name):
    del terrain[voxel_name]
    Easy.remove_replicated_variable_by_name(voxel_name)


voxel_counter = 0
def spawn_voxel(voxel_type, x, y, z, source='client'):
    global voxel_counter
    voxel_name = f"voxel_{voxel_counter}"

    Easy.create_replicated_variable(voxel_name, {"type": "voxel", "voxel_type": voxel_type, "position": (x, y, z), "source": source})

    terrain[voxel_name] = {'name': voxel_name, 'position': (x, y, z,)}

    voxel_counter += 1


@Server.event 
def onClientConnected(client):
    Easy.create_replicated_variable(f"player_{client.id}", {'type': 'player', 'id': client.id, 'position': (0,0,0), 'sit': False})
    print(f"\033[93m{client} connected!\033[0m")
    client.send_message("GetId", client.id)
    client.send_message("GetTerrainWidth", terrain_width)


@Server.event 
def onClientDisconnected(client):
    Easy.remove_replicated_variable_by_name(f"player_{client.id}")
    print(f"\033[93m{client.id} disconnected!\033[0m")


@Server.event
def request_destroy_voxel(client, voxel_name):
    destroy_voxel(voxel_name)
    if debug:
        print(f"Client {client.id} destroyed Voxel {voxel_name}")


@Server.event 
def request_spawn_voxel(client, content):
    spawn_voxel(content['voxel_type'], content['x'], content['y'], content['z'])
    if debug:
        print(f"Client {client.id} placed Voxel {content['voxel_type']} on position {content['x']} {content['y']} {content['z']}")


@Server.event 
def UpdatePosition(client, NewPosition):
    Easy.update_replicated_variable_by_name(f"player_{client.id}", "position", NewPosition)


@Server.event 
def UpdateSit(client, Sit):
    Easy.update_replicated_variable_by_name(f"player_{client.id}", "sit", Sit)


@Server.event 
def UpdateRot(client, Rot):
    Easy.update_replicated_variable_by_name(f"player_{client.id}", "rot", Rot)


@Server.event
def ask_terrain_width(client):
    client.send_message("answer_terrain_width", terrain_width)


if argv[3] == "Disabled":
    adv = False
    terrain_width = 17
else:
    adv = True
    terrain_width = int(argv[10])

if argv[8] == "Disabled":
    ores = False
else:
    ores = True

if argv[9] == "Disabled":
    trees = False
else:
    trees = True

world = GenTerrain(adv, int(argv[4]), int(argv[5]), int(argv[6]), int(argv[7]), ores, trees, terrain_width)

for voxel in world:
    spawn_voxel(voxel[3], voxel[0], voxel[1], voxel[2], source='server')


while True:
    Easy.process_net_events()