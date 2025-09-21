import pandas as pd

fruits = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90] 
        
        }

df_fruits = pd.DataFrame(fruits)
print(df_fruits)

df_fruits.set_index('Producto',inplace=True)
print(df_fruits)

df_fruits_reindexed = df_fruits.reindex(['Naranjas','Manzanas','Platanos','Peras','Uvas','Melones'])
print(df_fruits_reindexed)

df_fruits.rename(index={'Manzanas':'Apples','Naranjas':'Oranges'},inplace=True)
#modificar un campo en una fila
df_fruits.loc['Apples','Precio'] = 130
print(df_fruits)



df_fruits.loc['Fresas'] = {'Precio': 42}
print(df_fruits)


otro_indice = ['Melones', 'Manzanas', 'Peras']
interseccion_indices = df_fruits.index.intersection(otro_indice)
print(interseccion_indices)

print(df_fruits.loc['Apples','Precio'])

df_fruits.reset_index(inplace=True)
print(df_fruits)

#ejes(axis) de un dataframe
fruits_2 = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90],
                'Stock': [30,50,20,60,40]
        }

df_fruits2 = pd.DataFrame(fruits_2)
df_fruits2.set_index('Producto',inplace=True)
print(df_fruits2)

df_fruits2.drop('Manzanas',axis=0,inplace=True)
df_fruits2.drop('Stock',axis=1,inplace=True)
print(df_fruits2)

