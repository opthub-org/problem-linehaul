
from typing_extensions import override

from app.test_large_problem.new_cost_evaluator import NewCostEvaluator

class RealCostEvaluator(NewCostEvaluator):

    @override
    def set_route_table(self, js: list):

        self.route_table.set_route_list_by_1Dlist(js)