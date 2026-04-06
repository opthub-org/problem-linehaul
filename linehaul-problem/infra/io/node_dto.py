from dataclasses import dataclass, field
from domain.node.node_data import NodeData


@dataclass(frozen=True)
class NodeDTO(NodeData):
    latitude: float = field(metadata={"key": "latitude"})
    longitude: float = field(metadata={"key": "latitude"})
