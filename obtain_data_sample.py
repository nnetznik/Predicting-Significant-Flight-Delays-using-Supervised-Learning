# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:22:32 2022

@author: nnetznik
"""

import pandas as pd
import os

path = "C:/Users/nnetznik/Documents/Capstone/data/"
files = os.listdir(path)
 
df_list = [pd.read_csv(path+file) for file in files]
df = pd.concat(df_list, axis=0).sample(25000, axis=0, random_state=100)

df.to_csv(path+'sample.csv')

