#!/usr/bin/env python3
from flask import Flask, Response, request
from flask.ext.cors import CORS
from mimetypes import guess_all_extensions
from io import BytesIO
import urllib.request

# undefined :: a
undefined = None

app = Flask(__name__)
CORS(app)

@app.route('/imgs', methods=['GET', 'POST'])
def imgs():
    def post(req):
        mime = req.headers['Content-type']
        candidateext = guess_all_extensions(mime)
        ext = candidateext[0] if len(candidateext) > 0 else ""
        filename = 'file' + ext
        fileobj = BytesIO(req.data)
        return postImgRespondUrl(filename, fileobj)
    if request.method == 'POST': return post(request)
    else: return 'post image, return "pic.twitter.com/.*"'

@app.route('/thumbnail', methods=['GET'])
def thumbnail():
    def get(req):
        r = urllib.request
        ep = 'http://capture.heartrails.com/332x166?'
        tmp = r.urlopen(r.Request(ep + list(req.args.keys())[0]))
        return Response(tmp.read(), mimetype=tmp.getheader('Content-type'))
    if request.method == 'GET': return get(request)

def postImgRespondUrl(filename, fileobj):
    import tweepy
    from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    tw = tweepy.API(auth)
    tweet = tw.update_with_media(filename, file=fileobj)
    #return tweet.text
    return tweet.extended_entities['media'][0]['display_url']

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
