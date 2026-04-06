import json
from os import PathLike
from domain.branch.branch_collection import BranchCollection
from domain.node.node_collection import NodeCollection


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

    def read(self, file_path: PathLike):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.node.from_json(data["nodes"])
        self.branch.from_json(data["branches"])
