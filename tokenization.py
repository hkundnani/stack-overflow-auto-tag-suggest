
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize

stops = set(stopwords.words('english'))


def process(chunk):
    uri_re = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})|<p>|<\/p>|<pre>|<\/pre>|<code>|<\/code>|<a href=|<\/a>|[`~!@\$%^&*\(\)_-]|[\[\]\{\}]|[:;\"\']|[,?<>=]|[0-9]|[\\\/]"
    #for read in chunk:
    
    def rem_punct_url(x):
        x = x.lower()
        return re.sub(uri_re, "", x)
    def rem_stop_words(x):
        processed_words = [word for word in x.split() if word not in stops]
        return " ".join(processed_words)
    def tokenizer(x):
        source = unicode(x, 'utf-8')
        tokens = word_tokenize(source)
        return ','.join([token for token in tokens if token != '.'])
    def tag_process(x):
        # regex = r"<|>"
        # return re.sub(regex, " ", x)
        return x.replace('<', '')
           
    chunk["title"] = chunk["title"].map(rem_punct_url)
   
    chunk["title"] = chunk["title"].map(rem_stop_words)
   
    chunk["body"] = chunk["body"].map(rem_punct_url)
    chunk["body"] = chunk["body"].map(rem_stop_words)
    chunk["title"] = chunk["title"].map(tokenizer)
    chunk["body"] = chunk["body"].map(tokenizer)
    chunk["tags"] = chunk["tags"].map(tag_process)
    chunk["tags"] = chunk["tags"].map(lambda tag: ','.join(filter(None, unicode(tag).split('>'))))
    # print (chunk.head())
       # chunk["title"]=re.sub(uri_re, "", chunk["title"])
        #chunk["body"]=re.sub(uri_re, "", chunk["body"])
    #print(chunk.head())   
    
i = 0
chunksize = 100000
for chunk in pd.read_csv("stack-overflow.csv", chunksize=chunksize):
    process(chunk)
    # chunk.to_csv("processed_data.csv", encoding='utf-8', mode = 'a', index=False)
    print("Chunk number"+str(i))
    i=i+1
