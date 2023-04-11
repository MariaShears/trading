def count_price_increase_cases(prices_earnings_df):
    prices_earnings_df.where(prices_earnings_df['surprise'] > 0, inplace=True)
    return prices_earnings_df['price_increase'].astype('bool').value_counts()