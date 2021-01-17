#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


def foo(data):
    
    max_element = data[data.price == data.price.max()].head(1)
    min_element = data[data.price == data.price.min()].head(1)
    
    max_date = max_element.date.values[0]
    max_index = max_element.index[0]
    min_date = min_element.date.values[0]
    min_index = min_element.index[0]
    if max_date<min_date:
        temp = data.iloc[min_index:]
        max_element = temp[temp.price == temp.price.max()].head()
        
    
    print('Прибыль которую можно получить: ', max_element.price.values[0] - min_element.price.values[0])
    print('Дата покупки:', min_element.date.values[0], 'Время покупки: ', min_element.time.values[0])
    print('Дата продажи:', max_element.date.values[0], 'Время продажи: ', max_element.time.values[0])


# In[9]:


my_data = pd.read_csv(r"./new.csv", index_col =0)
foo(my_data)


# In[ ]:




