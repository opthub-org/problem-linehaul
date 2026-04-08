from abc import ABC,abstractmethod
import csv
from pathlib import Path

from domain.base import BaseData


class IReader[T:BaseData](ABC):

    DataClass:type[T]

    @abstractmethod
    def read(self):
        raise NotImplementedError()

    def _read_csv(self,file_path: Path,encoding:str="utf_8_sig")->list[T]:
        if not file_path.exists():
            raise FileNotFoundError(f"Error: {file_path} が見つかりません。")
        self.data_list = []

        with open(file_path, mode='r', encoding=encoding) as f:
            # DictReaderを作成
            reader = csv.DictReader(f)
            self.data_list = [self.DataClass.mapping(row) for row in reader]

        return self.data_list