import csv
from pathlib import Path

from .base_data import BaseData


class BaseCollection[T:BaseData]:
    DataClass:type[T] = BaseData

    def __init__(self):
        self.data_list: list[T] = []

    @property
    def n_data(self)->int:
        return len(self.data_list)