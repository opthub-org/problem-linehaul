import json
from app.test_problem.problem import TestVariableValidator


class RealVariableValidator(TestVariableValidator):

    def get_table_routing_schema(self):
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Routing Table Schema.",
            "description": f"A 2116(=46x46) 1D array of integers.",
            "type": "array",
            "minItems": self.n_node,
            "maxItems": self.n_node,
            "items": {
                "type": "integer"
            }
        }
        return json.dumps(schema, indent=4)