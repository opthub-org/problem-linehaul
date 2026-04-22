from __future__ import annotations
from typing import TYPE_CHECKING

import json

from jsonschema import validate

if TYPE_CHECKING:
    from app.test_problem.problem import Problem


class TestVariableValidator:

    def __init__(self,problem:Problem):
        self.problem = problem

    @property
    def n_node(self):
        return self.problem.n_node


    def get_table_routing_schema(self):
        return f"""{{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Routing Table Schema.",
        "description": "A 46x46 2D array of integers.",
        "type": "array",
        "minItems": {self.n_node},
        "maxItems": {self.n_node},
        "items": {{
            "type": "array",
            "minItems": {self.n_node},
            "maxItems": {self.n_node},
            "items": {{
                "type": "integer"
            }}
        }}
        }}"""

    def validate(self) -> list[dict]:
        """Validate the variable.

        Args:
            variable (str): The variable.
            n_node (int): The number of node
        Returns:
        float | list[float]: The validated variable.
        """
        # Validate the variable here.
        # This is an example that validates whether the variable is a scalar or a vector.
        ROUTING_TABLE_SCHEMA = self.get_table_routing_schema()

        json_variable = self.problem.variable  # Convert the variable to JSON
        validate(json_variable, json.loads(ROUTING_TABLE_SCHEMA))  # Validate the variable

        return json_variable
