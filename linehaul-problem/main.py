"""Example problem."""

import json
import logging
from pathlib import Path
import sys

import click

from evaluator.main import evaluate
from infra.path_setting import PathSetting
from validators.example_env import validate_example_env
from validators.variable import validate_variable

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)  # Logger


@click.command(help="Example problem.")
@click.option(
    "-c",
    "--case_name",
    type=str,
    help="case_name",
)
@click.option(
"-t",
    "--case_type",
    type=str,
    help="case_type",
)
def main(case_name: str,case_type) -> None:
    """Example main function for evaluating given variable."""
    root = Path(__file__).parent.parent
    env_var = {"case_name":case_name,
               "case_type":case_type}

    try:
        validated_example_env = validate_example_env(env_var)  # Validate the environment variable
        msg = f"validated_example_env: {validated_example_env}"
        LOGGER.info(msg)

        path_setting = PathSetting(str(root), validated_example_env["case_name"].strip())
        variable = get_variable(validated_example_env["case_type"].strip(), path_setting.routing_table)

        validated_variable = validate_variable(variable)  # Validate the variable
        # msg = f"validated_variable: {validated_variable}"
        # LOGGER.info(msg)

        result = evaluate(validated_variable,path_setting)  # Evaluate the variable
        msg = f"result: {result}"
        LOGGER.info(msg)

        sys.stdout.write(json.dumps(result))  # Write the result to the standard output

    except Exception as e:
        error_result = {"objective": None, "error": str(e)}
        sys.stdout.write(
            json.dumps(error_result),
        )  # Write the error result to the standard output
        msg = f"error result: {error_result}"
        LOGGER.info(msg)
        raise

def get_variable(case_type:str,file_path:Path)->str:
    match case_type:
        case "test":
            if not file_path.exists():
                raise FileNotFoundError(f"{file_path}is not exist")
            variable = file_path.read_text()
        case "problem":
            variable = input()
        case _:
            raise ValueError(f"case_type:{case_type} is undifined")
    return variable



if __name__ == "__main__":
    main()
