import math
from statistics import NormalDist

from domain.branch.branch_vo import BranchVO
from domain.order.order_vo import OrderVO


class BranchTransportCost:
    EPSILON = 10 ** -3

    def __init__(self, branch: BranchVO, vehicle_capacity: float):
        self.branch: BranchVO = branch
        self.vehicle_capacity: float = vehicle_capacity
        self.order_list: list[OrderVO] = []

    @property
    def total_load_average(self) -> float:
        return sum(o.weight for o in self.order_list)

    @property
    def total_standard_deviation(self) -> float:
        return math.sqrt(sum(o.sd **2 for o in self.order_list))

    @property
    def average_required_vehicle(self) -> float:
        return self.total_load_average / self.vehicle_capacity

    def get_cost(self):
        if not self.order_list:
            return 0
        cdf_list = self._make_cdf_list()

        total_cost = 0
        for n_vehicle in range(len(cdf_list)):
            upper = cdf_list[n_vehicle]
            lower = cdf_list[n_vehicle - 1] if n_vehicle > 1 else 0
            prob = upper - lower
            total_cost += prob * n_vehicle * self.branch.cost

        return total_cost

    def _make_cdf_list(self):

        norm_dist = NormalDist(mu=self.total_load_average,
                               sigma=self.total_standard_deviation)

        cdf_list = [0.0]
        stop_prob = 1 - self.EPSILON
        n_vehicle = 1
        while cdf_list[-1] < stop_prob:
            prob = norm_dist.cdf(n_vehicle * self.vehicle_capacity)
            cdf_list.append(prob)
            n_vehicle += 1

        return cdf_list
