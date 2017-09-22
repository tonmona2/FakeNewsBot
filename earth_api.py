from flask import Flask, render_template
import tweepy, time, sys
from time import sleep
from random import randint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
from flask import jsonify
from flask import request
import os
import io

app = Flask(__name__, template_folder="mytemplate")
list_names = ["@fakeNewsBots"]
# Authentication
try:
	t_consumerkey='TW_CONSUMERKEY'
	t_secretkey='TW_SECRETKEY'
	access_tokenkey='TW_ACCESS_TOKENKEY'
	access_tokensecret='TW_TOKENSECRET'
except KeyError: 
	print("You need to set the environment variables: TW_CONSUMERKEY, TW_SECRETKEY, TW_ACCESS_TOKENKEY, TW_TOKENSECRET")
	sys.exit(1)
# list of name to handle duplicates


#open file to read hashtags
with open('hashtags.txt') as f:
   for line in f:
        auth = tweepy.OAuthHandler(t_consumerkey, t_secretkey)
        auth.set_access_token(access_tokenkey, access_tokensecret)

        api = tweepy.API(auth)

        search_text = line
        search_number = 2
        search_result = api.search(search_text, rpp=search_number)

        # with io.open('output_tweets.txt', 'a', encoding='utf8') as w:
        #     for tweet in search_result:
        #         w.write('Username:  ' + tweet.author.screen_name + '\n')
        #         w.write("Tweet:  " + tweet.text + "\n")
        # w.close()
#tweet in the usernames
        for tweet in search_result:
            handle = "@" + tweet.user.screen_name
            print(handle)
            if handle not in list_names:
                m = handle + " " + "hola! Soy un bot verificando info del sismo. Me puedes confirmar si estos recursos aun se requieren? Grax! #19SRecursos"
                s = api.update_status(m)
                nap = randint(1, 60)
                time.sleep(nap)
                list_names.append(handle)


f.close()
if(__name__) == '__main__':
    app.run(debug=True)