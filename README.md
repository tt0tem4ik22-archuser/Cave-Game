# Cave Game
## A clone of Minecraft made by TT0tem4ik22 on python with using [ursina engine](https://github.com/pokepetter/ursina)
(README is being made right now, please wait)
### Installation

### Usage
use ```python3 main.py``` to open main menu <br>
use ```python3 server.py argv1 argv2 argv3 argv4 argv5 argv6 argv7 argv8 argv9 argv10 argv11``` to start server <br>
| Argument № | Description | Example | note |
| --- | --- | --- | --- |
| 1 | ip of server | 127.0.0.1 | |
| 2 | port of server | 8888 | |
| 3 | Toggle Advanced generation | *Enabled* or *Disabled* | |
| 4 | World seed | 1234567890 | Not required if №3 is *Disabled* |
| 5 | Perlin noise octaves | 2 | Not required if №3 is *Disabled* |
| 6 | Perlin noise period | 48 | Not required if №3 is *Disabled* |
| 7 | Perlin noise amplitude | 6 | Not required if №3 is *Disabled* |
| 8 | Toggle generate ores | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |
| 9 | Toggle generate trees | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |
| 10 | World width | 16 | Not required if №3 is *Disabled* |
| 11 | Toggle generate only terrain | *Enabled* or *Disabled* | Not required if №3 is *Disabled* |

### Task list
- [ ] Fully migrate all features from the Old Branch to the new Singleplayer.
- [ ] Fully migrate all features from the Old Branch to the new Multiplayer.
- [ ] Finish creating the main menu
- [ ] Select resource packs in-game
- [ ] Find a better class for Voxel than [Entity](https://github.com/pokepetter/ursina/blob/master/ursina/entity.py), because [Entity](https://github.com/pokepetter/ursina/blob/master/ursina/entity.py) is not optimized
- [ ] Add mobs
- [ ] Add survival mode