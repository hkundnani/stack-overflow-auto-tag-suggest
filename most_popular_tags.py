# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 20:12:17 2018

@author: Ankita
"""
import pandas as pd
from collections import Counter

chunksize = 10000
i =0
tag_final =[]

for chunk in pd.read_csv("E:/processed_data.csv", chunksize=chunksize):
    
    tags = chunk["tags"].tolist()
    tag_final = tag_final+tags
    i=i+1
    if(i==2):
        break
   # most_popular(tags)
print(tags[0:5])


mostcommon_tags= [item for item in Counter(tag_final).most_common(850)]
print("top 850 most frequent tags in the dataset?:")
print(str(mostcommon_tags))

