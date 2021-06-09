# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:15:33 2021

@author: Adarsh_Singh
"""

import pandas as pd


url = "https://query1.finance.yahoo.com/v7/finance/download/%5ENSEI?period1=1307232000&period2=1622851200&interval=1d&events=history&includeAdjustedClose=true" #in this url you can replace with your url from yahoo finance site
stock_price = pd.read_csv(url)
print(stock_price)

df = pd.DataFrame(stock_price)
df.sort_values(by=["Date"], ascending=True)
df.to_csv("NEFT.csv", index=False)