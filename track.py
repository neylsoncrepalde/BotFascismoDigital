# -*- coding: utf-8 -*-
"""
Track stream
Bot Fascismo Digital
@author: neylson.crepalde
"""
from twython import TwythonStreamer, Twython, TwythonError
import time
#from random import randint
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

post = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            lang = data['lang']
            message = "Lang: {} | @{}: {}".format(lang, username, tweet)
            if username == 'BotFascismo':
                # Não printa nem retweeta posts do próprio bot
                print('segue...')
            if username == 'Lionstours1':
                # outro bot
                print('segue...')
            else:
                print(message)
                # saida.write(str(data) + '\n')

                if 'RT @' not in message:
                    # Se não for RETWEET
                    if data['lang'] == "pt":
                        try:
                            post.retweet(id=data['id_str'])
                            print('Foi tweetado!')
                            print(time.ctime())
                        except TwythonError as e:
                            print(e)
                        except UnicodeEncodeError as e:
                            print(e)
                        #time.sleep(randint(10, 60))


stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Set id's to follow
NCrepalde = 3036885015
ids = [NCrepalde]

keys = ['#fascismodigital', '#fakenews', '#giars', '#giars2018']
stream.statuses.filter(track=keys, follow=ids)
