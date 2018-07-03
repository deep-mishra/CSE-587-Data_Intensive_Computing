#!/usr/bin/python3.4

"""mapper.py"""

import sys
import re
import nltk
from nltk.corpus import stopwords

#Top 10 words found in NYTimes Data
top_words = ['gun', 'school', 'trump', 'people', 'shooting', 'police', 'year', 'president', 'high', 'students']	

#The context for the co ocurrance in nytimes data is article. Each article is present in separate file and each file has single line.
for article in sys.stdin:
	#Clean data
	article = article.strip()
	article = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", " ", article)
	article = re.sub("\“|\”|\‘|\’|\"|,|'", " ", article)
	article = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", article)
	article = article.lower()
	article = re.sub(" mr | said | new | still | one | would | also | two | u | like "," ", article)	
	if article == '':
		continue
	words = article.split()

	#Remove stop words
	list_of_words = list()
	for word in words:
		if(word not in stopwords.words('english')):
			list_of_words.append(word)
	
	for index, word1 in enumerate(list_of_words):
		for word2 in list_of_words[(index+1):]:
			if(word2 == word1): continue
			pair = word1+","+word2
			if(word1 in top_words or word2 in top_words):
				print('%s\t%s' % (pair, 1))
