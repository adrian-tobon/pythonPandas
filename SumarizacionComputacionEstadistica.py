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
df_fruits['Suma acumulada Precios'] = df_fruits['Precio'].cumsum()
df_fruits['Suma acumulada Precios'] = df_fruits['Precio'].cumsum()
print(df_fruits)