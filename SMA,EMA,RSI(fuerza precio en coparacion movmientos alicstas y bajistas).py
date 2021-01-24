# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:25:08 2021

@author: egzlz
"""

"""
RSI,EMA,SMA,MACD
RSI:
when gets near 30 it wpuld a buy
when gets near 70 it´s a sell
then I put some threshold

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("TYME.csv")
#SMA:medias moviles
df=df.set_index("Date")
def SMA(df,period=30,column="Close"):
    return df[column].rolling(window=period).mean()
#EMA medias exponenciales
def EMA(data,period=30,column=["Close"]):
    """
    1- alpha)**n-1,(1-alpha)**n-2(dar funcion exponencial de pesos)
    """
    return df[column].ewm(span=period,adjust=False).mean()
def MACD(df,long_period=26,short_period=12,period_signal=9,column="Close"):
    #short term exponential movement
    short_EMA=EMA(df,short_period,column=column)
    long_EMA=EMA(df,long_period,column=column)
    #moving average divergence/cionvergence
    df["MACD"]=short_EMA-long_EMA
    df["signal_line"]=EMA(df,period_signal,column="MACD")
    return df
#create a function to compute the relative strenght index(RSI):INDICA LA FUERZA DEL PRECIO MEDIANTE
# COMPARACION DE MOVIMIENTOS A LA ALZA Y LA ABAJA

def RSI(df,period=14,column="Close"):
    delta=df[column].diff(1)
    """
    diferencia entre 1 y el siguiente
    """
    delta=delta[1:]
    up=delta.copy()
    down=delta.copy()
    up[up<0]=0
    down[down>0]=0
    df["up"]=up
    df["down"]=down
    AVG_gain=SMA(df,period,column="up")
    AVG_loss=abs(SMA(df,period,column="down"))
    relative_strenght=AVG_gain/AVG_loss
    RSI=100.0-(100.0/(1.0+relative_strenght))
    df["RSI"]=RSI
    return df
MACD(df)
RSI(df)
df["SMA"]=SMA(df)
df["EMA"]=EMA(df)



column_list=["SMA","Close"]
plt.figure(figsize=(12.2,4.5))
df[column_list].plot(figsize=(12.2,4.5))
plt.title("SMA for APPLE")
plt.xlabel("Date")
plt.ylabel("Price in $")

plt.show()

column_list=["EMA","Close"]
plt.figure(figsize=(12.2,4.5))
df[column_list].plot(figsize=(12.2,4.5))
plt.title("EMA for AAPLE")
plt.xlabel("Date")
plt.ylabel("Price in $")

plt.show()


column_list=["MACD","signal_line"]
plt.figure(figsize=(12.2,4.5))
df[column_list].plot(figsize=(12.2,4.5))
plt.title("MACD for APPLE")
plt.xlabel("Date")
plt.ylabel("Price in $")
plt.show()

column_list=["RSI"]
plt.figure(figsize=(12.2,4.5))
df[column_list].plot(figsize=(12.2,4.5))
plt.axhline(15,linestyle="--",color="orange")
plt.axhline(30,linestyle="--",color="blue")
plt.axhline(70,linestyle="--",color="blue")
plt.axhline(85,linestyle="--",color="orange")
plt.title("RSI  AAPLE")
plt.xlabel("Date")
plt.ylabel("Price in $")
plt.show()

plt.figure(figsize=(12.2,4.5))
plt.plot(df["Close"],label="close price",alpha=0.5)
plt.title(" AAPLE stock price")
plt.xlabel("Date")
plt.ylabel("Price in $")
plt.show()


    