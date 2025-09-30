import pandas as pd

#Concatenacion y tipos de Joins en dataframes


data1 = {
        'Empleado':['Juan','Ana'],
        'Salario':[50000,60000]
    
}

data2 = {
        'Empleado':['Pedro','Luis'],
        #'Salario':[55000,58000]
        'Deudas':[55000,58000]
    
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df2)

#concatenacion por filas
df_concat = pd.concat([df1,df2],axis=0)

print(df1)
print(df2)
print(df_concat)

data3 = {
        'Empleado':['Juan','Ana'],
        'Departamento':['Ventas','Marketing']
    
}

data4 = {
        'Empleado':['Juan','Ana'],
        'Salario':[55000,58000]       
    
}

df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

df_concat2 = pd.concat([df3,df4],axis=1)

print(df3)
print(df4)
print(df_concat2)

#joins

data_left = {
        'Empleado':['Juan','Ana','Pedro'],
        'Salario':[50000,60000,55000]       
    
}

data_right = {
        'Empleado':['Ana','Pedro','Luis'],
        'Departamento':['Marketing','Ventas','IT']
    
}

df_left = pd.DataFrame(data_left)
df_right = pd.DataFrame(data_right)

df_inner = pd.merge(df_left,df_right,on="Empleado",how='inner')
print(df_inner)

df_outer = pd.merge(df_left,df_right,on="Empleado",how='outer')
print(df_outer)

df_left_join = pd.merge(df_left,df_right,on="Empleado",how='left')
print(df_left_join)

df_right_join = pd.merge(df_left,df_right,on="Empleado",how='right')
print(df_right_join)

#Agrupacion y operaciones de Agregacion

#Agrupacion
data5 = {
    'Empleado': ['Juan', 'Ana', 'Pedro', 'Luis', 'Maria', 'Ana', 'Pedro', 'Luis', 'Maria'],
    'Departamento': ['Ventas', 'Marketing', 'Ventas', 'IT', 'Marketing', 'IT', 'Ventas', 'Marketing', 'Ventas'],
    'Salario': [50000, 60000, 55000, 58000, 62000, 60000, 55000, 58000, 62000],
    'Años_Experiencia': [5, 7, 6, 8, 9, 7, 6, 8, 9]
}
df5 = pd.DataFrame(data5)
print(df5)

df_salary_by_dept = df5.groupby('Departamento')['Salario'].sum()
print(df_salary_by_dept)

df_experience_years_mean_by_dept = df5.groupby('Departamento')['Años_Experiencia'].mean()
print(df_experience_years_mean_by_dept)

df_salary_agg_by_dept = df5.groupby('Departamento')['Salario'].agg(['sum','max','min','mean'])
print(df_salary_agg_by_dept)


df_multiple_agg_by_dept = df5.groupby('Departamento').agg(
    {
        'Salario':['sum','max','min','mean'],
        'Años_Experiencia':['sum','max','min','mean']
        
    })
print(df_multiple_agg_by_dept)

df_multiple_agg_by_multiple_grouping = df5.groupby(['Departamento','Empleado']).agg(
    {
        'Salario':['sum','max','min','mean'],
        'Años_Experiencia':['sum','max','min','mean']
        
    })

print(df_multiple_agg_by_multiple_grouping)