import pandas as pd
import plotly.express as px

#Crear visualización 
def graficos(df:"DataFrame"):
    fig = px.line(df,x='timeStamp', y='mid_price', color='exchange',facet_col='Level',facet_col_wrap=2)
    fig= px.line(df,x='timeStamp',y='mid_price',color='exchange')
    fig.show()