from app.test_problem.problem import Problem
from infra.path_setting import PathSetting
from real_problem.real_varidator import RealVariableValidator


class RealProblem(Problem):

    VaridatorClass = RealVariableValidator

    def initialize(self, path_setting: PathSetting):
        self.evaluator.initialize(path_setting)
        n_prefecture =46
        variable_2d_array =[self.variable[i:i+n_prefecture]
                            for i in range(0,len(self.variable),n_prefecture)]
        self.evaluator.set_route_table(variable_2d_array)
