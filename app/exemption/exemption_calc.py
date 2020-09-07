from app.exemption.get import get_exemptions
from app.db import session
from app.instruments.get import get_instrments


def calculate_total_exemption(exemptions):
    sum_exemptions = 0
    for exemption in exemptions:
        sum_exemptions += exemption.exemption_amount
    return sum_exemptions


def calculate_running_exemption(exemptions):
    instruments = get_instrments(session)
    profits = 0
    for instrument in instruments:
        profits += instrument.trade_profit
        running_exemption = calculate_total_exemption(exemptions) - profits
    return running_exemption
