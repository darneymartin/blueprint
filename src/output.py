import json

class Output():

    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.output()
    

    def output(self):
        output_type = self.config
        match output_type:
            case "text":
                Output.text_output(self.data)
            case "json":
                Output.json_output(self.data)
            case _:
                print("Invalid Output Type")

    @staticmethod
    def json_output(data: dict) -> None:
        print(json.dumps(data, indent=4))
        return None
    
    @staticmethod
    def text_output(data: dict) -> None:
        for model in data:
            headers = sorted(list(set(key for item in data[model] for key in item.keys())))

   
            col_widths = {key: len(key) for key in headers}
            for item in data[model]:
                for key in headers:
                    value = str(item.get(key, ""))
                    if len(value) > col_widths[key]:
                        col_widths[key] = len(value)

            header_line = " | ".join(f"{h:<{col_widths[h]}}" for h in headers)
            separator_line = "-+-".join("-" * col_widths[h] for h in headers)

            fmr_str = str(" " * (int(len(separator_line)/2) - int(len(model)/2)) )
            print(fmr_str + model)

            print(header_line)
            print(separator_line)

            for item in data[model]:
                row_values = [str(item.get(key, "")) for key in headers]
                row_line = " | ".join(f"{val:<{col_widths[key]}}" for key, val in zip(headers, row_values))
                print(row_line)
            print("")


        return None
            
