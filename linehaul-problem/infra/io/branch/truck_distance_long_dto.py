from dataclasses import dataclass, field

from domain.base import BaseData

@dataclass(frozen=True)
class TruckDistanceLongDTO(BaseData):
    origin_prefecture_code:int =field(metadata={"key":"origin_prefecture_code"})
    destination_prefecture_code:int = field(metadata={"key":"destination_prefecture_code"})
    time_min:float = field(metadata={"key":"time_min"})