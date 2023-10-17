from . import statistics
from .instruments.get_test import get_mock_instrument

def get_mock_instrument_with_profit(profit):
    mock = get_mock_instrument('stock')
    mock.trade_profit = profit
    return mock


def test_calculate_profit():
    test_instruments = [
        get_mock_instrument_with_profit(30),
        get_mock_instrument_with_profit(20),
        get_mock_instrument_with_profit(25),
        get_mock_instrument_with_profit(25)
    ]

    assert statistics.calculate_profit(test_instruments) == 100
