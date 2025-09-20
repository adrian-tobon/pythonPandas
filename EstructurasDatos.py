import pandas as pd
import numpy as np

#series: creacion, manipulacion y uso 
s_1 = pd.Series([1,2,3,4,5])

print(s_1)

s_2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

print(s_2)

s_3 = pd.Series([1,2.5,3,4.5,5])

s_4 = s_3 ** 2

datos = {'a':1,'b':2,'c':3}
s_dict = pd.Series(datos)

print(s_dict)

print(s_1[3])
print(s_2['b'])

#operaciones sobre series
print(s_1.add(s_3))
print(s_1.sub(s_3))
print(s_1.mul(s_3))
print(s_1.div(s_3))

print(s_1.mean())
print(s_1.min())
print(s_1.max())

#filtrado de datos sobre las series
print(s_4[s_4 > 3])
print(s_4[s_4 <= 3])

#aplicacion de funciones 
print(s_4.apply(np.log))

#combinacion de series usando dataframe
nombres = pd.Series(['Ana','Luis','Pedro'])
edades = pd.Series([25,30,35])

df_nombre = pd.DataFrame({'Nombre':nombres, 'Edad':edades})
print(df_nombre.head())

#Dataframes
data_list_dict = [{'Nombre': 'Ana', 'Edad': 25, 'Ciudad': 'Madrid'},
        {'Nombre': 'Luis', 'Edad': 30, 'Ciudad': 'Barcelona'},
        {'Nombre': 'Pedro', 'Edad': 22, 'Ciudad': 'Valencia'}]

print(type(data_list_dict))

df_list_dict = pd.DataFrame(data_list_dict)
print(df_list_dict.head())

data_dict_list = {  'Nombre': ['Ana','Luis','Pedro','Ana'],
                    'Edad':[25,30,22,29],
                    'Ciudad': ['Madrid','Barcelona','Valencia','Sevilla']}

df_dict_list = pd.DataFrame(data_dict_list)
print(df_dict_list)

#operaciones sobre Dataframes
nombres_2 = df_dict_list['Nombre']
print(nombres_2)

df_dict_list['Salario'] = ['2000','4000','4000','10000']
print(df_dict_list)

df_dict_list.drop('Salario',axis=1,inplace=True)
print(df_dict_list)


df_dict_list.loc[len(df_dict_list)] = {'Nombre': 'Jorge','Edad': 42,'Ciudad':'Alicante'}
print(df_dict_list)

df_dict_list.drop(len(df_dict_list) - 1 ,axis=0,inplace=True)
print(df_dict_list)


print(df_dict_list.iloc[0])

print(df_dict_list.loc[df_dict_list['Nombre']== 'Ana'])
print(df_dict_list.loc[df_dict_list['Edad'] < 30])

df_dict_list.sort_values(by='Edad',ascending=True, inplace=True)
print(df_dict_list)

