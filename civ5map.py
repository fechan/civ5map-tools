# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Civ5map(KaitaiStruct):
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
            self.unknown = self._io.read_u4le()
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
            if self.version == 12:
                self.maybe_lua_params = self._io.read_bytes(36)

            if self.version == 12:
                self.lua_script_len = self._io.read_u4le()

            if self.version == 12:
                self._raw_lua_script = self._io.read_bytes(self.lua_script_len)
                io = KaitaiStream(BytesIO(self._raw_lua_script))
                self.lua_script = self._root.Header.NullTerminatedStr(io, self, self._root)

            self.map_name = (self._io.read_bytes(self.map_name_len)).decode(u"utf-8")
            self.map_description = (self._io.read_bytes(self.map_description_len)).decode(u"utf-8")
            if self.version >= 11:
                self.string3_len = self._io.read_u4le()

            if self.version >= 11:
                self.string3 = (self._io.read_bytes(self.string3_len)).decode(u"utf-8")


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
                    self.values.append((self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8"))
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
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.terrain_type_id = self._io.read_bytes(1)
                self.resource_type_id = self._io.read_bytes(1)
                self.feature1_type_id = self._io.read_bytes(1)
                self.river = self._io.read_bytes(1)
                self.elevation = self._io.read_bytes(1)
                self.continent = self._io.read_bytes(1)
                self.feature2_type_id = self._io.read_bytes(1)
                self.unknown = self._io.read_bytes(1)




