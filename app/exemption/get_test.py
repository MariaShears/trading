import datetime

from . import get, Exemption

def get_mock_exemption(broker_id, exemption_amount):
    return Exemption(
        broker_id = broker_id,
        exemption_amount = exemption_amount,
        date = datetime.date.today(),
        comment = "mock exemption comment"
    )