from pathlib import Path

from domain.order.i_order_reader import IOrderReader
from domain.order.order_data import OrderData
from .virtual_prefecture_flow_dto import VirtualPrefecturesFlowDTO


class NewOrderReader(IOrderReader):
    DataClass = VirtualPrefecturesFlowDTO

    def __init__(self, csv_path: Path):
        super().__init__()
        self.csv_path = csv_path
        self.encoding = 'utf_8_sig'

    def read(self):
        data: list[VirtualPrefecturesFlowDTO] = self._read_csv(self.csv_path, self.encoding)
        for i, d in enumerate(data):
            od = OrderData(id=i + 1,
                           from_node=d.from_node,
                           to_node=d.to_node,
                           weight=d.virtual_load,
                           sd=d.standard_deviation)
            self.order.append(od)
        return self.order
