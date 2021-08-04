import os
import tweepy
from dotenv import load_dotenv
from datetime import date
from time import sleep

# authenticate with tweepy and return the api object
def authenticate():

    load_dotenv()
    # getting auth keys from env
    consumer_key = os.getenv("consumer_key")
    consumer_secret = os.getenv("consumer_secret")
    access_token = os.getenv("access_token_cd")
    access_token_secret = os.getenv("access_token_secret_cd")

    # authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


# create and post the tweet 
def postTweet(api):

    # calculate the days remaining
    premiere = date(2022, 4, 22)
    today = date.today()

    diff = premiere - today

    days_left = diff.days

    # choose a tweet format based on how many days remain
    if days_left == 0:
        tweet = "Today is the premiere of TUWOMT!!"
    elif days_left <= 100:
        tweet = "There are " + str(days_left) + " days until TUWOMT!"
    else:
        tweet = "There are " + str(days_left) + " days until TUWOMT."

    # post the tweet
    api.update_status(tweet)

    return days_left


def main():

    api = authenticate()

    ## create some sort of stopping mechanism here, combined with heroku scheduler?
    ## LOOK UP SOME VIDEO TUTORIALS ABOUT HEROKU SCHEDULER 

    postTweet(api)


    print("Done, check for tweet")


if __name__ == '__main__':
    main()

