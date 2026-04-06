from statistics import NormalDist

from domain.branch.branch_vo import BranchVO
from domain.order.order_vo import OrderVO


class BranchTransportCost:
    vehicle_capacity = 10

    def __init__(self, branch: BranchVO):
        self.branch: BranchVO = branch
        self.order_list: list[OrderVO] = []

    @property
    def total_load_average(self) -> float:
        return sum(o.weight for o in self.order_list)

    @property
    def total_standard_deviation(self) -> float:
        return sum(o.sd for o in self.order_list)

    @property
    def average_required_vehicle(self) -> float:
        return self.total_load_average / self.vehicle_capacity

    def get_cost(self):
        norm_dist = NormalDist(mu=self.total_load_average,
                               sigma=self.total_standard_deviation)
        vehicle_max = int(2 * self.average_required_vehicle)
        cdf_list = [norm_dist.cdf(i * self.vehicle_capacity) for i in range(vehicle_max)]

        total_cost = 0
        for n_vehicle in range(1, vehicle_max):
            upper = cdf_list[n_vehicle]
            lower = cdf_list[n_vehicle - 1]
            prob = upper - lower
            total_cost += prob * n_vehicle * self.branch.cost

        return total_cost
