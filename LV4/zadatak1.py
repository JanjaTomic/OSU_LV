from sklearn import datasets
from sklearn.model_selection import train_test_split 
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.metrics
import pandas as pd
import math

from sklearn.preprocessing import StandardScaler 

data = pd.read_csv('data_C02_emission.csv')

var_input = ['Fuel Consumption City (L/100km)',
             'Fuel Consumption Hwy (L/100km)',
             'Fuel Consumption Comb (L/100km)',
             'Fuel Consumption Comb (mpg)',
             'Engine Size (L)',
             'Cylinders']

var_output = ['CO2 Emissions (g/km)']

X=data[var_input].to_numpy()
y=data[var_output].to_numpy()


#a
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

#b Ovisnost kombinirane potrosnje i emisija CO2
plt.scatter(x=X_train[:,3],y=y_train,c='b',label="Train",s=1)
plt.scatter(x=X_test[:,3],y=y_test,c='r',label="Test",s=1)
plt.legend()
plt.show()

#c) Standardizacija podataka za učenje
ss=StandardScaler()
X_train_n=ss.fit_transform(X_train)

# Histogram usporedbe prije i poslije standardizacije
plt.hist(x=X_train[:,3])
plt.title("Prije standardizacije:")
plt.show()

plt.hist(x=X_train_n[:,3])
plt.title("Poslije standardizacije:")
plt.show()

# Transformacija podataka za testiranje
X_test_n=ss.transform(X_test)

#d) Izgradnja linearnog modela
linearModel=lm.LinearRegression()
linearModel.fit(X_train_n,y_train)

# Ispisivanje parametara 
print("Koeficijenti:")
print(linearModel.intercept_)
print(linearModel.coef_)

#e) Procjena izlazne veličine
y_test_p=linearModel.predict(X_test_n)

# Odnos stvarnih vrijednosti i procjene
plt.scatter(x=y_test,y=y_test_p)
plt.title("Odnos stvarnih vrijednosti i procjene")
plt.show()

#f) Računanje regresijskih metrika na skupu podataka za testiranje
MAE=sklearn.metrics.mean_absolute_error(y_test,y_test_p)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
RMSE=math.sqrt(MSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
R2=sklearn.metrics.r2_score(y_test,y_test_p)

print('MAE:',MAE)
print('MSE:',MSE)
print('RMSE:',RMSE)
print('MAPE:',MAPE)
print('R2:',R2)

#g) Promjena raspodjele train i test podataka
# Povećavanjem testnog skupa vrijednosti regresijskih metrika su se smanjile

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.4,random_state=1)

ss = StandardScaler()
X_train_n=ss.fit_transform(X_train)
X_test_n=ss.transform(X_test)

linModel = lm.LinearRegression()
linModel.fit(X_train_n,y_train)
print(linModel.coef_)

y_test_p=linModel.predict(X_test_n)

MAE=sklearn.metrics.mean_absolute_error(y_test,y_test_p)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
RMSE=math.sqrt(MSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
R2=sklearn.metrics.r2_score(y_test,y_test_p)

print('MAE:',MAE)
print('MSE:',MSE)
print('RMSE:',RMSE)
print('MAPE:',MAPE)
print('R2:',R2)