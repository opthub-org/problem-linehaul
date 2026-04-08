from dataclasses import dataclass, field

from domain.base import BaseData


@dataclass(frozen=True)
class VirtualPrefecturesFlowDTO(BaseData):
    from_node: int = field(metadata={"key": "origin_prefecture_code"})
    to_node: int = field(metadata={"key": "destination_prefecture_code"})
    virtual_load: float = field(metadata={"key": "virtual_load"})
    standard_deviation: float = field(metadata={"key": "standard_deviation"})
