from numpy import floor
from perlin_noise import PerlinNoise
from random import randint as rni, choice, seed as sd


start_player_y = 7
terrain_width = 1

def createTree(pos, type):
    output = []
    if type in ["oak", "birch"]:
        for i in range(5):
            output.append([int(pos[0]), int(pos[1]+i+1), int(pos[2]), f"{type} vertical"])
        
        output.append([int(pos[0]), int(pos[1]+6), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+7), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+7), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+7), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+6), int(pos[2]-1), f"{type} leaves"])        
        output.append([int(pos[0]), int(pos[1]+5), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+4), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+6), int(pos[2]-2), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+5), int(pos[2]-2), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+4), int(pos[2]-2), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+6), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+5), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+4), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+6), int(pos[2]+2), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+5), int(pos[2]+2), f"{type} leaves"])
        output.append([int(pos[0]), int(pos[1]+4), int(pos[2]+2), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+7), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+7), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+6), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+5), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+4), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-2), int(pos[1]+6), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-2), int(pos[1]+5), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]-2), int(pos[1]+4), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+6), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+5), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+4), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+2), int(pos[1]+6), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+2), int(pos[1]+5), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+2), int(pos[1]+4), int(pos[2]), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+4), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+5), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+6), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+4), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+5), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]+1), int(pos[1]+6), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+4), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+5), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+6), int(pos[2]+1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+4), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+5), int(pos[2]-1), f"{type} leaves"])
        output.append([int(pos[0]-1), int(pos[1]+6), int(pos[2]-1), f"{type} leaves"])
    return output


def GenTerrain(advanced, seed, octaves, amplitude, period, ores, trees, terrain_width, gen_only_terrain):
    output = []
    
    if advanced == "Enabled":
        octaves = octaves
        noise = PerlinNoise(octaves=octaves, seed=seed)
        amp = amplitude
        period = period

        landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]
        for position in range(terrain_width**2):
            x = floor(position / terrain_width)
            z = floor(position % terrain_width)
            y = floor(noise([x/period, z/period])*amp)
            landscale[int(x)][int(z)] = int(y)

        
            output.append([x, y, z, "grass"])

            if gen_only_terrain == "Disabled":
                for i in range(4):
                    output.append([x, y-i-1, z, "dirt"])

                for j in range(100):
                    if ores == "Enabled":
                        if y != 0:
                            sd(int(seed//y-x**z+j**4))
                        else:
                            sd(int(seed**0.5-x**z+j**4))
                        block = rni(0,1000)
                        if j <= 50:
                            if block <= 820:
                                output.append([x, y-5-j, z, "stone"])
                            if block > 820 and block <= 860:
                                output.append([x, y-5-j, z, "copper ore"])
                            if block > 860 and block <= 900:
                                output.append([x, y-5-j, z, "coal ore"])
                            if block > 900 and block <= 935:
                                output.append([x, y-5-j, z, "iron ore"])
                            if block > 935 and block <= 955:
                                output.append([x, y-5-j, z, "gold ore"])
                            if block > 955 and block <= 975:
                               output.append([x, y-5-j, z, "redstone ore"])
                            if block > 975 and block <= 990:
                                output.append([x, y-5-j, z, "lapis ore"])
                            if block > 990 and block <= 995:
                                output.append([x, y-5-j, z, "emerald ore"])
                            if block > 995 and block <= 1000:
                                output.append([x, y-5-j, z, "diamond ore"])
                        elif j > 50:
                            if block <= 820:
                                output.append([x, y-5-j, z, "deepslate"])
                            if block > 820 and block <= 860:
                                output.append([x, y-5-j, z, "deepslate copper ore"])
                            if block > 860 and block <= 900:
                                output.append([x, y-5-j, z, "deepslate coal ore"])
                            if block > 900 and block <= 935:
                                output.append([x, y-5-j, z, "deepslate iron ore"])
                            if block > 935 and block <= 955:
                                output.append([x, y-5-j, z, "deepslate gold ore"])
                            if block > 955 and block <= 975:
                               output.append([x, y-5-j, z, "deepslate redstone ore"])
                            if block > 975 and block <= 990:
                                output.append([x, y-5-j, z, "deepslate lapis ore"])
                            if block > 990 and block <= 995:
                                output.append([x, y-5-j, z, "deepslate emerald ore"])
                            if block > 995 and block <= 1000:
                                output.append([x, y-5-j, z, "deepslate diamond ore"])
                        if z != -1 and x != 0:
                            sd(seed//x**z)
                        else:
                            sd(seed+x**2+z**2)
                    else:
                        if j <= 50:
                            output.append([x, y-5-j, z, "stone"])
                        elif j > 50:
                            output.append([x, y-5-j, z, "deepslate"])
                    

                output.append([x, y-105, z, "bedrock"])
                if rni(1,256) == 4 and trees == "Enabled":
                    sd(x*z+seed)
                    trees = ["oak", "birch"]
                    tree = choice(trees)
                    for block in createTree((x,y,z), tree):
                        output.append(block)

                sd()
    else:
        for x in range(17):
            for z in range(17):
                output.append([x, 0, z, "stone"])

    return output