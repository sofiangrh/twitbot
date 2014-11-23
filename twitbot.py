# Twitter Auto Favorite Bot
# Coded by Zea
# www.zeaja.com

from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = '177011871-6brzQmEHrvIprSoMdVzbVczLQlWWkujWSPDsT2XO'  # Isikan dengan auth token dari apps.twitter
OAUTH_SECRET = 'Rsji8LyGqqIU3jpXmSkOlXwZ9X0KVsaq6JHnMJGpxeaI0'    # Isikan dengan auth secret dari apps.twitter
CONSUMER_KEY = 'DEzvNTxrijiAlZxxFs5ObTuWt'                           # Isikan dengan consumer key dari apps.twitter
CONSUMER_SECRET = 'RXTh2XyLui2IZUBbTte3daG6Gkdr2aLPWks71XT4foZQv3Bm01'  # Isikan dengan consumer secret dari apps.twitter

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

def fav_tweet(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: %s" % (result['text'])
        return result
    # Jika kamu sudah mem-favoritkan sebuat twit
    # Error ini akan muncul
    except TwitterHTTPError as e:
        print "Error: ", e
        return None

def auto_fav(q, count=100):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print a
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
    print "Kamu memfavoritkan total %i dari %i tweets" % (success,
          len(result['statuses']))
