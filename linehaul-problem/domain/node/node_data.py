from dataclasses import dataclass,field

from domain.base.base_data import BaseData

@dataclass(frozen=True)
class NodeData(BaseData):
    id:int = field(metadata={"key":"prefecture_code"})
    name:str = field(metadata={"key":"prefecture_name"})

    def __repr__(self):
        return f"{self.id:02}:{self.name}"


