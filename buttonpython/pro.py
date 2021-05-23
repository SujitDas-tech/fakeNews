from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn import linear_model
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
from wordcloud import WordCloud, STOPWORDS 


import numpy as np # linear algebra
import pandas as pd #data processing

import os
import re
import nltk
stop_words = stopwords.words('english')

total=sys.argv[1]+sys.argv[2]+sys.argv[3]
lemmatizer=WordNetLemmatizer()

filter_sentence = ''
    
sentence = total
sentence = re.sub(r'[^\w\s]','',sentence) #cleaning
    
words = nltk.word_tokenize(sentence) #tokenization
    
words = [w for w in words if not w in stop_words]  #stopwords removal
    
for word in words:
    filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()

filename = r'C:\Users\sujit\Desktop\model\django\buttonpython\NLP.sav'
loaded_model = joblib.load(filename)
if((loaded_model.predict([filter_sentence]))==0):
	output="It is a Real News"
else:
	output="It is a Fake News"
print(output)
