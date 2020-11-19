from app.cli_utils import *
from app.instruments.get import presentable_stock


def edit_stock_from_cli(stocks):
    entry_to_edit = get_existing_option_form_cli('Entry you want to edit is', list(map(presentable_stock, stocks)))
    return entry_to_edit