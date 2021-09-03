#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
rollercoaster=pd.read_excel("Rollercoasters.xlsx")

rollercoaster.columns = ["name", "height", "drop_height", "type", 
                         "inversions", "length", "speed", 
                         "duration", "angle"]
rollercoaster.head(22)
def funfactor(df, name):
    alreadychecked=0  #eliminate duplication of information
    for z in df.index:  #go through all the index values
        if df.loc[z,"name"]==name and alreadychecked==0:    #found the zip we requested (first-time)
            alreadychecked=1  #we will only do this once
            df1=df[df["name"]==name]
    return ("Enter a different rollercoaster if you wish.")
funfactor(rollercoaster, "Kingda Ka")

