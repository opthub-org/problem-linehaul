from abc import ABC,abstractmethod

from domain.branch.branch_data import BranchData
from domain.node.node_data import NodeData


class INetworkReader(ABC):

    def __init__(self):
        self.node:list[NodeData]=[]
        self.branch:list[BranchData] = []

    @abstractmethod
    def read(self):
        raise NotImplementedError()