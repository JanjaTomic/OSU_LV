import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('data_C02_emission.csv')


#a
data['CO2 Emissions (g/km)'].plot(kind='hist')
plt.xlabel('CO2 Emissions (g/km)')
plt.title('CO2 Emissions histogram')
plt.show()

#b
colors=['b','y','r','g','purple']
gas=['X','Z','D','E','N']

for i in range(0,5):
    data_subset=data[data['Fuel Type']==gas[i]]
    x=np.array(data_subset['Fuel Consumption City (L/100km)'])
    y=np.array(data_subset['CO2 Emissions (g/km)'])
    plt.scatter(x,y, c=colors[i], s=2 )
plt.show()

#c
data.boxplot(column = ['Fuel Consumption Hwy (L/100km)'], by = 'Fuel Type')
plt.title('Razdioba izvangradske potrošnje goriva s obzirom na tip goriva')
plt.show()

#d
data.groupby('Fuel Type').size().plot(kind = 'bar')
plt.title('Broj vozila po tipu goriva')
plt.show()

#e)
data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().plot(kind = 'bar')
plt.title('Prosječna emisija CO2 s obzirom na broj cilindara')
plt.show()