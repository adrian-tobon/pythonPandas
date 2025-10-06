import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sqlalchemy import create_engine
from sqlalchemy import text
import psycopg2
import pymysql


#conexion a base de datos SQLite

#base de datos en memoria
engine = create_engine('sqlite:///:memory:')
#base de datos persistente
#engine2 = create_engine('sqlite:///my_database.db')

data = {
    'Empleado': ['Juan', 'Ana', 'Pedro', 'Luis', 'Maria', 'Ana', 'Pedro', 'Luis', 'Maria'],
    'Departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'Marketing', 'Ventas'],
    'Salario': [50000, 60000, 55000, 58000, 62000, 60000, 55000, 58000, 62000],
    'Años_Experiencia': [5, 7, 6, 8, 9, 7, 6, 8, 9]
}
df = pd.DataFrame(data)
print(df)

df.to_sql('empleados',engine,index=False,if_exists='replace')


data_db_empleados = pd.read_sql('empleados',engine)
print(data_db_empleados)

query_empleados = 'select Empleado, Salario from empleados where Salario > 50000'
data_db_query_empleados = pd.read_sql(query_empleados,engine)
print(data_db_query_empleados)

update_query = "UPDATE empleados set Salario = Salario * 1.1 where Departamento = 'Ventas'"

with engine.connect() as con:
    con.execute(text(update_query))
    con.commit()
    con.close()

delete_query = 'delete from empleados where Empleado = "Juan"'

with engine.connect() as con:
    con.execute(text(delete_query))
    con.commit()
    con.close()
    
insert_query = "insert into empleados (Empleado,Departamento,Salario,Años_Experiencia) values('Antonio','Ventas','20000',0)"    

with engine.connect() as con:
    con.execute(text(insert_query))
    con.commit()
    con.close()
    
df_actualizado = pd.read_sql('empleados',engine)
print(df_actualizado) 

#Numpy y Scipy

#Numpy
data2 = {
    'A': [1,2,3,4,5],
    'B': [10,20,30,40,50]    
}

df2 = pd.DataFrame(data2)
print(df2)

df2['sqrt_A'] = np.sqrt(df2['A'])
print(df2)

df2['suma acumulada A'] = np.cumsum(df2['B'])
print(df2)

df2.loc[1,'B'] = np.multiply(5,df2.loc[1,'B'])
print(df2)

#Scipy
data3 = {
    'x':np.random.rand(100),
    'y':np.random.rand(100)
}

df3 = pd.DataFrame(data3)
print(df3)

correlacion,p_valor = stats.pearsonr(df3['x'],df3['y'])
print(correlacion)
print(p_valor)

slope,intercept,r_value,p_value,std_err = stats.linregress(df3['x'],df3['y'])
'''print(slope)
print(intercept)
print(r_value)
print(p_value)
print(std_err)
'''

print(f"Regresion Lineal = {slope} *x + {intercept}")


data4 = {
    'valores':np.random.rand(100)    
}

df4 = pd.DataFrame(data4)
df4['exp_valores'] = np.exp(df4['valores'])
print(df4)

muestra = np.random.rand(100) + 2
t_stat,p_value2 = stats.ttest_1samp(muestra,2) 
print(f"Prueba t de una muestra: t-statistic = {t_stat}, p-valor = {p_value2}")


#Bibliotecas de visualizacion
#Matplotlib
data5 = {
    'Mes':['Enero', 'Febrero','Marzo','Abril','Mayo'],
    'Ventas':[200,300,400,500,600]
    
}

df5 = pd.DataFrame(data5)
print(df5)

plt.figure(figsize=(10,6))
plt.bar(df5['Mes'],df5['Ventas'],color='skyblue')
plt.xlabel('Mes')
plt.ylabel('ventas')
plt.legend()
#plt.show()

data6 = {
    'Empleado': ['Juan', 'Ana', 'Pedro', 'Luis', 'Maria', 'Ana', 'Pedro', 'Luis', 'Maria'],
    'Departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'Marketing', 'Ventas'],
    'Salario': [50000, 60000, 55000, 58000, 62000, 60000, 55000, 58000, 62000],
    'Años_Experiencia': [5, 7, 6, 8, 9, 7, 6, 8, 9]
}
df6 = pd.DataFrame(data6)
print(df6)

salarios_depto = df6.groupby('Departamento')['Salario'].sum()
print(salarios_depto)

plt.figure(figsize=(10,6))
salarios_depto.plot(kind='bar',color='lightgreen')
plt.xlabel('Departamento')
plt.ylabel('Suma de Salarios')
plt.title('Suma de Salarios por Departamento')
#plt.show()

#Seaborn
plt.figure(figsize=(10,6))
sns.boxplot(x='Departamento',y='Salario',data=df6)
plt.title('Suma de Salarios por Departamento')
plt.show()
