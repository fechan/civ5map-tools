# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Civ5map(KaitaiStruct):
    """Many of Civilization 5's maps are in civ5map format, and encodes terrain and
    sometimes resources on the map plots. Scenario data is also encoded in some
    civ5map files, although this does not currently parse such data.
    
    Civ5maps can be accompanied by lua files which defines advanced behavior for
    world gen on top of what's already in the civ5map.
    
    There are three versions of the format identified in this file- Pre-B (e.g. 7
    and A), B, and C. The latest version of Civ can read all of them. Pre-B is
    the base version. Version B has some additional information about the map in
    the header (string3). Version C is the only one I've seen that has a mod_data
    length greater than 0.
    
    Examples of official Firaxis maps with these versions...
    Pre-B (7) - <Civ 5 Install Location>/steamassets/assets/maps/asia.civ5map
    B - <Civ 5 Install Location>/steamassets/assets/maps/m_ancientlake.civ5map
    C - <Civ 5 Install Location>/steamassets/assets/maps/earth_duel.civ5map
    
    .. seealso::
       Source - https://forums.civfanatics.com/threads/civ5map-file-format.418566/
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._root.Header(self._io, self, self._root)
        self.mapdata = self._root.Mapdata(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.has_scenario_data = self._io.read_bits_int(4)
            self.version = self._io.read_bits_int(4)
            self._io.align_to_byte()
            self.width = self._io.read_u4le()
            self.height = self._io.read_u4le()
            self.players = self._io.read_bytes(1)
            self.misc_settings_head = self._io.read_bits_int(5)
            self.random_goodies = self._io.read_bits_int(1) != 0
            self.random_resources = self._io.read_bits_int(1) != 0
            self.world_wrap = self._io.read_bits_int(1) != 0
            self._io.align_to_byte()
            self.misc_settings_tail = self._io.read_bytes(3)
            self.terrain_list_len = self._io.read_u4le()
            self.feature1_list_len = self._io.read_u4le()
            self.feature2_list_len = self._io.read_u4le()
            self.resource_list_len = self._io.read_u4le()
            self.mod_data_len = self._io.read_u4le()
            self.map_name_len = self._io.read_u4le()
            self.map_description_len = self._io.read_u4le()
            self._raw_terrain_list = self._io.read_bytes(self.terrain_list_len)
            io = KaitaiStream(BytesIO(self._raw_terrain_list))
            self.terrain_list = self._root.Header.NullTerminatedStr(io, self, self._root)
            self._raw_feature1_list = self._io.read_bytes(self.feature1_list_len)
            io = KaitaiStream(BytesIO(self._raw_feature1_list))
            self.feature1_list = self._root.Header.NullTerminatedStr(io, self, self._root)
            self._raw_feature2_list = self._io.read_bytes(self.feature2_list_len)
            io = KaitaiStream(BytesIO(self._raw_feature2_list))
            self.feature2_list = self._root.Header.NullTerminatedStr(io, self, self._root)
            self._raw_resource_list = self._io.read_bytes(self.resource_list_len)
            io = KaitaiStream(BytesIO(self._raw_resource_list))
            self.resource_list = self._root.Header.NullTerminatedStr(io, self, self._root)
            self.mod_data = self._io.read_bytes(self.mod_data_len)
            self.map_name = (self._io.read_bytes(self.map_name_len)).decode(u"UTF-8")
            self.map_description = (self._io.read_bytes(self.map_description_len)).decode(u"UTF-8")
            if self.version >= 11:
                self.string3_len = self._io.read_u4le()

            if self.version >= 11:
                self.string3 = (self._io.read_bytes(self.string3_len)).decode(u"UTF-8")


        class NullTerminatedStr(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.values = []
                i = 0
                while not self._io.is_eof():
                    self.values.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                    i += 1




    class Mapdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.plot_matrix = [None] * (self._root.header.height)
            for i in range(self._root.header.height):
                self.plot_matrix[i] = self._root.Mapdata.PlotRow(self._io, self, self._root)


        class PlotRow(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.plot_list = [None] * (self._root.header.width)
                for i in range(self._root.header.width):
                    self.plot_list[i] = self._root.Mapdata.Plot(self._io, self, self._root)



        class Plot(KaitaiStruct):
            """whatever_type_id is an index into the corresponding list in 
            the header. With the exception of terrain, it can be 0xFF,
            which represents nonetype.
            """

            class Elevation(Enum):
                none = 0
                hill = 1
                mountain = 2

            class Continent(Enum):
                none = 0
                americas = 1
                asia = 2
                africa = 3
                europe = 4
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.terrain_type_id = self._io.read_u1()
                self.resource_type_id = self._io.read_u1()
                self.feature1_type_id = self._io.read_u1()
                self.river = self._root.Mapdata.Plot.River(self._io, self, self._root)
                self.elevation = self._root.Mapdata.Plot.Elevation(self._io.read_u1())
                self.continent = self._root.Mapdata.Plot.Continent(self._io.read_u1())
                self.feature2_type_id = self._io.read_u1()
                self.resource_amount = self._io.read_u1()

            class River(KaitaiStruct):
                """Represents rivers defined by a tile's hex. Rivers are
                defined by edges of hexes.
                    /\
                   |  | East
                    \/
                  SW  SE
                Because hexes tesselate, defining only SW-SE-E edges
                of the rivers can define rivers for all valid river spots.
                """
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.unknown = self._io.read_bits_int(5)
                    self.southwest_edge = self._io.read_bits_int(1) != 0
                    self.southeast_edge = self._io.read_bits_int(1) != 0
                    self.east_edge = self._io.read_bits_int(1) != 0





