import pandas as pd

#Manejo de datos faltantes
data = {
        'A':[1,2,None,4,5],
        'B':[None,2,3,4,None],
        'C':[1,2,3,None,5]
        }


df = pd.DataFrame(data)
print(df)

null_data = df.isnull().sum()
print(null_data)

#df.dropna(inplace=True,axis=1)
#df.drop(len(df)-1,axis=0, inplace=True)
#df.fillna(0,inplace=True)
#df.fillna(df.mean(),inplace=True)
#df.bfill(inplace=True)
#df.ffill(inplace=True)
print(df)

#filtrado de datos
fruits = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90], 
               'Stock': [30,50,20,60,40]
        
        }

df_fruits = pd.DataFrame(fruits)
print(df_fruits)

print(df_fruits[(df_fruits['Precio']>80) & (df_fruits['Stock']>30)])
print(df_fruits[(df_fruits['Precio']>80) | (df_fruits['Stock']>30)])
print(df_fruits[~(df_fruits['Precio']>80)])


print(df_fruits[df_fruits['Producto'].str.contains('v')])
print(df_fruits[['Precio','Producto']])

print(df_fruits.loc[1,['Precio','Producto']])

print(df_fruits.query('Precio > 80 and Stock >30'))

print(df_fruits[df_fruits['Producto'].isin(['Platanos','Peras'])])


