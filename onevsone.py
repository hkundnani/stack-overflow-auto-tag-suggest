# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:49:12 2018

@author: Ankita
"""
import pandas as pd
from scipy.sparse import hstack
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
#from sklearn.svm import score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import linear_model, datasets
from sklearn.metrics import precision_score

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
file_train = "onevsone.csv"

file_test = "onevsone_test.csv"

#chunksize = 100000
#j=0
#for chunk in pd.read_csv(file_test, chunksize=chunksize):
#    
#    df = chunk[~chunk.common_tag.str.contains('notpresent')]
#    j=j+1
#    if(j==0):
#        header = True
#    else:
#        header = False
#        
#    df.to_csv("onevsone_test.csv", encoding='utf-8', mode = 'a', index=False)

df_train = pd.read_csv(file_train)
df_test = pd.read_csv(file_test)

df_test = df_test.drop(["post_type_id", "view_count", "answer_count"], axis =1)
df_train = df_train.drop(["post_type_id", "view_count", "answer_count"], axis =1)
vectorizer = CountVectorizer(input = 'content', stop_words = 'english')

dtm1 = vectorizer.fit_transform(df_train['body'])
dtm2 = vectorizer.transform(df_test['body'])

print(dtm1.shape)
print(dtm2.shape)
le = LabelEncoder()

# For Matrix
df_train['ctag'] = le.fit_transform(df_train['common_tag'])
  
df_test['ctag'] = le.fit_transform(df_test['common_tag'])
Y_test = []
Y_test = df_test['ctag'].tolist()
Y_train = []
Y_train = df_train['ctag'].tolist()

X_train = dtm1
X_test = dtm2

classifier = OneVsOneClassifier(SVC(probability = True, kernel = 'poly'))

classifier.fit(X_train, Y_train)

predicted = classifier.predict(X_test)


print "Accuracy Score SVM: ",accuracy_score(Y_test, predicted)
#print "Score:",score(X_test, Y_test)
print "Precision_score", precision_score(Y_test, predicted)