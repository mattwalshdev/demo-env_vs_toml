import toml
import os
from dotenv import load_dotenv

config = toml.load(".env.toml")
load_dotenv()

# make sure your environment file variables match below
CORRECT_VALUES = {
    "str": "I'm a string",
    "bool": False,
    "int": 123,
    "float": 0.29
}


def value_check(variable, variable_type, correct_values):
    if variable == correct_values[variable_type] and type(variable) == type(
        correct_values[variable_type]
    ):
        print(f"{variable_type} variable matches type and value")
    else:
        print(
            f"{variable_type} variable does not match value or type, {variable} {type(variable)} instead of {correct_values[variable_type]} {type(correct_values[variable_type])}"
        )


# raw .env options
env_string_raw: str = os.environ.get("string_example")
env_bool_raw: bool = os.environ.get("bool_example")
env_int_raw: int = os.environ.get("int_example")
env_float_raw: int = os.environ.get("float_example")

print("---RAW ENV EXAMPLES---")
value_check(env_string_raw, "str", CORRECT_VALUES)
value_check(env_bool_raw, "bool", CORRECT_VALUES)
value_check(env_int_raw, "int", CORRECT_VALUES)
value_check(env_float_raw, "float", CORRECT_VALUES)
print()

# converted .env options
env_string: str = str(os.environ.get("string_example"))
env_bool: bool = bool(os.environ.get("bool_example"))
env_int: int = int(os.environ.get("int_example"))
env_float: float = float(os.environ.get("float_example"))

print("---CONVERTED ENV EXAMPLES---")
value_check(env_string, "str", CORRECT_VALUES)
value_check(env_bool, "bool", CORRECT_VALUES)
value_check(env_int, "int", CORRECT_VALUES)
value_check(env_float, "float", CORRECT_VALUES)
print()

# toml options
toml_string: str = config["demo"]["string_example"]
toml_bool: bool = config["demo"]["bool_example"]
toml_int: int = config["demo"]["int_example"]
toml_float: float = config["demo"]["float_example"]

print("---TOML EXAMPLES---")
value_check(toml_string, "str", CORRECT_VALUES)
value_check(toml_bool, "bool", CORRECT_VALUES)
value_check(toml_int, "int", CORRECT_VALUES)
value_check(toml_float, "float", CORRECT_VALUES)
print()
