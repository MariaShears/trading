from app.instruments import get, Stock
import datetime


mock_instrument_old = Stock(
    instrument='TEST',
    buy_date=datetime.datetime(2000,5,1),
    sell_date=datetime.datetime(2000,5,1),
    buying_sum=400,
    buying_sum_comission=450,
    exchange_rate=1.5,
    position_size=100,
    comission=50,
    trade_profit=30,
    risk_reward_ratio=5,
    entry_price=4,
    target_price=6,
    bid_price=5,
    atr=0.4,
    initial_stop=4,
    risk_per_stock=1,
    entry_signal="bla",
    exit_signal="blabla",
    comment="comment",
)

mock_instrument_new = Stock(
    instrument='TEST1',
    buy_date=datetime.date.today(),
    sell_date=datetime.date.today(),
    buying_sum=400,
    buying_sum_comission=450,
    exchange_rate=1.5,
    position_size=100,
    comission=50,
    trade_profit=30,
    risk_reward_ratio=5,
    entry_price=4,
    target_price=6,
    bid_price=5,
    atr=0.4,
    initial_stop=4,
    risk_per_stock=1,
    entry_signal="bla",
    exit_signal="blabla",
    comment="comment",
)


def test_filter_by_year():
    mock_instruments = [mock_instrument_old, mock_instrument_new]

    assert len(get.filter_by_year([])) == 0
    assert len(get.filter_by_year(mock_instruments)) == 1
    assert get.filter_by_year([mock_instrument_new])[0].instrument == "TEST1"
    assert len(get.filter_by_year([mock_instrument_old])) == 0