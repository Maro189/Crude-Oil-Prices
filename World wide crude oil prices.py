#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing packages
import pandas as pd
import numpy as np

# defining dataframe and opening csv file
df = pd.read_csv(r'G:\Python projects\oil prices\crude-oil-prices.csv')

# dropping indicies
df = df.drop(df.index[0:99])

# dropping columns
df = df.drop(columns = ['Entity', 'Code'])

# resetting index
df = df.reset_index(drop = True)

# remaning columns
df = df.rename(columns={'Oil - Crude prices since 1861 (current $)': 'Crude Oil Prices ($)'})
df


# In[2]:


# importing package for visualisation
import matplotlib.pyplot as plt

# plotting graph
ax = df.plot(x = 'Year', y = 'Crude Oil Prices ($)', color= 'darkcyan', figsize = (30, 20), fontsize = 20)
ax.set_xlabel("Year", fontdict={'fontsize':24})
ax.set_ylabel("Price ($)",fontdict={'fontsize':24})
ax.legend(loc=2,fontsize=30)
ax.set_title("Worldwide Crude Oil Prices USD (1960-2021)", fontdict={'fontsize':24})
plt.show()


# In[ ]:




