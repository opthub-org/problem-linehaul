from dataclasses import dataclass, field

from domain.base.base_data import BaseData

@dataclass(frozen=True)
class OrderData(BaseData):
    id_: int = field(metadata={"key": "id"})
    from_node: int = field(metadata={"key": "origin_prefecture_code"})
    to_node: int = field(metadata={"key": "destination_prefecture_code"})
    weight: float = field(metadata={"key": "virtual_load"})
    sd:float = field(metadata={"key":"standard_deviation"} )

    def __repr__(self):
        return f"{self.from_node}→{self.to_node}"
