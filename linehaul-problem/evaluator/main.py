"""Example evaluator for the example problem."""
import json
from pathlib import Path
from typing import TypedDict,Any
from app.test_problem.cost_evaluator import CostEvaluator
from infra.path_setting import PathSetting
from test_problem.problem import Problem


class Evaluation(TypedDict):
    """The type of the solution."""

    objective: float

def get_variable(file_path:Path)->str:
    with open(file_path) as f:
        variable = json.load(f)
    return json.dumps(variable)


def evaluate(problem:Problem, path_setting:PathSetting) -> Evaluation:
    """Evaluate the solution variable.

    Args:
        problem (Problem): The problem to evaluate.
        path_setting:PathSetting

    Returns:
    Evaluation: The evaluation result.
    """
    problem.initialize(path_setting)
    objective = problem.evaluate()

    return {"objective": objective}

