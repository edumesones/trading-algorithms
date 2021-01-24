# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 08:20:51 2021

@author: egzlz
"""

"""
algoritmo trading
"""
import os 
os.chdir(r"C:\phyton\BOLSA")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
fichero=pd.read_csv("AAPL.csv")
fichero=fichero.set_index("Date")
plt.figure(figsize=(12.2,4.5))
plt.plot(fichero["Close"],label="Close")
plt.title("Close price History")
plt.xlabel("Date")
labels=["2020-01-27","2020-03-27","2020-05-27","2020-07-27","2020-09-27","2020-11-27"]
plt.xticks(labels,rotation="vertical")
plt.ylabel("Price in $")
plt.show()
shortEMA=fichero.Close.ewm(span=12,adjust=False).mean()
longEMA=fichero.Close.ewm(span=26,adjust=False).mean()
MACD=longEMA-shortEMA
signal=MACD.ewm(span=9,adjust=False).mean()
plt.figure(figsize=(12.2,4.5))
plt.plot(fichero.index,MACD,label="AAPL MACD",color="red")
plt.plot(fichero.index,signal,label="Signal line",color="blue")
plt.xticks(labels,rotation="vertical")
plt.legend(loc="upper left")
plt.show()
"""
tiempk de vender cuando la MACD line cruza la linea por encima de la de la señal
"""
fichero["MACD"]=MACD
fichero["signal line"]=signal
def buy_sell(signal):
    buy=[]
    sell=[]
    flag=-1
    for i in range(0,len(signal)):
        if signal["MACD"][i]>signal["signal line"][i]:
            sell.append(np.nan)
            if flag!=1:
                buy.append(signal["Close"][i])
                flag=1
            else:
                buy.append(np.nan)
        elif signal["MACD"][i]< signal["signal line"][i]:
            buy.append(np.nan)
            if flag!=0:
                sell.append(signal["Close"][i])
                flag=0
            else:
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    return buy,sell
a=buy_sell(fichero)
fichero["buy signal price"]=a[0]
fichero["sell signal price"]=a[1]
plt.figure(figsize=(12.2,4.5))
plt.scatter(fichero.index,fichero["buy signal price"],color="green",label="buy",marker=6,alpha=1)
plt.scatter(fichero.index,fichero["sell signal price"],color="red",label="sell",marker=7,alpha=1)
plt.plot(fichero["Close"],label="close price",alpha=0.35)
plt.title(" APPLE Close price buy & sell signals")
plt.xlabel("date")
plt.xticks(labels,rotation="vertical")
plt.ylabel("price in $")
plt.legend(loc="upper left")
plt.show()

            
            
        