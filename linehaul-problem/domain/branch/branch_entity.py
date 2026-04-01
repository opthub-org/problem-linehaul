from domain.branch.branch_data import BranchData
from domain.node.node_data import NodeData


class BranchEntity:

    def __init__(self,
                 data:BranchData,
                 from_node:NodeData,
                 to_node:NodeData):
        self.data:BranchData =data
        self.from_node: NodeData = from_node
        self.to_node: NodeData = to_node

    def __repr__(self):
        return str(self.data)

    @property
    def cost(self)->float:
        return self.data.cost

    @property
    def capa(self)->float:
        return self.data.capacity