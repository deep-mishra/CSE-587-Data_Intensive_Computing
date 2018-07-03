#!/usr/bin/python3.4

"""mapper.py"""

import sys
import re
import nltk
from nltk.corpus import stopwords

for line in sys.stdin:
   #Clean data
   line = line.strip()
   line = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", " ", line)
   line = re.sub("\“|\”|\‘|\’|\"|,|'", " ", line)
   line = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", line)
   line = line.lower()
   line = re.sub(" mr | said | new | still | one | would | also | two | u | like "," ", line)	
   
   if(line == ''):
      continue
   
   #Emit count for each word
   words = line.split()
   for word in words:
      if(word not in stopwords.words('english')):
         print('%s\t%s' % (word, 1))
