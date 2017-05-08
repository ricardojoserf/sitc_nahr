import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import csv
from optparse import OptionParser
import config as config
import argparse


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-q', '--query', required=True, action='store', help='Query')
  parser.add_argument('-l', '--limit', required=True, action='store', help='Max. number of tweets')
  my_args = parser.parse_args()
  return my_args


def get_tweets(query, count, geocode):

    consumer_key=config.consumer_key
    consumer_secret=config.consumer_secret
    access_token=config.access_token
    access_token_secret=config.access_token_secret

    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        tweets = []

        try:
            counter = 0
            #for tweet in api.search(q = query,count = count,geocode=geocode):
            for tweet in tweepy.Cursor(api.search, q = query,geocode=geocode, count=int(count), lan="fr").items(int(count)):
                counter+=1
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['time'] = tweet.created_at
                parsed_tweet['rts'] = tweet.retweet_count
                if tweet.place is not None:
                    parsed_tweet['place'] = tweet.place.full_name
                else:
                    parsed_tweet['place'] = "NaN"
                parsed_tweet['user'] = tweet.user.name
                if tweet.coordinates is not None:
                    parsed_tweet['lon'] = str(tweet.coordinates['coordinates'][0] )
                    parsed_tweet['lat'] = str(tweet.coordinates['coordinates'][1] )
                else:
                    parsed_tweet['lon'] = geocode[:geocode.index(",")]
                    parsed_tweet['lat'] = geocode[(geocode.index(",")+1):][:geocode[(geocode.index(",")+1):].index(",")]

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            print("Hemos conseguido "+str(counter)+" tweets")
            return tweets

        except ValueError:
            print("Error")

    except ValueError:
        print("Error")

def busqueda(query, count, geocode,csvname):
    print("Topic:        {}".format(query))
    print("Coordinates:  {}".format(geocode))
    tweets = get_tweets(query = query, count = count, geocode = geocode)
    csvFile = open(csvname, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["time","text","user","rts","place","lon","lat"])
    for tweet in tweets:
        try:
            csvWriter.writerow([tweet.get("time"),
                                tweet.get("text").encode("utf-8"),
                                tweet.get("user").encode("utf-8"),
                                tweet.get("rts"),
                                tweet.get("place"),
                                tweet.get("lon"),
                                tweet.get("lat")
                                ])
        except:
            pass
    print(csvname+" generated. \n\n")


def main():
    args = get_args()
    n_km="100"
    coords =    [
                ["Nouvelle-Aquitain","45.7087,0.6269,"+n_km+"km"],
                ["Occitanie","43.892,3.28,"+n_km+"km"],
                ["Auvergne-Rhone-Alpes","45.447,4.385,"+n_km+"km"],
                ["Grand Est","48.699,6.187,"+n_km+"km"],
                ["Bourgogne-Franche-Comte","47.281,4.999,"+n_km+"km"],
                ["Centre-Val de Loire","47.751,1.675,"+n_km+"km"],
                ["Pays de la Loire","47.763,-0.329,"+n_km+"km"],
                ["Hauts-de-France","50.287,2.781,"+n_km+"km"],
                ["Provence-Alpes-Cote-dAzur","43.935,6.068,"+n_km+"km"],
                ["Normandy","48.879,0.171,"+n_km+"km"],
                ["Brittany","48.202,-2.932,"+n_km+"km"],
                ["Ile-de-France","48.849,2.637,"+n_km+"km"],
                ["Corsica","42.15,9.083333,"+n_km+"km"],
                ]
    for region in coords:
        busqueda(args.query,args.limit,region[1], ("regions/"+region[0].encode("utf-8")+".csv") )


if __name__ == "__main__":
    main()
