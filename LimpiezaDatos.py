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

#Transformacion de Datos

#Funciones

data_empleado = {
        'Empleado':['Juan','Ana','Pedro','Luis','Maria'],
        'Salario': [50000,60000,55000,58000,62000], 
        'Años_Experiencia': [5,7,6,8,9]
      }

df_empleados = pd.DataFrame(data_empleado)
print(df_empleados)

def calcular_salario_ajustado(row):
        salario = row['Salario']
        anios_experiencia = row['Años_Experiencia']
        bono = 0.05 * anios_experiencia * salario
        salario_ajustado = salario + bono
        return salario_ajustado

def normalizar_serie(serie):
        return (serie - serie.mean())/serie.std()

df_empleados['Salario Ajustado'] = df_empleados.apply(calcular_salario_ajustado,axis=1)
print(df_empleados)


df_empleados[['Salario Normalizado','Años Normalizado']] = df_empleados[['Salario','Años_Experiencia']].apply(normalizar_serie)
print(df_empleados)

# mapeo

def categorizar_salario(salario):
        if salario > 60000:
                return 'Alto'
        elif salario > 55000:
                return 'Medio'
        else:
                return 'Bajo'
        
        
df_empleados['Categoria Salario']  = df_empleados['Salario'].map(categorizar_salario)
print(df_empleados)

def formatear_valor(x):
        if isinstance(x,(int,float)):
                return f"${x:,.2f}"      
        return x


df_empleados['Salario']  = df_empleados['Salario'].map(formatear_valor)
df_empleados['Salario Ajustado']  = df_empleados['Salario Ajustado'].map(formatear_valor)
#df_format = df_empleados.map(formatear_valor)
#print(df_format)
print(df_empleados)

#renombrar y reorganizar indices y columnas
data_empleados2 = {
        'Empleado':['Juan','Ana','Pedro','Luis','Maria'],
        'Salario': [50000,60000,55000,58000,62000], 
        'Años_Experiencia': [5,7,6,8,9]
      }

df_empleados2 = pd.DataFrame(data_empleados2)
print(df_empleados2)

df_empleados2.rename(columns={"Salario":"Salario Anual","Años_Experiencia":"Experiencia"},inplace=True)
print(df_empleados2)

df_empleados2.columns = ["Trabajador", "Sueldo", "Años"]
print(df_empleados2)

df_empleados2.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E"},inplace=True)
print(df_empleados2)

df_empleados2.index = [100, 200, 300,400,500]
print(df_empleados2)

df_reordenado_columnas = df_empleados2.reindex(columns= ["Años", "Trabajador", "Sueldo"])
print(df_reordenado_columnas)

df_empleados2 = df_empleados2[["Años", "Sueldo", "Trabajador"]]
print(df_empleados2)

df_reordenado_indices = df_empleados2.reindex(index=[500,400,300,200,100])
print(df_reordenado_indices)

df_reordenado_indices.sort_index(inplace=True,ascending=False)
print(df_reordenado_indices)

#Deteccion y filtrado de valores atipicos


data_empleados3 = {
        'Empleado':['Juan','Ana','Pedro','Luis','Maria','Pedro'],
        'Salario': [50000,60000,55000,58000,120000,500], #el ultimo valor es un salario atipico
        'Años_Experiencia': [5,7,6,8,9,1]
      }


df_empleados3 = pd.DataFrame(data_empleados3)
print(df_empleados3)

media_salario = df_empleados3['Salario'].mean()
std_salario = df_empleados3['Salario'].std()

print("Media: ",media_salario)
print("Desviacion Estandar: ",std_salario)

umbral = 1

df_empleados3['Atipico Media y Desviacion'] = abs(df_empleados3['Salario'] - media_salario) > umbral*std_salario
print(df_empleados3)

Q1 = df_empleados3['Salario'].quantile(0.25)
Q3 = df_empleados3['Salario'].quantile(0.75)
IQR = Q3 - Q1 #rango intercuartilico

umbral_inferior = Q1 - 1.5 * IQR
umbral_superior = Q3 + 1.5 * IQR

df_empleados3['Atipico Cuartiles'] = (df_empleados3['Salario'] < umbral_inferior) | (df_empleados3['Salario'] > umbral_superior)
print(df_empleados3)

df_atypical = df_empleados3[~df_empleados3['Atipico Cuartiles']]
print(df_atypical)


df_empleados3.loc[df_empleados3['Atipico Cuartiles'], 'Salario'] = media_salario
print(df_empleados3)