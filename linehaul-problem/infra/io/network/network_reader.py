import json
from pathlib import Path

from domain.branch.branch_data import BranchData
from domain.network.i_network_reader import INetworkReader
from domain.node.node_data import NodeData

class NetWorkReader(INetworkReader):

    def __init__(self,json_path:Path):
        super().__init__()
        self.json_path = json_path

    def read(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            js = json.load(f)
        self.node = [NodeData.mapping_by_key(data) for data in js["nodes"]]
        self.branch = [BranchData.mapping_by_key(data) for data in js["branches"]]