from functools import cached_property
import json

from app.test_problem.cost_evaluator import CostEvaluator
from infra.path_setting import PathSetting


from .test_varidator import TestVariableValidator


class Problem:

    VaridatorClass = TestVariableValidator

    def __init__(self,
                 str_variable:str,
                 evaluator:CostEvaluator,
                 n_node:int):
        self.str_variable:str = str_variable
        self.evaluator = evaluator
        self.n_node = n_node
        self.varidator = self.VaridatorClass(self)


    @cached_property
    def variable(self)->list[list]:
        self.variable = json.loads(self.str_variable)
        return self.variable

    def initialize(self,path_setting:PathSetting):
        self.evaluator.initialize(path_setting)
        self.evaluator.set_route_table(self.variable)


    def validate(self):
        return self.varidator.validate()

    def evaluate(self)->float:
        return self.evaluator.eveluate()