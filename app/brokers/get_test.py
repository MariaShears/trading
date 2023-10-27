import datetime

from . import get, Broker

def get_mock_broker(id, exemptions, stocks):
    return Broker(
    id = id,
    name = f"test_broker_{id}",
    date = datetime.date.today(),
    exemptions = exemptions,
    stocks = stocks
    )