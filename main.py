#!/usr/bin/env python3
from flask import Flask
from flask import request
import tweepy
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

# undefined :: a
undefined = None

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#tw = tweepy.API(auth)
app = Flask(__name__)

@app.route('/imgs', methods=['GET', 'POST'])
def imgs():
    def post(req):
        print(req.headers['Content-Type'])
        return req.data
    if request.method == 'POST': return post(request)
    else: return 'post image, return "pic.twitter.com/.*"'

def postImgRespondUrl():
    return undefined

if __name__ == "__main__" :
    exit(app.run(debug=True))

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
