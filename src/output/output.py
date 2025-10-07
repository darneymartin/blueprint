
from .json_output import json_output

def output(data, config):
    # Output Based on Configuration Value
    output_type = "json"
    match output_type:
        case "json":
            json_output.output(data)
        case _:  # The wildcard case, similar to 'default'
            print("Invalid Output Type")
