from generation import terrain_width

BREAK = "left mouse down"
SET = "right mouse down"
COPY = "middle mouse down"
EXIT = "escape"
RTP = "g"
NOCLIP = "v"
SIT = "left shift"
SPRINT = "left control"
SAVE_COORD = "z"
LOAD_COORD = "x"
INV = "e"
FIRST_THIRD_PERSON = "f"
SAVE_LEVEL = "p"
LOAD_LEVEL = "l"
SHOW_CONTROLS = "m"
PLANT_TREE = "n"

controls_text = f"""W: Go front 
A: Go left
S: Go backward
D: Go Right
Space: jump

{BREAK}: remove block
{SET}: place block

{INV}: open/close inventory

{SAVE_COORD}: save player position and rotation (not saving world)
{LOAD_COORD}: load player position

{RTP}: random teleportation from 0 to {terrain_width} for x and z

{NOCLIP}: Noclip toggle

[Hold] {SIT}: duck
[Hold] {SPRINT}: run 

{FIRST_THIRD_PERSON}: turn on/off third person

{SAVE_LEVEL}: save world into save.save 
{LOAD_LEVEL}: load world (unable)

{PLANT_TREE}: plant tree

{SHOW_CONTROLS}: Open this text again"""