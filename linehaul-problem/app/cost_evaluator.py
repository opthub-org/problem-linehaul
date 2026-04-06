from infra.path_setting import PathSetting
from domain.network.network_entity import NetWork
from domain.route.route_table import RouteTable
from domain.order.order_collection import OrderCollection
from domain.transport_cost.branch_transport_cost_collection import TransportCostCollection


class CostEvaluator:

    def __init__(self):
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
        self.network.read(path_setting.network)

        self.order_collection.read_csv(path_setting.order)
        self.order_collection.convert_vo(self.nodes)

        self.route_table = RouteTable(self.network.node.data_list)

    def set_route_table(self, js: list):
        self.route_table.set_list(js)


    def eveluate(self) -> float:

        self.branch_transport_costs.initialize(self.branches)

        for order in self.order_collection.vo_list:
            route = self.route_table.get_route_by_order(order)
            for f, t in route.pairwise:
                branch = self.branches.get_branch_by_ft(f, t)
                cost = self.branch_transport_costs.get_cost(branch)
                cost.order_list.append(order)

        return self.branch_transport_costs.calc_total_cost()
