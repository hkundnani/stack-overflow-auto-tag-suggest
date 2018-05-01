# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
from sklearn import svm
import numpy as np
from itertools import islice
from sklearn.metrics import accuracy_score
from multiprocessing import Pool
from sklearn.model_selection import KFold
import pickle
from collections import OrderedDict
from operator import itemgetter

split_val = 850

train_df = pd.read_csv("processed_data_train_new.csv")
test_df = pd.read_csv("processed_data_test_new.csv")
train_df = train_df.drop(["post_type_id", "view_count", "answer_count"], axis =1)
test_df = test_df.drop(["post_type_id", "view_count", "answer_count"], axis =1)
train_df.columns = ['#id#', '#body#', '#tags#', '#title#', '#common_tag#']
test_df.columns = ['#id#', '#body#', '#tags#', '#title#', '#common_tag#']

# Initializing vectorizer to convert text documents into matrix of token counts
vectorizer = CountVectorizer(input = 'content', stop_words = 'english', strip_accents='ascii')

train_dtm = vectorizer.fit_transform(train_df['#body#'])
test_dtm = vectorizer.transform(test_df['#body#'])

# Initializing label encoder to convert the string labels into value between 0 to n-1 classes
label_encode = preprocessing.LabelEncoder()

train_label_split = np.split(train_df['#common_tag#'], split_val)
test_label_split = np.split(test_df['#common_tag#'], 17000)

count = 0
for index in range(split_val):
		train_dtm_split = train_dtm[count:count+2250, :]
		train_label = label_encode.fit_transform(train_label_split[index])
		
		# Initializing the SVM classifier
		classifier = svm.SVC(kernel='rbf', probability=True, random_state=42)
		print ('start')

		# Training the model individually for each tag and saving it to a file 
		classifier.fit(train_dtm_split, train_label)
		filename = 'models_new/model' + str(index) + '.sav'
		pickle.dump(classifier, open(filename, 'wb'))
		print ('finish')
		count += 2250

for index in range(17000):
   listOfTags = {}
   actualTag = []
   question = []
   print ('Question {}'.format(index))
   test_dtm_split = test_dtm[index:index+1, :]
   test_label = label_encode.fit_transform(test_label_split[index])

   # Reading each saved model file and predicting the probability of that tag for each test question
   for count in range(split_val):
       model = pickle.load(open('models_new/model' + str(count) + '.sav', 'rb'))
       listOfTags['model'+str(count+1)] = model.predict_proba(test_dtm_split).ravel()[0]
       # print (label_encode.inverse_transform(test_label))
       actualTag.append(label_encode.inverse_transform(test_label).item())
       question.append('Question' + str(index))
       # print (actualTag)
   prob_list = list(OrderedDict(sorted(listOfTags.items(), key=itemgetter(1), reverse=True)).items())
   final_df = pd.DataFrame.from_records(prob_list[0:10])
   final_df['actual'] = actualTag[0:10]
   final_df['question'] = question[0:10]
   if index == 0:
       header = True
   else:
       header = False
   # Storing the generates probability to the file
   final_df.to_csv('result_positive.csv', encoding='UTF-8', mode='a', header=header, index=False)