import pandas as pd
import requests
import mplfinance as mpf #libreria construida sobre matplotlib para visualizaciones de datos financieros
import matplotlib.pyplot as plt

def obtener_datos_historicos(criptomoneda, vs_moneda, dias):
    url = f'https://api.coingecko.com/api/v3/coins/{criptomoneda}/market_chart'
    parametros = {
        'vs_currency': vs_moneda,
        'days': dias
    }
    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()
    precios = datos['prices']
    df = pd.DataFrame(precios, columns=['timestamp', 'precio'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df


df = obtener_datos_historicos('bitcoin', 'usd', 60)
print(df)

#resample() - ajusta las series temporales de acuerdo a una frecuencia
#ohlc() - permite definir valores open high low y close(primero, maximo, minimo y ultimo) luego de un resample
df_candlestick = df['precio'].resample('D').ohlc()
print(df_candlestick)

mpf.plot(df_candlestick,type='candle',style='charles',title='Bitcoin - Velas Japonesas',ylabel='Precio (USD)')

df.describe()

df['Media_Movil 20'] = df['precio'].rolling(window=20).mean()
#df['Media_Movil 50'] = df['precio'].rolling(window=50).mean()

plt.figure(figsize=(14,7))
plt.plot(df.index,df['precio'],label='Precio de Cierre')
plt.plot(df.index,df['Media_Movil 20'],label='Media Movil 20 dias',color='orange')
#plt.plot(df.index,df['Media_Movil 50'],label='Media Movil 50 dias',color='red')
plt.title('Precio de Cierre de Bitcoin')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.legend()
plt.show()

'''
1. **Carga y Exploración de Datos**:
   - **Inspección Inicial**: Siempre revisa una muestra de los datos con `head()` y `tail()`.
   - **Información del DataFrame**: Usa `info()` para obtener una visión general del DataFrame.
   - **Estadísticas Descriptivas**: Utiliza `describe()` para obtener un resumen estadístico rápido.

2. **Limpieza y Preparación de Datos**:
   - **Manejo de Datos Faltantes**: Decide cómo tratar los valores faltantes: `dropna()`, `fillna()`.
   - **Tipos de Datos**: Asegúrate de que los tipos de datos son correctos (`astype()`).
   - **Renombrar Columnas**: Usa nombres de columnas claros y consistentes (`rename()`).

3. **Manipulación de Datos**:
   - **Selección y Filtrado**: Utiliza técnicas de selección eficientes (`loc`, `iloc`).
   - **Filtrado Condicional**: Filtra datos utilizando condiciones (`df[df['col'] > value]`).
   - **Operaciones Vectorizadas**: Aprovecha las operaciones vectorizadas para mejorar el rendimiento.

4. **Agrupación y Agregación**:
   - **Agrupación Inteligente**: Usa `groupby()` para realizar análisis segmentados.
   - **Agregaciones Personalizadas**: Aplica funciones de agregación específicas a tus grupos (`agg()`).

5. **Análisis de Series Temporales**:
   - **Índices de Fecha**: Asegúrate de que tu DataFrame tiene un índice de fecha (`set_index()`).
   - **Resampling y Rolling**: Usa `resample()` y `rolling()` para análisis de series temporales.

6. **Visualización de Datos**:
   - **Gráficos Simples**: Empieza con gráficos simples para entender la distribución de los datos.
   - **Gráficos Avanzados**: Utiliza bibliotecas como Seaborn y Plotly para visualizaciones más complejas e interactivas.

7. **Código Limpio y Documentado**:
   - **Funciones y Modulares**: Divide el código en funciones para mayor claridad y reutilización.
   - **Comentarios y Documentación**: Agrega comentarios y docstrings para explicar el propósito y el funcionamiento del código.
   - **Consistencia**: Mantén un estilo de código consistente para mejorar la legibilidad y el mantenimiento.
'''


