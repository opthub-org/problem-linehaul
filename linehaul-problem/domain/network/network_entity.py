import json
from os import PathLike
from domain.branch.branch_collection import BranchCollection
from domain.node.node_collection import NodeCollection
from .i_network_reader import INetworkReader

class NetWork:

    def __init__(self):
        self.node: NodeCollection = NodeCollection()
        self.branch: BranchCollection = BranchCollection(self.node)

    @property
    def n_node(self) -> int:
        return self.node.n_data

    @property
    def n_branch(self) -> int:
        return self.branch.n_data

    def read(self, reader:INetworkReader):
        reader.read()

        self.node.convert_to(reader.node)
        self.branch.convert_to(reader.branch)
