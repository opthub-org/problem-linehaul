from __future__ import annotations
from typing import TYPE_CHECKING,Iterator

from domain.base import BaseCollection
from domain.order.order_data import OrderData
from .i_order_reader import IOrderReader
from .order_vo import OrderVO

if TYPE_CHECKING:
    from domain.node.node_collection import NodeCollection

class OrderCollection(BaseCollection[OrderData]):

    DataClass = OrderData

    def __init__(self):
        super().__init__()
        self.vo_list:list[OrderVO] = []

    def read(self,reader:IOrderReader):
        reader.read()
        self.data_list = reader.order

    def convert_vo(self,node_collection:NodeCollection):
        self.vo_list=[]
        for dto in self.data_list:
            f_node = node_collection.get_by_id(dto.from_node)
            t_node = node_collection.get_by_id(dto.to_node)
            vo=OrderVO.from_dto(dto, f_node, t_node)
            self.vo_list.append(vo)