#Analysis of Tweets vs CDS Surveillance on Influenza
#@author: Deep Narayan Mishra

############################################################################################################
## CODE TO DOWNLOAD THE TWEETS AND QUERY USER LOCATION, THEN RETRIEVE THEIR LONG, LAT, AND REGION (STATE) ##
################## This might not give any data if query over limit has reached ############################


library(twitteR)
library(ggplot2)

#Uncomment below 2 line for METHOD 2 (alternate way of getting lon, lat and state)
#library(googleway)
#googleway_key <- "AIzaSyBzqd4G6K6yUrJ7zHXRVrRjplk-0B32K4o"

#TWITTER OAUTH..
api_key <- API_KEY
api_secret <- API_SECRET
access_token <- ACCESS_TOKEN
access_token_secret <- ACCESS_TOKEN_SECRET
setup_twitter_oauth(api_key, api_secret, access_token, access_token_secret)


#I placed this condition later to get an approximate US tweets
us_geocode <- "40.482405,-97.413745,2280mi"

#GET TWEETS..
tweets <- searchTwitter('#fluseason', n=10, since="2018-03-06", until = "2018-03-09", lang="en", geocode = us_geocode)
#tweets <- searchTwitter('#flu', n=2, since="2018-03-06", until = "2018-03-09", lang="en", geocode = us_geocode)
#tweets <- searchTwitter('#influenza', n=2, since="2018-03-06", until = "2018-03-09", lang="en", geocode = us_geocode)
#tweets <- searchTwitter('#flushot', n=2, since="2018-03-06", until = "2018-03-09", lang="en", geocode = us_geocode)


#PROCESS ONLY IF TWEETS ARE FOUND
if(length(tweets) != 0) {
  
  #CONVERT TO A DATAFRAME
  tweets.df <- twListToDF(tweets)
  cat("\nNew tweets count ", nrow(tweets.df))
    
  #LOAD PREVIOUS LOADED DATA..
  prev_loaded_data <- read.csv("twt_data/FluTweetsData.csv")
  cat("\nExisting record size ", nrow(prev_loaded_data))

  #GET USER LOCATION
  twitter_users <- lookupUsers(users = tweets.df$screenName, includeNA = TRUE)
  twitter_users.df <- twListToDF(twitter_users)
  #map user location
  tweets.df$location <- twitter_users.df$location[match(tweets.df$screenName, twitter_users.df$screenName)]
  tweets.df <- tweets.df[!(is.na(tweets.df$location) | (tweets.df$location == "")),]
  #create us state column
  tweets.df$us_states <- NA
  
  
  #GET LON LAT and STATE USING GEOCODE 
  for(i in 1:nrow(tweets.df)) {
    
    tweet <- tweets.df[i,]
    add <- toString(tweet$location)
    
    # Get long, lat and state of the tweet
    # METHOD 1
    tryCatch({ 
      # consume any error while calling the geocode and move on to next record
      cat("\ncalling geocode for record ", i, add)
      result <- geocode(add, output = "more", source = "google")
      tweets.df$longitude[i] <- result$lon        #longitude of the add
      tweets.df$latitude[i] <- result$lat         #latitude of the add
      
      #Placed this code later, after identifying can't plot graph without state name
      # for the older data executed my other code to call revgeocode and get this value
      if(result$country == "United States") {
        tweets.df$us_states <- as.character(result$administrative_area_level_1)        #state of the add
      }
    }, error=function(e){ print ("error while calling geocode..")})
    
    
    
    
    ## METHOD 2
    ## Alternative method to call and get lon, lat if the previous one doesn't work
    ## Comment out first method before uncommenting this

    #tryCatch({ 
    #  cat("\ncalling geocode for record ", i, add)
    #  result1 <- google_geocode(add, key = googleway_key) #get long and lat
    #  if(result1$status == "OK") {
    ##    #get coordinates
    #    coords <- geocode_coordinates(result1)
    #    tweets.df$longitude[i] <- coords$lng
    #    tweets.df$latitude[i] <- coords$lat
    #    
    #    #Not as good as geocode - it doesn't give you exact state name ( for that have to use revgeocode code)
    #    # so avoid using this method to get address
    #  }
    #}, error=function(e){ print ("error while calling googleway geocode")})

  }
  
  #APPEND THE NEW DATA TO OLD DATA
  #Copying data to keep to temp to analyse
  write.csv(tweets.df, "twt_data/temp.csv", row.names = F)
  newdata <- read.csv("twt_data/temp.csv")
  cat("\nNew tweets with location ", nrow(newdata))
  #Append the old and new data
  complete_data <- rbind(prev_loaded_data, newdata)
  cat("\nTotal tweets ", nrow(complete_data))
  #Write to CSV
  if(length(prev_loaded_data) != 0) {
    #This condition is not needed. Just putting it in case the code is executed without my 
    # file.. so that it doesn't create a new file.
    write.csv(complete_data, "twt_data/FluTweetsData.csv", row.names = F )
  }
  
} else {
  print ("No new tweets found.")
}



## TWEETS DATA STATISTICS ##

twt_stat <- read.csv("twt_data/FluTweetsData.csv")
cat("\t\tStatistics on Tweets data\n\n")
print ("TOTAL TWEETS WITH LOCATION")
nrow(twt_stat)

unq_twts <- twt_stat[!duplicated(twt_stat$text) | !duplicated(twt_stat$screenName), ]
print ("UNIQUE TWEETS WITH LOCATION")
nrow(unq_twts)

print ("UNIQUE TWEETS WITH US STATE LOCATION")
sum(!is.na(unq_twts$us_states))