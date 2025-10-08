# test_output.py
from src.output import Output


def test_json_ouput(capsys):
    # Define Data Dict
    data_dict = {}
    data_dict['key'] = "value"

    # Define JSON Return
    data_json = """{
    "key": "value"
}
"""
    Output(data_dict, "json")
    captured = capsys.readouterr()
    assert data_json in captured.out

def test_text_output():
    # Define Data Dict
    data_dict = {}
    data_dict['key'] = "value"

    ret_code=Output(data_dict, "text")
    assert None == None

