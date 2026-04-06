from dataclasses import dataclass, field

from domain.base.base_data import BaseData

@dataclass(frozen=True)
class BranchData(BaseData):
    from_node: int = field(metadata={"key": "from"})
    to_node: int = field(metadata={"key": "to"})
    cost: float = field(metadata={"key": "cost"})
    capacity: float = field(metadata={"key":"capa"},default=0)

    def __repr__(self):
        return f"{self.from_node}⇔{self.to_node}"