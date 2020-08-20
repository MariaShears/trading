import datetime
from . import Broker
from app.cli_utils import get_number_from_cli, get_optional_string_from_cli, get_date_from_cli, get_required_string_from_cli, get_required_number_from_cli


def create_broker_from_cli():
    broker = get_required_string_from_cli('Broker you use')
    tax_exemption = get_required_number_from_cli('Tax exemption for this broker')
    comment = get_optional_string_from_cli('Comment')

    #calculated fields
    date = datetime.datetime.today()

    new_broker = Broker(
        broker = broker,
        tax_exemption = tax_exemption,
        date = date,
        comment = comment,
    )
    return new_broker