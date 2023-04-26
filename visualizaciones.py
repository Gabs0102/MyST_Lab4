#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 07:50:23 2023

@author: gabrielaortiz



"""


#Crear visualización 
fig = px.line(df,x='timeStamp', y='mid_price', color='exchange',facet_col='Level',facet_col_wrap=2)
fig= px.line(df,x='timeStamp',y='mid_price',color='exchange')
fig.show()
