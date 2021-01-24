# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:14:45 2021

@author: egzlz
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
df=pd.read_csv("AAPL.csv")
df=df[["Adj Close"]]
#te indica el numero de dias de la prediccion
forecast_out=30
df["prediction"]=df.shift(-forecast_out)
"""
columna prediccion me da  30 dias antes del precio real de mercado
"""
X=np.array(df.drop(["prediction"],1))
X=X[:-forecast_out]
y=np.array(df["prediction"])

"""
le quita los ultimos 30
"""
y=y[:-forecast_out]
"""
la columna 30 de x es la columna 1 de y
"""
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
svr_fct=SVR(kernel="rbf",C=1e3,gamma=0.1)
svr_fct.fit(x_train,y_train)
svm_confidence=svr_fct.score(x_test,y_test)
lr=LinearRegression()
lr.fit(x_train,y_train)
lr_confidence=lr.score(x_test,y_test)
x_forecast=np.array(df.drop(["prediction"],1))[-forecast_out:]
lr_prediction=lr.predict(x_forecast)
svm_prediction=svr_fct.predict(x_forecast)
print("lr:\n",lr_prediction)
print("svm:\n",svm_prediction)
