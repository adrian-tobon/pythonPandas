import pandas as pd

def discount(precio):
        return precio * 0.85

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

#Indexacion, Seleccion y filtrado
fruits_3 = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90],
                'Stock': [30,50,20,60,40]
        }

df_fruits3 = pd.DataFrame(fruits_3)
#df_fruits3.set_index('Producto',inplace=True)
print(df_fruits3)

#print(df_fruits3['Precio'])
print(df_fruits3.loc[1,['Precio']])
print(df_fruits3.loc[1,['Producto','Stock']])
print(df_fruits3.iloc[1,[0,2]])

print(df_fruits3[(df_fruits3.index >= 3) & (df_fruits3['Stock'] > 50)])
print(df_fruits3.loc[(df_fruits3.index >= 3) | (df_fruits3['Stock'] > 50)])
print(df_fruits3.iloc[df_fruits3.index >= 3])

print(df_fruits3[df_fruits3.index >= 3].where(df_fruits3['Stock'] > 50,other=0))
print(df_fruits3.loc[df_fruits3.index >= 3].where(df_fruits3['Stock'] > 50,other=0))
print(df_fruits3.iloc[df_fruits3.index >= 3].where(df_fruits3['Stock'] > 50,other=0))


print(df_fruits3[df_fruits3.index >= 3].query('Stock > 50'))
print(df_fruits3.loc[df_fruits3.index >= 3].query('Stock > 50'))
print(df_fruits3.iloc[df_fruits3.index >= 3].query('Stock > 50'))

#funciones aritmetica y alineacion de datos

#alineacion de series y dataframes
s1 = pd.Series([10,20,30],index=['a','b','c'])
s2 = pd.Series([40,50,60,70],index=['b','c','d','e'])

s3 = s1+s2
print(s3)

s4 = s1.add(s2,fill_value=0)
print(s4)

df1 = pd.DataFrame({'A':[1,2],'B':[3,4]},index=[1,2]) 
df2 = pd.DataFrame({'B':[5,6],'C':[7,8]},index=[2,3])

df3 = df1 + df2
print(df3)

df4 = df1.add(df2,fill_value=0)
print(df4) 

#Aplicacion de funciones y mapeo

#Aplicaion de funciones en dataframes
fruits_4 = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90]               
        }

df_fruits4 = pd.DataFrame(fruits_4)
print(df_fruits4)

df_fruits4['Precio con descuento'] = df_fruits4['Precio'].apply(discount)
print(df_fruits4)

df_fruits4['Producto'] = df_fruits4['Producto'].apply(lambda x: x.upper())
print(df_fruits4)

#mapeo
fruits_5 = {
               'Producto':['Manzanas','Naranjas','Platanos','Uvas','Peras'],
               'Precio': [100,80,60,120,90]               
        }

df_fruits5 = pd.DataFrame(fruits_5)
print(df_fruits5)

#df_fruits5['Producto'] = df_fruits5['Producto'].map({'Manzanas':'Apples','Naranjas':'Oranges'})

mapping = {'Manzanas':'Apples','Naranjas':'Oranges'}
df_fruits5['Producto'] = df_fruits5['Producto'].map(lambda x: mapping.get(x,x))

df_fruits5 = df_fruits5.map(lambda x: x.lower() if type(x) == str else x)
print(df_fruits5)

df_fruits5['Descuento'] = [10, 15, 10, 20,5]

df_fruits5['Valor Final'] = df_fruits5.apply(lambda x: x['Precio'] - (100 - x['Descuento']) /100, axis = 1)
print(df_fruits5)
