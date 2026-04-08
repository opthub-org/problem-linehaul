from pathlib import Path

from test_large_problem.new_cost_evaluator import NewCostEvaluator
from test_problem.cost_evaluator import CostEvaluator
from .test_problem.problem import Problem


class ProblemFactory:

    @staticmethod
    def create(case_type:str,file_path:Path) ->Problem:
        if case_type=="test":
            if not file_path.exists():
                raise FileNotFoundError(f"{file_path}is not exist")

        match case_type:
            case "test":
                variable = file_path.read_text()
                problem = Problem(str_variable= variable,
                                  evaluator= CostEvaluator(v_capa=10),
                                  n_node=5)
            case "test-large":
                variable = file_path.read_text()
                problem = Problem(str_variable=variable,
                                  evaluator=NewCostEvaluator(v_capa=100000),
                                  n_node=46)
            case "problem":
                variable = input()
                problem = Problem(str_variable=variable,
                                  evaluator=NewCostEvaluator(v_capa=100000),
                                  n_node=46)
            case _:
                raise ValueError(f"case_type:{case_type} is undifined")
        return problem
