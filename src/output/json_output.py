import json

class json_output():

    def output(data: dict):
        print(json.dumps(data, indent=4))