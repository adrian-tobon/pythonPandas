import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Analisis de datos de series temporales

dates = pd.date_range(start='2025-01-01',periods=100,freq='D')

np.random.seed(0)
prices = np.random.lognormal(mean=0.001,sigma=0.02,size=len(dates))*100

df  = pd.DataFrame({'Fecha':dates,'Precio_Cierre':prices})
df.set_index('Fecha',inplace=True)

print(df.head())
print(df.describe())

#Media movil, maximos y minimos
df['Media_Movil'] = df['Precio_Cierre'].rolling(window=20).mean()
df['Maximos'] = df['Precio_Cierre'][(df['Precio_Cierre'] > df['Precio_Cierre'].shift(1)) & (df['Precio_Cierre'] > df['Precio_Cierre'].shift(-1))]
df['Minimos'] = df['Precio_Cierre'][(df['Precio_Cierre'] < df['Precio_Cierre'].shift(1)) & (df['Precio_Cierre'] < df['Precio_Cierre'].shift(-1))]


'''plt.figure(figsize=(12,6))
plt.plot(df.index,df['Precio_Cierre'],label='Precio Cierre')
plt.plot(df.index,df['Media_Movil'],label='Media Movil 20 dias',color='orange')
plt.scatter(df.index,df['Maximos'],label='Maximos',color='red')
plt.scatter(df.index,df['Minimos'],label='Minimos',color='green')
plt.xlabel('Fecha')
plt.ylabel('Precio Cierre')
plt.title('Precio de Cierre de Acciones')
plt.legend()
plt.show()'''

#Datos financieros

dates2 = pd.date_range(start='2025-01-01',periods=252,freq='B')#freq='B' indica dias habiles(Business Day)
np.random.seed(42)
prices2 = np.random.lognormal(mean=0.0005,sigma=0.01,size=len(dates2))*100

df2 = pd.DataFrame({'Fecha':dates2,'Precio_Cierre':prices2})
df2.set_index('Fecha',inplace=True)
print(df2)

#calcular retornos diarios
df2['Retorno_Diario'] = df2['Precio_Cierre'].pct_change()
df2['Media_Movil 20'] = df2['Precio_Cierre'].rolling(window=20).mean()
df2['Media_Movil 50'] = df2['Precio_Cierre'].rolling(window=50).mean()
df2['Rendimiento Acumulado'] =(1 + df2['Retorno_Diario']).cumprod()
print(df2)

'''
plt.figure(figsize=(14,7))
plt.plot(df2.index,df2['Precio_Cierre'],label='Precio Cierre')
plt.plot(df2.index,df2['Media_Movil 20'],label='Media Movil 20',color='purple')
plt.plot(df2.index,df2['Media_Movil 50'],label='Media Movil 50',color='yellow')
plt.xlabel('Fecha')
plt.ylabel('Precio Cierre')
plt.title('Precio de Cierre y Medias Moviles')
plt.legend()
plt.show()
'''
'''
plt.figure(figsize=(14,7))
plt.plot(df2.index,df2['Rendimiento Acumulado'],label='Rendimiento Acumulado',color='yellow')
plt.xlabel('Fecha')
plt.ylabel('Rendimiento Acumulado')
plt.title('Rendimiento Acumulado de la Accion')
plt.legend()
plt.show()
'''
'''
plt.figure(figsize=(14,7))
plt.plot(df2.index,df2['Retorno_Diario'],label='Retornos Diarios',color='orange')
plt.xlabel('Fecha')
plt.ylabel('Retorno Diario')
plt.title('Retorno Diario de la Accion')
plt.legend()
plt.show()
'''
#Analisis de datos de redes sociales
data3 = {
    'fecha': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'usuario': np.random.choice(['user1', 'user2', 'user3', 'user4'], size=100),
    'tweet': np.random.choice([
        'I love pandas for data analysis!', 
        'Python is awesome!', 
        'Just finished a great workout!', 
        'Pandas makes data manipulation easy.', 
        'Data science is fascinating!'
    ], size=100)
}
df3 = pd.DataFrame(data3)
print(df3)


all_tweets = ' '.join(df3['tweet'])
wordcloud = WordCloud(width=800,height=400,background_color='white').generate(all_tweets)
'''
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud de tweets')
plt.show()
'''
tweets_por_dia = df3['fecha'].value_counts().sort_index()
'''
plt.figure(figsize=(12,6))
tweets_por_dia.plot(kind='line',marker='o',color='blue')
plt.xlabel('Fecha')
plt.ylabel('Numero de Tweets')
plt.title('Numero de Tweets por dia')
plt.show()
'''

tweets_por_usuario = df3['usuario'].value_counts()

plt.figure(figsize=(12,6))
tweets_por_usuario.plot(kind='bar',color='coral')
plt.xlabel('Usuario')
plt.ylabel('Numero de Tweets')
plt.title('Numero de Tweets por usuario')
plt.show()