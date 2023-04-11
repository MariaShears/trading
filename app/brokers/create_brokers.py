import datetime
from . import Broker
from app.cli_utils import get_number_from_cli, get_optional_string_from_cli, get_date_from_cli, get_required_string_from_cli, get_required_number_from_cli
from app.brokers.get import get_brokers
from app.db import session


def _check_if_broker_exists(name):
    brokers = get_brokers(session)
    existing_brokers = []
    for broker in brokers: 
        if broker.name.casefold().__eq__(name.casefold()):
            existing_brokers.append(broker.name)
    return existing_brokers

def create_broker_from_cli():
    name = get_required_string_from_cli('Broker you use')
    while name.casefold() in _check_if_broker_exists(name):
        print('This broker already exists')
        name = get_required_string_from_cli('Broker you use')
    else:
        comment = get_optional_string_from_cli('Comment')

    # calculated fields
    date = datetime.datetime.today()

    new_broker = Broker(
        name=name,
        date=date,
        comment=comment,
    )
    return new_broker
