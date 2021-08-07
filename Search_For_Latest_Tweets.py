import tweepy
import re
import csv
import pandas as pd

consumer_key = 'WANElrUycPRNtPh9ssenTmhm8'
consumer_secret = 'kHXXtKmDEyFKlct6IAVENkcCkgo8AqhFHOkbnF3XmB2tqelPGQ'
access_token = '1268162697306296320-j5cuIjT8D3xhfvZfpEoL68ry7cl9wp'
access_token_secret = 'Y7IhnkvMzGHVYWCx4hZoLd1cXQ4HffmyE0XCDBdffqerg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#waste OR #Wastemanagement OR #Pune OR #garbage OR #kachra OR #recycle",
                           lang="en",
                           since="2020-08-20").items():
    cord=""
    try:
        if( re.search( r'Pune', tweet.user.location, re.M|re.I)):
        # if(True):
            
            print("********************************")
            print (tweet.created_at)
            print("Tweet Information")
            print("================================")
            print("Text: ", tweet.text.encode("utf-8"))
            print()

            try:
                # print("Place: ", tweet.place.name)
                cord="["+str(tweet.place.bounding_box.coordinates[0][0][1])+","+str(tweet.place.bounding_box.coordinates[0][0][0])+"]"
                # place=tweet.place.name
            except AttributeError:
                # print("Place: ", tweet.place)
                # place=tweet.place
                cord=tweet.coordinates
                
            
            try:
                if cord is None:
                    from geopy.geocoders import Nominatim
                    geolocator = Nominatim(user_agent="ABC")
                    location = geolocator.geocode(tweet.user.location)
                    cord="["+str(location.latitude)+","+str(location.longitude)+"]"
            except AttributeError:
                pass

            print("Coordinates",cord)

            print()

            print("User Information")
            print(tweet.user.screen_name)
            
            print("================================")
            print("Location: ", tweet.user.location)
            print("********************************")
            
            csvWriter.writerow([tweet.created_at,tweet.user.screen_name,tweet.user.location,cord,tweet.text.encode("utf-8")])

    except UnicodeEncodeError as identifier:
        pass
    
