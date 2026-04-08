import csv
from pathlib import Path

from domain.branch.branch_data import BranchData
from domain.network.i_network_reader import INetworkReader
from domain.node.node_data import NodeData
from infra.io.branch.truck_distance_long_dto import TruckDistanceLongDTO


class NewNetworkReader(INetworkReader):

    def __init__(self,
                 prefectures_path: Path,
                 truck_distance_time_long: Path,
                 virtual_prefecture_flows: Path):
        super().__init__()
        self.prefectures_path = prefectures_path
        self.truck_distance_time_long = truck_distance_time_long
        self.virtual_prefecture_flows = virtual_prefecture_flows

    def read(self):
        self._read_prefecture()
        self._read_truck_distance()

    def _read_prefecture(self):
        with open(self.prefectures_path, mode='r', encoding='utf_8_sig') as f:
            reader = csv.DictReader(f)
            self.node = [NodeData.mapping(row) for row in reader]

    def _read_truck_distance(self):
        with open(self.truck_distance_time_long, mode='r', encoding='utf_8_sig') as f:
            reader = csv.DictReader(f)
            truck_distance_data_list = [TruckDistanceLongDTO.mapping(row) for row in reader]

        for tdd in truck_distance_data_list:
            cost = 80000 * tdd.time_min / 480
            bd = BranchData(from_node=tdd.origin_prefecture_code,
                            to_node=tdd.destination_prefecture_code,
                            cost=cost)
            self.branch.append(bd)

