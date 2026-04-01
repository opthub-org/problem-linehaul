from dataclasses import dataclass, field

from domain.node.node_data import NodeData
from domain.base.base_data import BaseData

@dataclass(frozen=True)
class OrderData(BaseData):
    id_: int = field(metadata={"key": "id"})
    from_node: NodeData = field(metadata={"key": "from"})
    to_node: NodeData = field(metadata={"key": "to"})
    weight: int = field(metadata={"key": "weight"})

    def __repr__(self):
        return f"{self.from_node}→{self.to_node}"
