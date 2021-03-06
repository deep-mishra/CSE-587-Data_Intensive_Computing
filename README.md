# CSE-587-Data_Intensive_Computing

##

## Project 1 - Analyse Twitter reaction vs CDC surveillance report on influenza activity in US States. [Repo..](project1-twitter-vs-cdc-influenza-analysis)
The project fetches the tweets on influenza and plots the heat map to compare how twitter reacted on influenza affected States. The complete project is implemented in R with the help of twitteR and geocode API for collecting tweets.

[TwtsVsCdsAnalysis.R](project1-twitter-vs-cdc-influenza-analysis/TweetsVsCdsAnalysis.ipynb)

![HeatMap](project1-twitter-vs-cdc-influenza-analysis/pics/twt_vs_cdc.PNG)

##
##

## Project 2 - Sentiment Analysis on Gun Violence using Hadoop. [Repo..](project2-sentiment-analysis)
Performed Sentiment analysis of People on gun violence on Twitter data and compared that with NYTimes articles. **Hadoop** is used to perform the word count and co-occurance of top words in two sets of data. I have used d3 for word-could and python to implement mapper and reducer of Hadoop framework.

[TopWordComp.html](project2-sentiment-analysis/SentimentAnalysis/d3_wordcloud/topwords-wordcloud.html)

![Comparison1](project2-sentiment-analysis/SentimentAnalysis/images/comparison1.PNG)

[CooccurTopWordComp.html](project2-sentiment-analysis/SentimentAnalysis/d3_wordcloud/co-occur-wordcloud.html)

![Comparison2](project2-sentiment-analysis/SentimentAnalysis/images/comparison2.PNG)


##
##

## Project 3 - Document Classification using Spark Infrastructure. [Repo..](project3-document-classification)
News articles can be from different categories like sports, business, etc. This project uses **Spark infrastructure with machine learning** to predict the category of articles. The first step is to train our model using the training set, test it, and finally predict the unknow set of articles and evaluate the performance of trained model.

[ArticleCollection Python Code](project3-document-classification/arcticles-collection.ipynb)

[DocumentClassification Python Code](project3-document-classification/document-classification.ipynb)

**Prediction Result:**

Prediction using Random Forest Classification-
![RandomForestClassification](project3-document-classification/output/random_forest_classification.png)

Prediction using Logistic Regression Model
![LogisticRegression](project3-document-classification/output/logistic_regression.png)

