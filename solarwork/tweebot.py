import tweepy
import requests
import jobs
import numpy
from datetime import datetime, date, timedelta
from pytz import timezone
import pytz
'''
from config import *

consumer_key=CONSUMER_KEY
consumer_secret=CONSUMER_SECRET
access_token=ACCESS_TOKEN
access_token_secret=ACCESS_TOKEN_SECRET
seia_url=SEIA_URL
seia_dateformat = SEIA_DATEFORMAT
'''

#api.update_status(status=raw_input("Enter tweet: "))

def date_today():
    utc = pytz.utc
    pacific = timezone('US/Pacific')
    naive_today = datetime.today()
    utc_today = utc.localize(naive_today)
    today = utc_today.astimezone(pacific).date()
    return today


def get_todays_jobs(url):
    collection = requests.get(url).json()['results']['collection1']
    DATE_FORMAT = "%m/%d/%Y"
    todays_jobs = []
    #today's date in Pacific Timezone
    t = date_today()
    for x in collection:
        if datetime.strptime(x['seia_date']['text'], DATE_FORMAT).date() == t:
            try:
                todays_jobs.append([x['seia_title']['text'], x['seia_title']['href'], x['seia_location']['text'], x['seia_company']['text']])
            except:
                pass
    return todays_jobs

def authorize_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def form_tweet(job_list)
    for x in job_list:
    
