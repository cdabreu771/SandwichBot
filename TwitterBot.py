'''
Created on Nov 14, 2019

@author: Camille
'''

import tweepy
import markovify
import time
from PIL import Image, ImageFont, ImageDraw

class TwitterAPI():
    def __init__(self):
            
            consumer_key = '3NS3A2hmvYmtokJf7qgBlu1wa'
            consumer_secret = 'Ywxwe11hBBLwIS0JhNbJqXTxSfnXUoCeMlpvFjVCuhFXHvR73x'
            access_token = '1195079549307899904-g4IzyUcpbmGo8jLNPjAwNhode15lpF'
            access_token_secret = '7cqYSd5uNM3K4CzQAQtoM9kfcHsWhli1yuJ2i8xx6I54R'
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth)
            
            #tweet = "Hello from Spain!"
            #image_path ="/Users/Camille/Documents/Photos/20190909_110215_Thomas Jacob Bedwin__Engagement Corey and Camille_0121.JPG" 
            
            #status = self.api.update_with_media(image_path, tweet)
            #self.api.update_status(status = tweet) 
            
            
            font = ImageFont.truetype("/Users/Camille/Library/Fonts/MontserratAlternates-Medium.otf", 25)
            img = Image.new("RGBA", (200,200), (120,20,20))
            draw = ImageDraw.Draw(img)
            draw.text((0,0), "This is a test", (255,255,0), font=font)
            draw = ImageDraw.Draw(img)
            img.save("a_test.png")
            
            status = self.api.update_with_media("a_test.png")
            
            print("sleeping")
            time.sleep(900) #Tweet every 15 minutes
            

tweet = TwitterAPI()

"""
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
    
    
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_key", "access_secret")

api = tweepy.API(auth)
    
# Create a tweet
api.update_status("Hello Tweepy")
"""
    
"""

    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)
"""

    
"""
   
   twitter_api = Twitter_Api(consumer_key, consumer_secret, access_key, access_secret)
   
class Twitter_Api():   
   def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self._logger = logging.getLogger(__name__)
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_key = access_key
        self._access_secret = access_secret
        self._authorization = None
        if consumer_key is None:
            self.tweet = lambda x : self._logger.info("Test tweet: " + x)
            self._login = lambda x : self._logger.debug("Test Login completed.")
            
   def _login(self):
        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_key, self._access_secret)
        self._authorization = auth
        
    def tweet(self, tweet):
        if self._authorization is None:
            self._login()
            pass
        api = tweepy.API(self._authorization)
        stat = api.update_status(tweet)
        self._logger.info("Tweeted: " + tweet)
        self._logger.info(stat)
    
    def disconnect(self):
        self._authorization = None
"""