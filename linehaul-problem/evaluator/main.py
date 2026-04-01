"""Example evaluator for the example problem."""
import json
from pathlib import Path
from typing import TypedDict,Any
from app.cost_evaluator import CostEvaluator
from infra.path_setting import PathSetting


class Evaluation(TypedDict):
    """The type of the solution."""

    objective: float

def get_variable(file_path:Path)->str:
    with open(file_path) as f:
        variable = json.load(f)
    return json.dumps(variable)


def evaluate(variable:list[dict[str,Any]], path_setting:PathSetting) -> Evaluation:
    """Evaluate the solution variable.

    Args:
        variable (float): Solution variable.
        path_setting:PathSetting

    Returns:
    Evaluation: The evaluation result.
    """

    evaluater = CostEvaluator()
    evaluater.initialize(path_setting)
    evaluater.set_route_table(variable)
    objective = evaluater.eveluate()

    return {"objective": objective}

