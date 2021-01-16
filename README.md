# money-flow-index-
algorithm for trading 
"""
algorithm called money flow index for trading
IMPORTANT I GET THE DATA FROM YAHOO FINANCE ,the only thing you have to is choose the ticker you want to analyse and download the data in the part "historical data"
EXAMPLE:
GO TO https://finance.yahoo.com/quote/AAPL/history?p=AAPL
and download the historical data in the same directory as you are coding and that´s shit!!
for english people fichero means file
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fichero=pd.read_csv("NNDM.csv")
fichero=fichero.set_index("Date")
plt.figure(figsize=(12.2,4.5))
plt.plot(fichero["Close"],label="Close")
plt.title("Close price History")
plt.xlabel("Date")
labels=["2020-01-27","2020-03-27","2020-05-27","2020-07-27","2020-09-27","2020-11-27"]
plt.xticks(labels,rotation="vertical")
plt.ylabel("Price in $")
plt.legend(fichero.columns.values,loc="upper left")
plt.show()
typical_price=(fichero["High"]+fichero["Low"]+fichero["Close"])/3
period=14
money_flow=typical_price*fichero["Volume"]
positive_flow=[]
negative_flow=[]
for i in range(1,len(typical_price)):
    if typical_price[i]>typical_price[i-1]:
        positive_flow.append(money_flow[i-1])
        negative_flow.append(0)
    elif typical_price[i]<typical_price[i-1]:
        positive_flow.append(0)
        negative_flow.append(money_flow[i-1])
    else:
        negative_flow.append(0)
        positive_flow.append(0)
        
positive_mf=[]
negative_mf=[]

for i in range(period-1,len(positive_flow)):
               positive_mf.append(sum(positive_flow[i+1-period:i+1]))
for i in range(period-1,len(negative_flow)):
               negative_mf.append(sum(negative_flow[i+1-period:i+1]))
mfi=100*(np.array(positive_mf)/(np.array(positive_mf)+np.array(negative_mf)))
df2=pd.DataFrame()
df2["MFI"]=mfi
plt.figure(figsize=(12.2,4.5))
plt.plot(df2["MFI"],label="MFI")
plt.axhline(10,linestyle="--",color="orange")
plt.axhline(20,linestyle="--",color="blue")
plt.axhline(80,linestyle="--",color="blue")
plt.axhline(90,linestyle="--",color="orange")
plt.title("MFI")
plt.ylabel("MFI value")

plt.show()
new_df=pd.DataFrame()
new_df=fichero[period:]
new_df["MFI"]=mfi
def get_signal(data,high,low):
    buy_signal=[]
    sell_signal=[]
    for i in range(len(data["MFI"])):
        if data["MFI"][i]>high:
            buy_signal.append(np.nan)
            sell_signal.append(data["Close"][i])
        elif data["MFI"][i]<low:
            buy_signal.append(data["Close"][i])
            sell_signal.append(np.nan)
        else:
             sell_signal.append(np.nan)
             buy_signal.append(np.nan)
        
    return buy_signal,sell_signal
new_df["buy"]=get_signal(new_df,80,20)[0]
new_df["sell"]=get_signal(new_df,80,20)[1]
plt.figure(figsize=(12.2,4.5))
plt.plot(new_df["Close"],label="close price",alpha=0.5)
plt.scatter(new_df.index,new_df["buy"],color="green",label="BUY SIGNAL",marker="^",alpha=1)
plt.scatter(new_df.index,new_df["sell"],color="red",label="SELL SIGNAL",marker="v",alpha=1)
plt.title(" APPLE Close price buy & sell signals")
plt.xlabel("date")
plt.xticks(labels,rotation="vertical")
plt.ylabel("price in $")
plt.legend(loc="upper left")
plt.show()

plt.figure(figsize=(12.2,4.5))
plt.plot(new_df["MFI"],label="MFI")
plt.axhline(10,linestyle="--",color="orange")
plt.axhline(20,linestyle="--",color="blue")
plt.axhline(80,linestyle="--",color="blue")
plt.axhline(90,linestyle="--",color="orange")
plt.title("MFI")
plt.ylabel("MFI value") 
