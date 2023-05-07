import pandas as pd
import numpy as np

data = pd.read_csv('data_C02_emission.csv')
pd.set_option('display.max_columns', None)

#a
print("Broj mjerenja u DataFrame:",len(data))

print("Tipovi podataka za veličine:",data.dtypes)

print(data.isnull().sum())
print("Nema izostalih vrijednosti")

data.drop_duplicates(inplace=True)
print("Broj mjerenja nakon uklanjanja duplikata:", len(data))

#konvertiranje kategorickih velicina u tip category
data[data.select_dtypes(include=['object']).columns] = data.select_dtypes(include=['object']).astype('category')


#b
fuel_consumption_data =data[['Make','Model','Fuel Consumption City (L/100km)',]]

print('Tri auta s najmanjom gradskom potrošnjom:',fuel_consumption_data.nsmallest(3,'Fuel Consumption City (L/100km)'))
print('Tri auta s najvećom gradskom potrošnjom:',fuel_consumption_data.nlargest(3,'Fuel Consumption City (L/100km)'))

#c
data_motor_size =data[(data['Engine Size (L)']>=2.5) & (data['Engine Size (L)']<=3.5)]

print('Broj vozila sa motorima veličine između 2.5 i 3.5 L:',len(data_motor_size ))
print('Prosječna CO2 emisija ovih vozila:',np.mean(data_motor_size ['CO2 Emissions (g/km)']))

#d
data_audi=data[(data['Make']=='Audi')]

print('Broj Audi vozila:',len(data_audi))

data_audi_cylinders=data_audi[(data_audi['Cylinders']==4)]

print('CO2 emisije Audi auta sa 4 cilindra:',np.mean(data_audi_cylinders['CO2 Emissions (g/km)']))

#e
print('Broj vozila s parnim brojem cilindara:',len(data[(data['Cylinders']%2==0)]))

print('CO2 potrošnja s obzirom na broj cilindara:',data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean())

#f
data_diesel=data[(data['Fuel Type']=='D')]
data_gas=data[(data['Fuel Type']=='X')]

print('Prosječna potrošnja dizelaša u gradu:',np.mean(data_diesel['Fuel Consumption City (L/100km)']))
print('Prosječna potrošnja benzinaca u gradu:',np.mean(data_gas['Fuel Consumption City (L/100km)']))

print('Median dizelaša',np.median(data_diesel['Fuel Consumption City (L/100km)']))
print('Median benzinaca',np.median(data_gas['Fuel Consumption City (L/100km)']))

#g)
data_diesel_4=data[(data['Fuel Type']=='D') & (data['Cylinders']==4)]

print('Dizel vozilo sa 4 cilindra s najvećom gradskom potrošnjom:')
print(data_diesel_4.nlargest(1,'Fuel Consumption City (L/100km)')[['Make','Model','Fuel Consumption City (L/100km)']])

#h)
data_manual=data[(data['Transmission'].str.startswith('M'))]
print('Broj auta sa mjenjačem:',len(data_manual))

#i)
print(data.corr(numeric_only=True))