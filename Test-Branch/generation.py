# from numpy import floor
# from perlin_noise import PerlinNoise
# from random import randint as rni, choice


# def create_tree(pos, type):
# 	if type in ["oak", "birch"]:
# 	    for i in range(5):
# 	        output.append([pos[0], pos[1]+i+1, pos[2], blocks_textures[f"{type} vertical"]])
	    
# 	    output.append([pos[0], pos[1]+6, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+7, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+7, pos[2]+1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+7, pos[2]-1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+6, pos[2]-1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+5, pos[2]-1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+4, pos[2]-1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+6, pos[2]-2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+5, pos[2]-2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+4, pos[2]-2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+6, pos[2]+1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+5, pos[2]+1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+4, pos[2]+1, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+6, pos[2]+2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+5, pos[2]+2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0], pos[1]+4, pos[2]+2, blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0]+1, pos[1]+7, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0]-1, pos[1]+7, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0]-1, pos[1]+6, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0]-1, pos[1]+5, pos[2], blocks_textures[f"{type} leaves"]])
# 	    output.append([pos[0]-1, pos[1]+4, pos[2], blocks_textures[f"{type} leaves"]])
# 	    voxel = Voxel(position=(pos[0]-2,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-2,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-2,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+2,pos[1]+6,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+2,pos[1]+5,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+2,pos[1]+4,pos[2]), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+4,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+5,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]+1,pos[1]+6,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+4,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+5,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+6,pos[2]+1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+4,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+5,pos[2]-1), texture=blocks_textures[f"{type} leaves"])
# 	    voxel = Voxel(position=(pos[0]-1,pos[1]+6,pos[2]-1), texture=blocks_textures[f"{type} leaves"])



# def genTerrain(seed, advanced, octaves=2, amplitude=6, period=48):
# 	output = []

# 	octaves = octaves
#     noise = PerlinNoise(octaves=octaves, seed=seed)
#     amp = amplitude
#     period = period
#     #generation
#     landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]
#     for position in range(terrain_width**2):
#         x = floor(position / terrain_width)
#         z = floor(position % terrain_width)
#         y = floor(noise([x/period, z/period])*amp)
#         landscale[int(x)][int(z)] = int(y)

#         if advanced:
#         	output.append([x, y, z, blocks_textures["grass"]])

#             for i in range(4):
#                 output.append([x, y-i-1, z, blocks_textures["dirt"]])

#             for j in range(100):
#                 random.seed((seed//y-x**z+j**4))
#                 block = rni(0,1000)
#                 if j <= 50:
#                     if block <= 820:
#                         voxel = Voxel(texture=blocks_textures["stone"], position=(x,int(y+2-j),z))
#                     if block > 820 and block <= 860:
#                         voxel = Voxel(texture=blocks_textures["copper ore"], position=(x,int(y+2-j),z))
#                     if block > 860 and block <= 900:
#                         voxel = Voxel(texture=blocks_textures["coal ore"], position=(x,int(y+2-j),z))
#                     if block > 900 and block <= 935:
#                         voxel = Voxel(texture=blocks_textures["iron ore"], position=(x,int(y+2-j),z))
#                     if block > 935 and block <= 955:
#                         voxel = Voxel(texture=blocks_textures["gold ore"], position=(x,int(y+2-j),z))
#                     if block > 955 and block <= 975:
#                         voxel = Voxel(texture=blocks_textures["redstone ore"], position=(x,int(y+2-j),z))
#                     if block > 975 and block <= 990:
#                         voxel = Voxel(texture=blocks_textures["lapis ore"], position=(x,int(y+2-j),z))
#                     if block > 990 and block <= 995:
#                         voxel = Voxel(texture=blocks_textures["emerald ore"], position=(x,int(y+2-j),z))
#                     if block > 995 and block <= 1000:
#                         voxel = Voxel(texture=blocks_textures["diamond ore"], position=(x,int(y+2-j),z))
#                 elif j > 50:
#                     if block <= 820:
#                         voxel = Voxel(texture=blocks_textures["deepslate"], position=(x,int(y+2-j),z))
#                     if block > 820 and block <= 860:
#                         voxel = Voxel(texture=blocks_textures["deepslate copper ore"], position=(x,int(y+2-j),z))
#                     if block > 860 and block <= 900:
#                         voxel = Voxel(texture=blocks_textures["deepslate coal ore"], position=(x,int(y+2-j),z))
#                     if block > 900 and block <= 935:
#                         voxel = Voxel(texture=blocks_textures["deepslate iron ore"], position=(x,int(y+2-j),z))
#                     if block > 935 and block <= 955:
#                         voxel = Voxel(texture=blocks_textures["deepslate gold ore"], position=(x,int(y+2-j),z))
#                     if block > 955 and block <= 975:
#                         voxel = Voxel(texture=blocks_textures["deepslate redstone ore"], position=(x,int(y+2-j),z))
#                     if block > 975 and block <= 990:
#                         voxel = Voxel(texture=blocks_textures["deepslate lapis ore"], position=(x,int(y+2-j),z))
#                     if block > 990 and block <= 995:
#                         voxel = Voxel(texture=blocks_textures["deepslate emerald ore"], position=(x,int(y+2-j),z))
#                     if block > 995 and block <= 1000:
#                         voxel = Voxel(texture=blocks_textures["deepslate diamond ore"], position=(x,int(y+2-j),z))

#             output.append([x, y-98, z, blocks_textures["bedrock"]])

#             random.seed(x**z//seed)

#             if rni(1,256) == 4:
#                 trees = ["oak", "birch"]
#                 tree = choice(trees)
#                 create_tree((x,y+7,z), tree)
#         random.seed()

def create_tree(pos, type):
	return [2,1,1,"dirt"]
def genTerrain(seed, advanced, octaves=2, amplitude=6, period=48):
	return [[0,0,0,"grass"]]

