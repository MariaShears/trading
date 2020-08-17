from app.instruments import create

def test_calculate_initial_stop():
    assert create._caculate_initial_stop(entry_price = 46.0, atr = 1.4) == 43.2
    assert create._caculate_initial_stop(entry_price = 1, atr = 2) == -3

def test_caculate_risk_per_stock():
    assert create._caculate_risk_per_stock(entry_price = 30, initial_stop = 26) == 4
    assert create._caculate_risk_per_stock(entry_price = 6.0, initial_stop = 2) == 4

def test__aculate_risk_reward_ratio():
    assert create._caculate_risk_reward_ratio(risk_per_stock = 4, target_price = 65, entry_price = 60) == 0.8
    assert create._caculate_risk_reward_ratio(risk_per_stock = 4, target_price = 65, entry_price = 65) == 0

def test_caculate_buying_sum():
    assert create._caculate_buying_sum(position_size = 100, entry_price = 60) == 6000
    assert create._caculate_buying_sum(position_size = 3.0, entry_price = 9.0) == 27.0

def test_caculate_buying_sum_comission():
    assert create._caculate_buying_sum_comission(position_size = 100, entry_price = 60, comission = 15.0) == 6015
    assert create._caculate_buying_sum_comission(position_size = 20, entry_price = 0.4, comission = 5) == 13
    
def test_caculate_trade_profit():
    assert create._caculate_trade_profit(exchange_rate = 1.5, position_size = 100, bid_price = 55.0, entry_price = 30.0, comission = 15) == 1651.6667
    assert create._caculate_trade_profit(exchange_rate = 1.4, position_size = 20.0, bid_price = 23, entry_price = 22.0, comission = 10) == 4.2857
    assert create._caculate_trade_profit(exchange_rate = 0, position_size = 13, bid_price = 60.0, entry_price = 50.0, comission = 10) == 120
