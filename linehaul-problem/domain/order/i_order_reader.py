from abc import ABC
from domain.base.i_reader import IReader
from .order_data import OrderData

class IOrderReader(IReader,ABC):

    def __init__(self):
        self.order:list[OrderData] = []

