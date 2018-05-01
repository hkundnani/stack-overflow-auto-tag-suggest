### Suggesting tags automatically for Stack Overflow questions
This project is an implemention of the paper "A Discriminative Model Approach for Suggesting Tags Automatically for Stack Overflow Questions"

All the code files used in this project are mentioned below with a short description about the code implemented inside that particular file.
##### **Note:
This repository doesn't contain data files as they were too large and couldn't be commited due to less space in free github account. Two .csv (most_common_tags.csv, test_dataset.csv) files present in repository were not too large in size. Any file not mentioned in the readme file is not used in the overall development of project or may have been commited initialy and later not used. 

##### accuracy.py
Code to calculate the accuracy for 

##### connection.py
Code to insert the postgresql dump inside the postgresql database and to get only the questions with few parameters (id, body, title, tags, view_count, answer_count) by querying the databse.

##### data_model.py
Code to get the count of number of questions for each number of tags along with the percentage. Also, draw the graph for average views per question for the number of tags.

##### dtm.py
Code to read train and test data and generate the term frequency count of tokens present in column 'body'. Train the SVM model on the train data for each tag and store the models in files. Test the model against test data and generate a .csv file which includes probability of a top 10 models for each question.

##### generate_train_data.py
Code to generate train dataset based on the discriminative model for each of the most popular tag using the approach mentioned in the paper with 60 positive questions (questions containing the tag) and 1500 negative questions (questions not containing the tag).

##### generate_test_data.py
Code to generate test dataset based on the discriminative model for each of the most popular tag using the approach mentioned in the paper with 10 positive questions (questions containing the tag) and 10 negative questions (questions not containing the tag) and questions not in the train dataset.

##### most_popular_tags.py
Code to create a list of tags and their frequency and take 850 most frequent tags and store them in a .csv file

##### onevsone.py
Code to implement a model using OnevsOne classification approach 

##### tokenize_data.py
Code to remove punctuations, URLs, stop words, and other unwanted characters from column 'body'
