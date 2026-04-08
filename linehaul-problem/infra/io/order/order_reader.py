from pathlib import Path

from domain.order.i_order_reader import IOrderReader
from domain.order.order_data import OrderData


class OrderReader(IOrderReader):

    DataClass = OrderData

    def __init__(self,csv_path:Path):
        super().__init__()
        self.csv_path = csv_path
        self.encoding = 'utf_8_sig'

    def read(self):
        self.order = self._read_csv(self.csv_path,self.encoding)
        return self.order
