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


# create and post the tweet; returns days remaining to stop looping after the premiere arrives
def postTweet(api):

    # calculate the days remaining
    premiere = date(2022, 4, 22)
    today = date.today()

    diff = premiere - today

    days_left = diff.days

    # choose a tweet format based on how many days remain
    if days_left == 0:
        tweet = "Today is the premiere of TUWOMT!!"
    elif days_left == 1:
        tweet = "There is " + str(days_left) + " day until TUWOMT!"
    elif days_left <= 100:
        tweet = "There are " + str(days_left) + " days until TUWOMT!"
    else:
        tweet = "There are " + str(days_left) + " days until TUWOMT."

    # post the tweet
    api.update_status(tweet)

    return days_left


def main():

    # authenticate and access Twitter API
    api = authenticate()

    # post the tweet
    postTweet(api)

    # confirmation
    print("Done, check for tweet")


if __name__ == '__main__':
    main()

