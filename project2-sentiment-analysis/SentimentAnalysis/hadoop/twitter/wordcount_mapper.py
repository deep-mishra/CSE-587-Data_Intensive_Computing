#!/usr/bin/python3.4

"""mapper.py"""

import sys
import re
from nltk.corpus import stopwords
import nltk

#May require to download stopwords when this is ran first time
#nltk.download("stopwords")

for line in sys.stdin:
   line = line.strip()
   line = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", "", line)
   line = re.sub("\“|\”|\‘|\’|\"|,|'", " ", line)
   line = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", line)
   line = line.lower()
   line = re.sub(" [a-z] |aa+[a-z]* | ab | aba | abc | ac | acc | acq | az | ba | baa* | ca | czq | czt | da | daca  | ec | ed | rt | co ", " ", line)
   line = re.sub(" amp | get | pi | marc | someon | talking | speaking | ever | done | less ", " ", line)
   line = line.strip()
   if(line == ''):
      continue
   words = line.split()

   #filtered_words = [word for word in words if word not in stopwords.words('english')]
   for word in words:
      if(word not in stopwords.words('english')):
         print('%s\t%s' % (word, 1))


