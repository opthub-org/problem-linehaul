from typing import FrozenSet

from domain.base import BaseCollection
from domain.branch.branch_data import BranchData
from domain.branch.branch_entity import BranchEntity
from domain.node.node_collection import NodeCollection
from domain.node.node_data import NodeData
from domain.route.route_entity import RouteEntity

class BranchCollection(BaseCollection[BranchData]):

    DataClass = BranchData

    def __init__(self,node_collection:NodeCollection):
        super().__init__()
        self.nodes = node_collection
        self.entity_list:list[BranchEntity] = []
        self.entity_dict :dict[FrozenSet[NodeData],BranchEntity] = dict()

    def from_json(self,js:list[dict]):
        super().from_json(js)
        self.entity_list =[]
        for d in self.data_list:
            f_node = self.nodes.get_by_name(d.from_node)
            t_node = self.nodes.get_by_name(d.to_node)
            self.entity_list.append(BranchEntity(d, f_node, t_node))

        self.entity_dict = {frozenset((e.from_node,e.to_node)):e
                            for e in self.entity_list}

    def get_branch_by_ft(self,from_:NodeData,to_:NodeData)->BranchEntity:
        return self.entity_dict[frozenset((from_,to_))]

    def get_cost(self,route:RouteEntity)->int:
        total_cost = 0

        for from_, to_ in route.pairwise:
            key = frozenset((from_,to_))
            branch = self.entity_dict.get(key, None)
            if branch is None:
                raise ValueError(f"routeが接続されていません。{key}")
            total_cost += branch.cost

        return total_cost