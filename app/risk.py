import click
import pandas as pd
import sys

pd.set_option('display.max_columns', 20)

def calculate_trade_parameters():
    master_df = get_trade_frame()
    print(master_df)
    while click.confirm('Do you want to continue?', abort=False):
        new_df = get_trade_frame()
        master_df = master_df.append(new_df, ignore_index=True)
        print(master_df)

def get_trade_frame():
    # ask user what their trading capital is and save it
    capital = float(input("Your current overall trading capital: "))
    # ask user for their trade risk
    trade_risk_raw = int(input("Your trade risk, %: "))
    # calculate user's individual risk capital
    risk_capital = capital * (trade_risk_raw/100)
    # ask user for the product ISIN (optional for manual input version)
    instrument = input("The product ISIN is: ")
    # ask user for ATR of the product (2, 5, days - up to user)
    atr = float(input("Products ATR is: ")) 
    # ask user for ATR multiple
    atr_multiple = float(input("Your ATR multiple is: ")) 
    # ask user for entry price
    entry_price = float(input("Your instrument's entry price is: "))
    # calculate the stop-loss for the trade
    stop_loss = entry_price - (atr * atr_multiple)
    # calculate risk per stock
    risk_per_stock = entry_price - stop_loss
    # calculate position size
    position_size = risk_capital/risk_per_stock
    # calculate buying sum
    buying_sum = position_size * entry_price

    return pd.DataFrame({'Capital': [capital], 
                'Trade risk': [trade_risk_raw], 
                'Risk capital': [risk_capital],
                'Instrument': [instrument],
                'ATR': [atr], 
                'ATR multiple': [atr_multiple], 
                'Entry price': [entry_price], 
                'Stop-loss': [stop_loss], 
                'Risk per stock': [risk_per_stock], 
                'Position size': [position_size], 
                'Buying sum': [buying_sum]
                })