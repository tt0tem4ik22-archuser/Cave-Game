from numpy import floor
from perlin_noise import PerlinNoise
from random import randint as rni, choice, seed as sd


def createTree(pos, type):
    if type in ["oak", "birch"]:
        for i in range(5):
            output.append([[pos[0], pos[1]+i+1, pos[2], f"{type} vertical"]])
        
        output.append([[pos[0], pos[1]+6, pos[2], f"{type} leaves"]])
        output.append([[pos[0], pos[1]+7, pos[2], f"{type} leaves"]])
        output.append([[pos[0], pos[1]+7, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+7, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+6, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+5, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+4, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+6, pos[2]-2, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+5, pos[2]-2, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+4, pos[2]-2, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+6, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+5, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+4, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+6, pos[2]+2, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+5, pos[2]+2, f"{type} leaves"]])
        output.append([[pos[0], pos[1]+4, pos[2]+2, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+7, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+7, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+6, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+5, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+4, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-2, pos[1]+6, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-2, pos[1]+5, pos[2], f"{type} leaves"]])
        output.append([[pos[0]-2, pos[1]+4, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+6, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+5, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+4, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+2, pos[1]+6, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+2, pos[1]+5, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+2, pos[1]+4, pos[2], f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+4, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+5, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+6, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+4, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+5, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0]+1, pos[1]+6, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+4, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+5, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+6, pos[2]+1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+4, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+5, pos[2]-1, f"{type} leaves"]])
        output.append([[pos[0]-1, pos[1]+6, pos[2]-1, f"{type} leaves"]])


def genTerrain(seed, advanced, terrain_width, octaves=2, amplitude=6, period=48):
    output = []

    octaves = octaves
    noise = PerlinNoise(octaves=octaves, seed=seed)
    amp = amplitude
    period = period
    #generation
    landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]
    for position in range(terrain_width**2):
        x = floor(position / terrain_width)
        z = floor(position % terrain_width)
        y = floor(noise([x/period, z/period])*amp)
        landscale[int(x)][int(z)] = int(y)

        if advanced:
            output.append([x, y, z, "grass"])

            for i in range(4):
                output.append([x, y-i-1, z, "dirt"])

            for j in range(100):
                sd((seed//y-x**z+j**4))
                block = rni(0,1000)
                if j <= 50:
                    if block <= 820:
                        output.append([x, y+2-j, z, "stone"])
                    if block > 820 and block <= 860:
                        output.append([x, y+2-j, z, "copper ore"])
                    if block > 860 and block <= 900:
                        output.append([x, y+2-j, z, "coal ore"])
                    if block > 900 and block <= 935:
                        output.append([x, y+2-j, z, "iron ore"])
                    if block > 935 and block <= 955:
                        output.append([x, y+2-j, z, "gold ore"])
                    if block > 955 and block <= 975:
                       output.append([x, y+2-j, z, "redstone ore"])
                    if block > 975 and block <= 990:
                        output.append([x, y+2-j, z, "lapis ore"])
                    if block > 990 and block <= 995:
                        output.append([x, y+2-j, z, "emerald ore"])
                    if block > 995 and block <= 1000:
                        output.append([x, y+2-j, z, "diamond ore"])
                elif j > 50:
                    if block <= 820:
                        output.append([x, y, z, "deepslate"])
                    if block > 820 and block <= 860:
                        output.append([x, y+2-j, z, "deepslate copper ore"])
                    if block > 860 and block <= 900:
                        output.append([x, y+2-j, z, "deepslate coal ore"])
                    if block > 900 and block <= 935:
                        output.append([x, y+2-j, z, "deepslate iron ore"])
                    if block > 935 and block <= 955:
                        output.append([x, y+2-j, z, "deepslate gold ore"])
                    if block > 955 and block <= 975:
                       output.append([x, y+2-j, z, "deepslate redstone ore"])
                    if block > 975 and block <= 990:
                        output.append([x, y+2-j, z, "deepslate lapis ore"])
                    if block > 990 and block <= 995:
                        output.append([x, y+2-j, z, "deepslate emerald ore"])
                    if block > 995 and block <= 1000:
                        output.append([x, y+2-j, z, "deepslate diamond ore"])

            output.append([x, y-98, z, "bedrock"])

            sd(x**z//seed)

            if rni(1,256) == 4:
                trees = ["oak", "birch"]
                tree = choice(trees)
                createTree((x,y+7,z), tree)
        sd()
        return output