from .node_data import NodeData
from ..base.base_collection import BaseCollection


class NodeCollection(BaseCollection[NodeData]):
    DataClass = NodeData

    def __init__(self):
        super().__init__()
        self.data_dict:dict[int,NodeData] = dict()

    def convert_to(self,dto_list:list[NodeData]):
        self.data_list = dto_list
        self.data_dict = {d.id: d for d in self.data_list}

    def get_by_id(self, id_: int) -> NodeData:
        return self.data_dict[id_]
