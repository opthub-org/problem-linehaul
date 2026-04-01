import itertools
from domain.node.node_data import NodeData


class RouteEntity:

    def __init__(self, node_list: list[NodeData]):
        self.node_list: list[NodeData] = node_list
        self._check_valid()

    def __repr__(self):
        return "→".join(n.name for n in self.node_list)

    @property
    def n_node(self):
        return len(self.node_list)

    @property
    def from_(self) -> NodeData:
        return self.node_list[0]

    @property
    def to_(self) -> NodeData:
        return self.node_list[-1]

    @property
    def pairwise(self):
        return itertools.pairwise(self.node_list)

    def _check_valid(self):
        if self.n_node < 2:
            raise ValueError(f"RouteEntityの作成には少なくとも2つ以上のNodeDataが必要です。")
        if self.from_ == self.to_:
            raise ValueError(f"from_とto_が同じです。({self.from_}")