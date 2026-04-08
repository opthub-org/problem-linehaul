from typing import Type

from infra.io.order.order_reader import OrderReader
from infra.path_setting import PathSetting
from infra.io.network import NetWorkReader
from domain.network.network_entity import NetWork
from domain.route.route_table import RouteTable
from domain.order.order_collection import OrderCollection
from domain.transport_cost.branch_transport_cost_collection import TransportCostCollection


class CostEvaluator:

    def __init__(self,v_capa:float):
        self.vehicle_capacity:float = v_capa
        self.network: NetWork = NetWork()
        self.route_table: RouteTable | None = None
        self.order_collection = OrderCollection()
        self.branch_transport_costs: TransportCostCollection = TransportCostCollection()

    @property
    def branches(self):
        return self.network.branch

    @property
    def nodes(self):
        return self.network.node

    def initialize(self, path_setting: PathSetting):
        network_reader =  NetWorkReader(path_setting.network)
        self.network.read(network_reader)

        order_reader = OrderReader(path_setting.order)
        self.order_collection.read(order_reader)
        self.order_collection.convert_vo(self.nodes)

        self.route_table = RouteTable(self.network)

    def set_route_table(self, js: list):
        self.route_table.set_list(js)


    def eveluate(self) -> float:

        self.branch_transport_costs.initialize(self.branches,v_capa=self.vehicle_capacity)

        for order in self.order_collection.vo_list:
            if order.is_same_ft:
                continue
            route = self.route_table.get_route_by_order(order)
            for f, t in route.pairwise:
                branch = self.branches.get_branch_by_ft(f, t)
                cost = self.branch_transport_costs.get_cost(branch)
                cost.order_list.append(order)

        return self.branch_transport_costs.calc_total_cost()
