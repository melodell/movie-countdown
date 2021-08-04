# this file was used to perform PIN-Based OAuth verification and tests,
# but nothing is dependent on this file.
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# getting auth keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token_cd")
access_token_secret = os.getenv("access_token_secret_cd")
callback_url = os.getenv("callback_url")

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)

    ## getting outside auth

    #redirect_url = auth.get_authorization_url()
    #print(redirect_url)

    #pin = input("Paste PIN: ")

    #auth.get_access_token(pin)
    #print(auth.access_token, auth.access_token_secret)

    ##

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# testing authentication and writing
api.update_status("Test")
print("Check for tweet")




