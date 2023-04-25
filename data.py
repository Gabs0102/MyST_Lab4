#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:03:29 2023

@author: gabrielaortiz
"""
from sklearn.datasets import load_iris
import pandas as pd

df = pd.DataFrame(load_iris().data)

# 'sepal_lenght','sepal_width','petal_lenght','petal_width'
df.columns = ['sepal_lenght', 'sepal_width','petal_lenght','petal_width']
print(df)
