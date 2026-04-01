import json
from pathlib import Path

from domain.node.node_data import NodeData
from .route_entity import RouteEntity

class RouteTable:

    def __init__(self, node_list: list[NodeData]):
        self.table: dict[tuple[NodeData, NodeData], NodeData] = dict()
        self.node_list: list[NodeData] = node_list
        self.node_dict:dict[str,NodeData] = {n.name:n for n in  node_list}

    def read_json(self, file_path: Path):
        self.table = dict()
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.set_list(data)

    def set_list(self,data:list):
        for d in data:
            from_ = self.node_dict.get(d["from"],None)
            nexts = d["next"]
            for to_, _next in zip(self.node_list, nexts):
                if from_ == to_:
                    continue
                __next = self.node_dict.get(_next,None)
                if __next is None:
                    raise ValueError(f"{_next}はノードリストに登録されていません")
                self.table[(from_, to_)] = __next

    def get_next(self, from_: NodeData, to_: NodeData) -> NodeData:
        return self.table[(from_, to_)]

    def get_route(self, from_: NodeData, to_: NodeData) -> RouteEntity:
        if from_ == to_:
            raise ValueError(f"fromとtoが同じです。{from_}")

        route = [from_]
        visited = {from_}
        curr = from_

        while curr != to_:
            next_ = self.get_next(curr, to_)
            route.append(next_)

            if next_ in visited:
                raise ValueError(f"{from_}から{to_}へのルートに循環があります。{route}")
            visited.add(next_)
            if next_ == to_:
                return RouteEntity(route)
            curr = next_
        raise ValueError(f"{from_}から{to_}へのルートが存在しません。")
