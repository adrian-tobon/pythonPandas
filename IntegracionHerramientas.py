import pandas as pd
from sqlalchemy import create_engine

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