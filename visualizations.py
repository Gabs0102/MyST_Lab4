import pandas as pd
import plotly.express as px

#Crear visualización 
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def graficas(df, symbol): 
    # Datos del dataframe son : level,
    # Seleccionar las exchanges y los datos correspondientes
    exchanges = ["bitforex", "huobipro", "bitmart"]
    data = {}
    for exchange in exchanges:
        data[exchange] = df[df.exchange == exchange]

    # Generar los subplots
    fig = make_subplots(rows=2, cols=3, subplot_titles=('Level', 'ask_volume', 'bid_volume', 'total_vol', 'mid_price', 'vwap'))

    # Graficar cada exchange en su subplot correspondiente
    row = 1
    col = 1
    for exchange in exchanges:
        df_exchange = data[exchange]
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.Level, mode='lines', name=f'{exchange} Level'), row=row, col=col)
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.ask_volume, mode='lines', name=f'{exchange} ask_volume'), row=row, col=col+1)
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.bid_volume, mode='lines', name=f'{exchange} bid_volume'), row=row, col=col+2)
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.total_vol, mode='lines', name=f'{exchange} total_vol'), row=row+1, col=col)
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.mid_price, mode='lines', name=f'{exchange} mid_price'), row=row+1, col=col+1)
        fig.add_trace(go.Scatter(x=df_exchange.timeStamp, y=df_exchange.vwap, mode='lines', name=f'{exchange} vwap'), row=row+1, col=col+2)

        # Actualizar la posición actual de los subplots
        if col == 1:
            col += 2
        else:
            col = 1
            row += 1

    # Mostrar la figura
    return fig.show()