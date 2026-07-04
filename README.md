# Cave Game
## A clone of Minecraft made by TT0tem4ik22 on python with using [ursina engine](https://github.com/pokepetter/ursina)
(README is being made right now, please wait)
### Installation
Download the script with using command ```$ git clone https://github.com/tt0tem4ik22-archuser/Cave-Game```<br>
Enter script folder with using command ```$ cd path/to/project/Cave-Game/```

#### Setting up venv
Create venv for the project: ```$ python -m venv *name*``` <br>
Activate it on Windows: ```$ *name*\Scripts\activate```<br>
Activate it on MacOS/Linus: ```$ source *name*/bin/activate```<br>
Deactivate it with ```$ deactivate```

#### Installing requirements 
If you activated venv then use command```python -m pip install -r requirements.txt```

### Usage
use ```python3 main.py``` to open main menu <br>
use ```python3 server.py argv1 argv2 argv3 argv4 argv5 argv6 argv7 argv8 argv9 argv10 argv11``` to start server <br>
use ```python3 singleplayer.py argv3 argv4 argv5 argv6 argv7 argv8 argv9 argv10 argv11``` to start server <br>
| Argument № | Description | Example | note |
| --- | --- | --- | --- |
| 1 | ip of server | 127.0.0.1 | Multiplayer only |
| 2 | port of server | 8888 | Multiplayer only |
| 3 | Toggle Advanced generation | *Enabled* or *Disabled* | |
| 4 | World seed | 1234567890 | Not required if №3 is *Disabled* |
| 5 | Perlin noise octaves | 2 | Not required if №3 is *Disabled* |
| 6 | Perlin noise period | 48 | Not required if №3 is *Disabled* |
| 7 | Perlin noise amplitude | 6 | Not required if №3 is *Disabled* |
| 8 | Toggle generate ores | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |
| 9 | Toggle generate trees | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |
| 10 | World width | 16 | Not required if №3 is *Disabled* |
| 11 | Toggle generate only terrain | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |
---
use ```python3 client.py ip port``` to start client and join to server <br>

### Task list
- [ ] Fully migrate all features from the Old Branch to the new Singleplayer.
- [ ] Fully migrate all features from the Old Branch to the new Multiplayer.
- [ ] Finish creating the main menu
- [ ] Select resource packs in-game
- [ ] Find a better class for Voxel than [Entity](https://github.com/pokepetter/ursina/blob/master/ursina/entity.py), because [Entity](https://github.com/pokepetter/ursina/blob/master/ursina/entity.py) is not optimized
- [ ] Add mobs
- [ ] Add survival mode
- [ ] Sort out the shit I wrote