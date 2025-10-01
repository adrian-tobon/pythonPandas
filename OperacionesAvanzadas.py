from random import randint
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

#agregacion
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

#uso avanzado del groupby

df5['Salario Normalizado'] = df5.groupby('Departamento')['Salario'].transform(lambda x: (x - x.mean())/x.std())
print(df5)

df_filter = df5.groupby('Departamento').filter(lambda x: len(x) > 2)
print(df_filter)

data6 = {
        
        'Fecha':pd.date_range(start='2025-01-01',periods=90,freq='D'),
        'Ventas':[randint(1000,99999) for i in range(90)]
}

df6 = pd.DataFrame(data6)
df6.set_index('Fecha',inplace=True)

df_by_week = df6.groupby(pd.Grouper(freq='1M'))['Ventas'].sum()
print(df_by_week)

def rango_salarial(x):
        return x['Salario'].max() - x['Salario'].min()

def mean_salario(x):
        return x['Salario'].mean()

df5_normalized = df5.groupby('Departamento').apply(rango_salarial)
print(df5_normalized)

#Pivot Tables

print(df5)
pivot_table = df5.pivot_table(values='Salario',index='Departamento',aggfunc=['sum','mean'])
print(pivot_table)

pivot_table_years = df5.pivot_table(values='Salario',index=['Departamento','Empleado'],columns='Años_Experiencia',aggfunc=['sum','mean'])
print(pivot_table_years)

#cross tabulation
cross_tab = pd.crosstab(df5['Departamento'],df5['Empleado'], values=df5['Salario'],aggfunc='sum',margins=True)
print(cross_tab)

cross_tab_normalize = pd.crosstab(df5['Departamento'],df5['Empleado'],normalize='index') 
print(cross_tab_normalize)

#Datos categoricos
df5['Departamento'] = df5['Departamento'].astype('category')
print(df5['Departamento'])

print(df5['Departamento'].cat.categories)
print(df5['Departamento'].cat.codes)

df5['Departamento'] = df5['Departamento'].cat.reorder_categories(['IT','Ventas','Marketing'],ordered=True)
print(df5['Departamento'])
print(df5['Departamento'].cat.codes)


df5['Departamento'] = df5['Departamento'].cat.add_categories(['Recursos Humanos'])
print(df5['Departamento'])

df5['Departamento'] = df5['Departamento'].cat.remove_categories(['Recursos Humanos'])
print(df5['Departamento'])
