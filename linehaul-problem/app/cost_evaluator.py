from domain.network.network_entity import NetWork
from domain.route.route_table import RouteTable
from domain.order.order_collection import OrderCollection

from infra.path_setting import PathSetting


class CostEvaluator:
    truck_capa: int = 10

    def __init__(self):
        self.network: NetWork = NetWork()
        self.route_table: RouteTable | None = None
        self.order_collection = OrderCollection()

    @property
    def branches(self):
        return self.network.branch

    @property
    def nodes(self):
        return self.network.node

    def initialize(self, path_setting: PathSetting):
        self.network.read(path_setting.network)

        self.order_collection.read_csv(path_setting.order)
        self.route_table = RouteTable(self.network.node.data_list)

    def set_route_table(self, js: list):
        self.route_table.set_list(js)

    def eveluate(self) -> float:

        load_dict = dict()
        for order in self.order_collection:
            route = self.route_table.get_route(order.from_node, order.to_node)
            for f, t in route.pairwise:
                load_dict[(f, t)] = load_dict.get((f, t), 0) + order.weight
        total_cost = 0.0
        for (f, t), load in load_dict.items():
            branch = self.branches.get_branch_by_ft(f, t)
            n_truck = (load + self.truck_capa - 1) // self.truck_capa  # weight/t_capaで切り上げ
            total_cost += branch.cost * n_truck
        return total_cost
