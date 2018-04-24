# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:05:31 2018

@author: Ankita
"""

import pandas as pd
# REad Files: List of Tags and REsult of SVM
result_df = pd.read_csv("result_new.csv", header =0)
tag_dfdf = pd.read_csv("tag_list.csv", header = 0)

# Merge to get Tag Predicted
tag_df = pd.merge(result_df, tag_dfdf, on = 'Model')
tag_df['Question'] = tag_df['Question'].str.split('n').str[1]
tag_df['only_tag'] = tag_df['actual_tag'].str.split(" ").str[1] 

# Finding accuracy for prediction - each question    
df_not =  tag_df[tag_df['actual_tag'].str.contains("not")]
df_present = tag_df[~tag_df['actual_tag'].str.contains("not")]
df_present['Accuracy'] = df_present.apply(lambda x: 1 if x['only_tag'] == x['Tag'] else 0, axis=1)
df_not['Accuracy'] = df_not.apply(lambda x: 1 if x['only_tag'] != x['Tag'] else 0, axis=1)
df = df_present.append(df_not)

# Accuracy if any tag among top 5 matches correct prediction for the question
accuracy = df.groupby('Question')['Accuracy'].agg(['sum'])
accuracy = accuracy.sort_index()  
accuracy['Question']= accuracy.index.values

# Finding accuracy for all 850 models
model =[]
x=0
for j in range(850):
    for i in range(x, x+20):
       
        tag_df_mid = accuracy.loc[accuracy['Question']== str(i)]
        if i==j:
            df_final = tag_df_mid
        else:
            df_final = df_final.append(tag_df_mid)
    #    df_final.columns =['Accuracy', 'Question', 'Sum']
        df_final['sum'] = df_final.apply(lambda x: 0 if x['sum'] == 0 else 1, axis=1)
    model.append(df_final['sum'].mean())
    x+=20
        
        
