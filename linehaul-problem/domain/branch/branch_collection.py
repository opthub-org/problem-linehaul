
from domain.base import BaseCollection
from domain.branch.branch_data import BranchData
from domain.branch.branch_vo import BranchVO
from domain.node.node_collection import NodeCollection
from domain.node.node_data import NodeData
from domain.route.route_entity import RouteEntity

class BranchCollection(BaseCollection[BranchData]):

    DataClass = BranchData

    def __init__(self,node_collection:NodeCollection):
        super().__init__()
        self.nodes = node_collection
        self.entity_list:list[BranchVO] = []
        self.entity_dict :dict[tuple[NodeData,NodeData],BranchVO] = dict()


    def convert_to(self,dto_list:list[BranchData]):

        self.entity_list = []
        for d in dto_list:
            f_node = self.nodes.get_by_id(d.from_node)
            t_node = self.nodes.get_by_id(d.to_node)
            if f_node == t_node:
                continue
            self.entity_list.append(BranchVO(d, f_node, t_node))

        self.entity_dict = {(e.from_node, e.to_node): e
                            for e in self.entity_list}
    def is_connected(self,from_node:NodeData,to_node:NodeData)->bool:
        return (from_node, to_node) in self.entity_dict

    def get_branch_by_ft(self,from_:NodeData,to_:NodeData)->BranchVO:
        return self.entity_dict[(from_,to_)]

    def get_cost(self,route:RouteEntity)->int:
        total_cost = 0

        for from_, to_ in route.pairwise:
            key = (from_,to_)
            branch = self.entity_dict.get(key, None)
            if branch is None:
                raise ValueError(f"routeが接続されていません。{key}")
            total_cost += branch.cost

        return total_cost