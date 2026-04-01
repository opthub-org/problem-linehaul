from dataclasses import dataclass,field

from domain.base.base_data import BaseData

@dataclass(frozen=True)
class NodeData(BaseData):
    name:str = field(metadata={"key":"name"})

    def __repr__(self):
        return self.name


