from . import cli_utils

def test_validate_date():
    assert cli_utils._validate_date('01.01.1993') == True
    assert cli_utils._validate_date('asdfksadf') == False