import csv
from pathlib import Path
from typing import Iterator

from .base_data import BaseData


class BaseCollection[T:BaseData]:
    DataClass:type[T] = BaseData

    def __init__(self):
        self.data_list: list[T] = []

    def __iter__(self)->Iterator[T]:
        return iter(self.data_list)

    @property
    def n_data(self)->int:
        return len(self.data_list)

    def read_csv(self, file_path: Path, encoding: str = "utf-8-sig") ->list[type[T]]:
        if not file_path.exists():
            raise FileNotFoundError(f"Error: {file_path} が見つかりません。")
        self.data_list = []

        with open(file_path, mode='r', encoding=encoding) as f:
            # DictReaderを作成
            reader = csv.DictReader(f)
            self.data_list = [self.DataClass.mapping(row) for row in reader]

        return self.data_list

    def from_json(self,js:list[dict]):
        self.data_list = [self.DataClass.mapping_by_key(data) for data in js]
