#!/usr/bin/python3.4

"""mapper.py"""

import sys
import re
from nltk.corpus import stopwords
import nltk
#nltk.download("stopwords")

#Top 10 words found in twitter data
top_words = ['guncontrol','marchforourlives','nra','gun','gunviolence','vote','house','republicans','guns','rating']

#The context for the co occurrence is twitter data is tweet. Each tweet is there in separate line.
for tweet in sys.stdin:
   #Clean data
   tweet = tweet.strip()
   tweet = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", "", tweet)
   tweet = re.sub("\“|\”|\‘|\’|\"|,|'", " ", tweet)
   tweet = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", tweet)
   tweet = tweet.lower()
   tweet = re.sub(" [a-z] |aa+[a-z]* | ab | aba | abc | ac | acc | acq | az | ba | baa* | ca | czq | czt | da | daca  | ec | ed | rt | co ", " ", tweet)
   tweet = re.sub(" amp | nj | th | ar | get | pi | marc | someon | talking | speaking | ever | done | less ", " ", tweet)
   tweet = tweet.strip()
   if(tweet == ''):
      continue
   words = tweet.split()
   temp = []
   #Remove stop words
   for word in words:
      if word not in stopwords.words('english'):
         temp.append(word)
   words = list(filter(None, temp))

   #Emit co-occurance pairs if any word in the pair is part of top_words
   for i in range(len(words)):
      for j  in range(i+1, len(words)):
         if words[i] == words[j]: continue
         if words[i] in top_words or words[j] in top_words:
            print ('%s\t%s' % (words[i]+','+words[j], 1))

