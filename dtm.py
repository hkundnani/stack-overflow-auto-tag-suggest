# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:05:00 2018

@author: Ankita
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("processed_data.csv")
df = df.drop(["post_type_id", "view_count", "answer_count"], axis =1)
print(df.head())
vectorizer = CountVectorizer(input = 'content', stop_words = 'english')

dtm = vectorizer.fit_transform(df['body'])
print(dtm.shape)
for i, col in enumerate(vectorizer.get_feature_names()):
    df[col] = pd.SparseSeries(dtm[:, i].toarray().ravel(), fill_value=0)
print(df.shape)
df.to_csv("test_dtm.csv", encoding='utf-8', mode = 'a', index=False)
#df = df[df.columns.drop(list(df.filter(regex='\d+')))]