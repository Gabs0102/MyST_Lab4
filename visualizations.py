import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graficas(df, symbol):
    # separar el DataFrame por exchanges
    exchanges = df['exchange'].unique()

    # crear la figura
    fig = make_subplots(rows=2, cols=3,
                        subplot_titles=('Level', 'ask_volume', 'bid_volume', 'total_vol', 'mid_price', 'vwap'))

    # añadir trazas para cada exchange
    for i, exchange in enumerate(exchanges, start=1):
        df_exchange = df[df['exchange'] == exchange]

        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['Level'], mode='lines', name=f'{exchange} Level'), row=1, col=i)
        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['ask_volume'], mode='lines', name=f'{exchange} ask_volume'), row=1, col=i)
        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['bid_volume'], mode='lines', name=f'{exchange} bid_volume'), row=1, col=i)
        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['total_vol'], mode='lines', name=f'{exchange} total_vol'), row=2, col=i)
        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['mid_price'], mode='lines', name=f'{exchange} mid_price'), row=2, col=i)
        fig.add_trace(go.Scatter(x=df_exchange['timeStamp'], y=df_exchange['vwap'], mode='lines', name=f'{exchange} vwap'), row=2, col=i)

    # actualizar el layout y mostrar la figura
    fig.update_layout(height=600, width=1000, title=f'{symbol} - Order Book Data')
    fig.show()



# ETH_BTC = pd.read_csv(r'files\orderbooks_27abr.csv')
# ETH_BTC = ETH_BTC.drop(['Unnamed: 0'],axis=1)
# ETH_BTC_1 = ETH_BTC.drop(['close_price','spread','effective_spread'],axis=1)
# graficas(ETH_BTC_1,'ETH_BTC')