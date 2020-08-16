import datetime
import re

def get_number_from_cli(description):
    """Gets a number from the command line defaulting to 0"""
    num = None
    while num is None:
        try:
            num = float(input(f"{description}: ") or 0)
        except Exception:
            print(f"{description} should be a number")
    return num

def get_optional_string_from_cli(description):
    return input(f"{description}: ") or "n/a"

def get_date_from_cli(description):
    date = None
    while date is None:
        try:
            date_txt = input(f"{description}, ex[01.01.1993]: ") or ""
            is_date = re.match(r"^\d{2}\.\d{2}\.\d{4}$", date_txt)
            if is_date:
                date = datetime.datetime.strptime(date_txt, '%d.%m.%Y')
            else:
                raise Exception("invalid date") 
        except Exception:
            print(f"{description} should be in format of 01.01.1993")
    return date