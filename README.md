# civ5map-tools
Tools for reading Civilization 5 map files

I'm using Kaitai Struct to define the structure of binary file formats, and I'll put the latest compiled python version in this repo.

Files
--
`civ5map.ksy` Kaitai Struct definition for .civ5map files

`civ5map.py` Python module compiled by Kaitai Struct compiler

`civ5map_client.py` Sample client that prints out the land of a civ5map. If you set up everything properly, you should see some recognizeable shapes when you give it a civ5map.
