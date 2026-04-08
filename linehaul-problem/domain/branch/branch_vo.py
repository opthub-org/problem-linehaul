from dataclasses import dataclass

from domain.branch.branch_data import BranchData
from domain.node.node_data import NodeData


@dataclass(frozen=True)
class BranchVO:
    data: BranchData
    from_node: NodeData
    to_node: NodeData

    def __repr__(self):
        return str(self.data)

    @property
    def cost(self) -> float:
        return self.data.cost
