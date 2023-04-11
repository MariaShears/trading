import datetime
import re
import readline


def get_existing_option_form_cli(description, options, prefill_text=None):
    selected_option = None
    question = description
    for i, option in enumerate(options):
        question += "\n" + str(i) + " - " + option[0]
    question += "\n"
    while selected_option is None:
        try:
            answer = int(input_with_prefill(question, prefill_text))
            selected_option = options[answer][1]
        except Exception:
            print("Give in a number from the selection")
    return selected_option


def get_number_from_cli(description, prefill_text=None):
    """Gets a number from the command line defaulting to 0"""
    num = None
    while num is None:
        try:
            num = float(input_with_prefill(
                f"{description}: ", prefill_text) or 0)
        except Exception:
            print(f"{description} is should be a number")
    return num


def get_required_number_from_cli(description, prefill_text=None):
    """Gets a required number from the command line"""
    required_num = None
    while required_num is None:
        try:
            required_num = float(input_with_prefill(
                f"{description}: ", prefill_text))
        except Exception:
            print(f"{description} is required and should be a number")
    return required_num


def get_optional_string_from_cli(description, prefill_text=None):
    return input_with_prefill(f"{description}: ", prefill_text) or "n/a"


def is_blank(string):
    if string and string.strip():
        return False
    return True


def get_required_string_from_cli(description, prefill_text=None):
    value = ''
    while is_blank(value):
        value = input_with_prefill(f"{description}: ", prefill_text)
    return value


def _validate_date(txt):
    return re.match(r"^\d{2}\.\d{2}\.\d{4}$", txt) != None


def get_date_from_cli(description, prefill_text=None):
    date = None
    while date is None:
        try:
            date_txt = input_with_prefill(
                f"{description}, ex[01.01.1993]: ", prefill_text)
            if _validate_date(date_txt):
                date = datetime.datetime.strptime(date_txt, '%d.%m.%Y')
            else:
                raise Exception("invalid date")
        except Exception:
            print(f"{description} should be in format of 01.01.1993")
    return date


def input_with_prefill(description, prefill_text):
    if prefill_text is not None:
        def hook():
            readline.insert_text(prefill_text)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        result = input(description)
        readline.set_pre_input_hook()
        return result
    else:
        return input(description)
