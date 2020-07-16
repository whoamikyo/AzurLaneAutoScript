from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('A1')
MAP.shape = 'I6'
MAP.camera_data = ['D2', 'D4', 'F2', 'F4']
MAP.camera_data_spawn_point = []
MAP.map_data = """
    Me -- -- ME -- -- ME -- Me
    -- -- -- -- -- -- -- -- MB
    ME -- ME ++ ++ ME -- -- --
    -- -- ++ ++ ++ -- -- ME Me
    SP -- ++ ++ -- MS -- ++ ++
    SP SP -- -- -- ME MB ++ ++
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 1},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2, 'boss': 1},
    {'battle': 5, 'enemy': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
    = MAP.flatten()


class Config:
    SUBMARINE = 0

    POOR_MAP_DATA = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_SIREN = True
    MAP_HAS_DYNAMIC_RED_BORDER = False
    MAP_SIREN_COUNT = 1

    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (100, 255 - 24),
        'width': 1,
        'prominence': 10,
        'distance': 35,
    }
    EDGE_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (255 - 24, 255),
        'prominence': 2,
        'distance': 50,
        'wlen': 1000
    }


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        return self.battle_default()

    def battle_4(self):
        return self.fleet_boss.clear_boss()
