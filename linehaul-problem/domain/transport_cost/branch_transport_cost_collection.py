from __future__ import annotations
from typing import TYPE_CHECKING

from .branch_transport_cost import BranchTransportCost

if TYPE_CHECKING:
    from domain.branch.branch_vo import BranchVO
    from domain.branch.branch_collection import BranchCollection


class TransportCostCollection:

    def __init__(self):
        self.entity_dict: dict[BranchVO, BranchTransportCost] = dict()

    def initialize(self, branches:BranchCollection,v_capa:float):
        self.entity_dict = dict()
        for branch in branches.entity_list:
            branch_cost = BranchTransportCost(branch,vehicle_capacity=v_capa)
            self.entity_dict[branch] = branch_cost

    def get_cost(self,branch:BranchVO)->BranchTransportCost:
        if (cost := self.entity_dict.get(branch)) is None:
            raise KeyError(f"{branch}の移動が定義されていません。")
        return cost

    def calc_total_cost(self):
        return sum(cost.get_cost() for cost in self.entity_dict.values())