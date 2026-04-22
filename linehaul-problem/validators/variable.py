"""Example validator for the variable."""

import json

from jsonschema import validate

from app.test_problem.problem import Problem


def get_table_routing_schema(n_node: int):
    return f"""{{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Routing Table Schema.",
    "description": "A 46x46 2D array of integers.",
    "type": "array",
    "minItems": 46,
    "maxItems": 46,
    "items": {{
        "type": "array",
        "minItems": 46,
        "maxItems": 46,
        "items": {{
            "type": "integer"
        }}
    }}
    }}"""


def validate_variable(problem: Problem) -> list[dict]:
    """Validate the variable.

    Args:
        variable (str): The variable.
        n_node (int): The number of node
    Returns:
    float | list[float]: The validated variable.
    """
    # Validate the variable here.
    # This is an example that validates whether the variable is a scalar or a vector.
    ROUTING_TABLE_SCHEMA = get_table_routing_schema(problem.n_node)

    json_variable = problem.variable  # Convert the variable to JSON
    validate(json_variable, json.loads(ROUTING_TABLE_SCHEMA))  # Validate the variable

    return json_variable
