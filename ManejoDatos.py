import pandas as pd
#import os

#carga de datos CSV
#print(os.getcwd())
data = pd.read_csv('pythonPandas/ejemplo_datos.csv')

#df = pd.DataFrame(data)
#print(df)

print(data.head())
print(data.shape)
print(data.info())
print(data.describe())

data.to_csv('pythonPandas/new_data.csv')


    