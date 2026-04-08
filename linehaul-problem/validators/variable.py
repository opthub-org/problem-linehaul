"""Example validator for the variable."""

import json

from jsonschema import validate

from app.test_problem.problem import Problem


def get_table_routing_schema(n_node: int):
    return f"""{{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Routing Table Schema.",
    "type": "array",
    "items": {{
      "type": "object",
      "properties": {{
        "from": {{
          "type": "integer",
          "description": "出発地点のprefecture code"
        }},
        "next": {{
          "type": "array",
          "items": {{
            "type": "integer"
          }},
          "minItems": {n_node},
          "maxItems": {n_node},
          "description": "遷移先のノードリスト,自己ループは-1（要素数は{n_node}固定）"
        }}
      }},
      "required": ["from", "next"],
      "additionalProperties": false
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
