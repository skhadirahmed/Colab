# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:43:24 2019

@author: skhad
"""

import pandas as pd

df = pd.read_excel("Data_Train.xlsx")

print(df.head())

train1 = df["Location"]

print(train1.head())