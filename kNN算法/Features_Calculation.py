import pandas as pd
import numpy as np

def RSI_calculator(period_length, data):
    # There must be column 'up_or_down' prepared in 'data'
    df_ups = data[data['up_or_down'] > 0]
    df_downs = data[data['up_or_down'] <= 0]
    sum_ups = df_ups.up_or_down.sum()
    sum_downs = abs(df_downs.up_or_down.sum())
    avg_ups = sum_ups / period_length
    avg_downs = sum_downs / period_length
    RS = avg_ups / avg_downs
    RSI = 100 - (100 / (1 + RS))
    return RSI


def  SCH_calculator(data, S):
    L_price = data['Adj Close'].min()
    H_price = data['Adj Close'].max()
    SCH = 100 * ((S - L_price) / (H_price - L_price))
    return SCH


def WPR_calculator(data, S):
    L_price = data['Adj Close'].min()
    H_price = data['Adj Close'].max()
    WPR = -100 * ((H_price - S) / (H_price - L_price))
    return WPR