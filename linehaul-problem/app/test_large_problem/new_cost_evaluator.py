
from typing_extensions import override

from app.test_problem.cost_evaluator import CostEvaluator
from domain.route.route_table import RouteTable
from infra.io.network import NewNetworkReader
from infra.path_setting import PathSetting
from infra.io.order.new_order_reader import NewOrderReader

class NewCostEvaluator(CostEvaluator):

    @override
    def initialize(self, path_setting: PathSetting):
        network_reader = NewNetworkReader(path_setting.prefectures,
                                          path_setting.truck_distance_time_long,
                                          path_setting.virtual_prefecture_flows)
        self.network.read(network_reader)

        order_reader = NewOrderReader(path_setting.virtual_prefecture_flows)
        self.order_collection.read(order_reader)
        self.order_collection.convert_vo(self.nodes)

        self.route_table = RouteTable(self.network)
