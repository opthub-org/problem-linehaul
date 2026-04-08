from dataclasses import dataclass, field

from domain.node.node_data import NodeData
from .order_data import OrderData

@dataclass(frozen=True)
class OrderVO:
    id: int
    from_node: NodeData
    to_node: NodeData
    weight: float
    sd:float

    def __repr__(self):
        return f"{self.from_node}→{self.to_node}"

    @classmethod
    def from_dto(cls,dto:OrderData,from_:NodeData,to_:NodeData):
        return cls(id=dto.id,
                   from_node=from_,
                   to_node=to_,
                   weight=dto.weight,
                   sd=dto.sd)

    @property
    def is_same_ft(self)-> bool:
        return self.from_node == self.to_node
