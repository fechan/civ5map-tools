import civ5map

path = "/path/to/map.civ5map"
map = civ5map.Civ5map.from_file(path)
terrains = map.header.terrain_list.values
for row in map.mapdata.plot_matrix[::-1]:
    for plot in row.plot_list:
        if terrains[plot.terrain_type_id] == "TERRAIN_OCEAN" or terrains[plot.terrain_type_id] == "TERRAIN_COAST":
            print(" ", end='')
        else:
            print("#", end='')
    print("")