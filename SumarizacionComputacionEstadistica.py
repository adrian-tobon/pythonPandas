import pandas as pd

fruits = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90], 
               'Stock': [30,50,20,60,40]
        
        }

df_fruits = pd.DataFrame(fruits)
print(df_fruits)

#sumarizacion

print(df_fruits['Precio'].sum())
print(df_fruits['Precio'].mean())
print(df_fruits['Precio'].median())
print(df_fruits['Precio'].min())
print(df_fruits['Precio'].max())
print(df_fruits['Precio'].std())
print(df_fruits['Precio'].var())
print(df_fruits['Precio'].describe())

#computacion
df_fruits['Suma acumulada Precios'] = df_fruits['Precio'].cumsum()
df_fruits['Producto acumulado Precios'] = df_fruits['Precio'].cumprod()
df_fruits['Diferencia Discreta Precios'] = df_fruits['Precio'].diff()
df_fruits['Cambio Porcentual Precios'] = df_fruits['Precio'].pct_change() * 100



#correlacion y covarianza
data = {
        'A':[1,2,3,4,5],
        'B':[5,4,3,2,1],
        'C':[2,3,4,5,6]        
        }

df_data = pd.DataFrame(data)
print(df_data)

'''pearson_correlation = df_data.corr(method='pearson')
kendall_correlation = df_data.corr(method='kendall')
spearman_correlation = df_data.corr(method='spearman')
covariance = df_data.cov()

print('Correlacion Pearson:\n',pearson_correlation)
print('Correlacion Kendall:\n',kendall_correlation)
print('Correlacion Spearman:\n',spearman_correlation)
print('Covarianza:\n',covariance)

print(type(pearson_correlation))
'''

#Conteo de Valores Unicos, Frecuencias y Modas
fruits_2 = {
               'Producto':['Manzanas','Naranjas','Platanos','Manzanas','Peras'],
               'Precio': [100,80,60,100,90], 
               'Stock': [30,50,20,30,40]
        
        }

df_fruits_2 = pd.DataFrame(fruits_2)
print(df_fruits_2)

valores_unicos = df_fruits_2.nunique()
print(valores_unicos)

frecuencia_productos = df_fruits_2.value_counts()
print(frecuencia_productos)

modas = df_fruits_2.mode()
print(modas)

#Uso de funciones de Ventana

data_2 = {
        'Fecha': pd.date_range(start='2025-01-01',periods=10,freq='D'),
        'Valor': [10,20,30,40,50,60,70,80,90,100]
        }

df_data_2 = pd.DataFrame(data_2)
df_data_2.set_index('Fecha', inplace=True)

print(df_data_2)

media_movil = df_data_2['Valor'].rolling(window=4).mean()
print(media_movil)

suma_movil = df_data_2['Valor'].rolling(window=4).sum()
print(suma_movil)

std_movil = df_data_2['Valor'].rolling(window=4).std()
print(std_movil)

