import datetime

# these imports are needed so sqlalchemy can find the def of Broker and Exemption
import app.brokers
import app.exemption
from . import get, Stock

def get_mock_instrument(name, trade_profit, broker_id):
    return Stock(
        instrument=name,
        buy_date=datetime.date.today(),
        sell_date=datetime.date.today(),
        buying_sum=1,
        buying_sum_comission=1,
        exchange_rate=1,
        position_size=1,
        comission=1,
        trade_profit=trade_profit,
        risk_reward_ratio=1,
        entry_price=1,
        target_price=1,
        bid_price=1,
        atr=1,
        initial_stop=1,
        risk_per_stock=1,
        entry_signal="signal",
        exit_signal="signal",
        comment="comment",
        broker_id = broker_id
    )

def test_filter_by_year():
    mock_instrument_old = get_mock_instrument('old', trade_profit=1, broker_id=1)
    mock_instrument_old.sell_date = datetime.datetime(2000, 5, 1)

    mock_instrument_new = get_mock_instrument('new', trade_profit=1, broker_id=1)
    mock_instruments = [mock_instrument_old, mock_instrument_new]

    assert len(get.filter_by_year([])) == 0
    assert len(get.filter_by_year(mock_instruments)) == 1
    assert get.filter_by_year([mock_instrument_new])[0].instrument == "new"
    assert len(get.filter_by_year([mock_instrument_old])) == 0

def test_filter_by_month():
    mock_instrument_old = get_mock_instrument('old', trade_profit=1, broker_id=1)
    mock_instrument_old.sell_date = datetime.datetime(2000, 5, 1)
    mock_instrument_bit_old = get_mock_instrument('-40', trade_profit=1, broker_id=1)
    mock_instrument_bit_old.sell_date = datetime.datetime.today() - datetime.timedelta(days=40)
    mock_instrument_new = get_mock_instrument('new', trade_profit=1, broker_id=1)
    mock_instruments = [mock_instrument_old, mock_instrument_bit_old, mock_instrument_new]

    assert len(get.filter_by_month([])) == 0
    assert len(get.filter_by_month(mock_instruments)) == 1
    assert get.filter_by_month([mock_instrument_new])[0].instrument == "new"
    assert len(get.filter_by_month([mock_instrument_old])) == 0