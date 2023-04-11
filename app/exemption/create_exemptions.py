import datetime
from . import Exemption
from app.cli_utils import get_required_number_from_cli, get_optional_string_from_cli, get_existing_option_form_cli
from app.brokers.get import presentable_broker


def create_exemption_from_cli(brokers):
    exemption_amount = get_required_number_from_cli('Exemption amount')
    broker = get_existing_option_form_cli(
        'Broker', list(map(presentable_broker, brokers)))
    comment = get_optional_string_from_cli('Comment')

    # calculated fields
    date = datetime.datetime.today()

    new_exemption = Exemption(
        exemption_amount=exemption_amount,
        broker=broker,
        date=date,
        comment=comment,
    )
    return new_exemption
