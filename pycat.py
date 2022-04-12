import tweepy
from time import sleep
from random import randint
consumer_key = 'ROtFCqWU76JHAo95DDvZMUSAJ'
consumer_secret = '0HM1SBdSw4E3cvVqVaPq2OJWxOvnRYaMhSUEj9QNpzwwXSjKZn'

key = '764027649874210816-XS6kDL8NuPJqjjtAkJIWdYU6OYYHUCV'
secret = 'K59rz3wuh2TVNdESBzlLfVECGP8no9jPwvPbRZAYJkrqG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
tweet = str(input("enter message: "))
n = int(input("How many time want to tweet? = "))
c = 0
for i in range (n):
    api = tweepy.API(auth)
    try:
        api.update_status(tweet + " " + str(i+5/2+1.07 + randint(10,1000)))
        print("send {}".format(i+1))
        sleep(1)
        c += 1
    except:
        pass
print("succesfull send = {}".format(c))
