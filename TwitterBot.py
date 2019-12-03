'''
Created on Nov 14, 2019

@author: Camille
'''

import os
import random
import tweepy
import time
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import textwrap
from random import seed
from random import randint


class TwitterAPI():
    def __init__(self):
            
        consumer_key = '3NS3A2hmvYmtokJf7qgBlu1wa'
        consumer_secret = 'Ywxwe11hBBLwIS0JhNbJqXTxSfnXUoCeMlpvFjVCuhFXHvR73x'
        access_token = '1195079549307899904-g4IzyUcpbmGo8jLNPjAwNhode15lpF'
        access_token_secret = '7cqYSd5uNM3K4CzQAQtoM9kfcHsWhli1yuJ2i8xx6I54R'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        ####self.follow()
        ####self.retweet()
        
    #def tweet(self, tweet):
        #api = tweepy.API(self._authorization)
        
    def follow(self):
        for follower in tweepy.Cursor(self.api.followers).items():    
            follower.follow() 
    
    def retweet(self):
        search = "sandwich"
        numberOfTweets = 3

        for tweet in tweepy.Cursor(self.api.search, search).items(numberOfTweets):    
            try:        
                tweet.retweet()        
                print('Retweeted the tweet')

            except tweepy.TweepError as e:        
                print(e.reason)

            except StopIteration:        
                break   
    
class Bot:
    def __init__(self, twitter_api, tweets_per_hour = 60):
        
        self.twitter_api = twitter_api
        
        self.bread_array = []
        with open('bread.txt') as f:
            #Content_list is the list that contains the read lines.     
            for line in f:
                line = line.strip()
                self.bread_array.append(line)
           # print(bread_array)
        
        self.meat_array = []
        with open('meat.txt') as f:
            for line in f:
                line = line.strip()
                self.meat_array.append(line)
           # print(meat_array)
            
        self.cheese_array = []
        with open('cheese.txt') as f:
            for line in f:
                line = line.strip()
                self.cheese_array.append(line)
           # print(cheese_array)
            
        self.topping_array = []
        with open('topping.txt') as f:
            for line in f:
                line = line.strip()
                self.topping_array.append(line)
           # print(topping_array)
        
        self.adjective_array = []
        with open('adjective.txt') as f:
            for line in f:
                line = line.strip()
                self.adjective_array.append(line)
        
        self.noun_array = []
        with open('noun.txt') as f:
            for line in f:
                line = line.strip()
                self.noun_array.append(line)
                
        self.hashtag_array = ["#sandwich", "#sandwichtime", "#lunchtime", "#lunch", "#whatsforlunch", "#dinner", "#dinnertime", "#whatsfordinner", "#drool", "#meatsweats", "#food", "#foodporn", "#foodie", "#yummy", "#delicious", "#foodgasm", "#cheese", "#foodlover", "#foodblogger", "#sandwichlover", "#tasty"]
                
        self.sleep_timer = int(60*60/tweets_per_hour)
        
    def get_tweet(self):
        tweet = ''
        seed()
        meatInt=randint(0,len(self.meat_array)-1)
        cheeseInt = randint(0,len(self.cheese_array)-1)
        toppingInt = randint(0,len(self.topping_array)-1)
        breadInt = randint(0,len(self.bread_array)-1)
        
        meatNum = randint(0,2)
        cheeseNum = randint(0,1)
        toppingNum = randint(1,3)
        if meatNum!=0:
            tweet = self.meat_array[randint(0,len(self.meat_array)-1)].capitalize()
        
            for i in range(meatNum - 2):
                tweet += ", " + self.meat_array[randint(0,len(self.meat_array)-1)]
        
            tweet += " with "
            
        if cheeseNum!=0:
            tweet += self.cheese_array[randint(0,len(self.cheese_array)-1)] + " cheese, and "
        
        tweet += self.topping_array[randint(0,len(self.topping_array)-1)]
        for i in range(toppingNum -1):
            tweet += ", " + self.topping_array[randint(0,len(self.topping_array)-1)]
        
        
        tweet += " on " + self.bread_array[breadInt] + "."
       
        wrapper = textwrap.TextWrapper(width=45) 
        string = wrapper.fill(text=tweet) 
        return string 
    
    def get_name(self):
        name = ''
        seed()
        name = "The " + self.adjective_array[randint(0,len(self.adjective_array)-1)].capitalize()  + " " + self.noun_array[randint(0,len(self.noun_array)-1)].capitalize()
        wrapper = textwrap.TextWrapper(width=45) 
        string = wrapper.fill(text=name) 
        return string
        
    
    def get_hashtags(self):
        hashtags = ''
        seed()
        hashtagNum = randint(2,4)
        for i in range(hashtagNum):
            hashtags += self.hashtag_array[randint(0,len(self.hashtag_array)-1)] + " "
        return hashtags
    
    def run(self):
        
        while True:
           
            name = self.get_name()
            tweet = self.get_tweet()
            hashtags = self.get_hashtags()
            self.get_image_tweet(tweet,name,hashtags)
            print("sleeping")
            time.sleep(self.sleep_timer) #Every 10 minutes
        
        
    def get_image_tweet(self,tweet,name,hashtags):
    
        root_image_path = "/Users/Camille/Documents/COEN296B/FinalProject/Images/"
        images_files = os.listdir(root_image_path)
        single_image = random.sample(images_files, 1)[0]
        image = Image.open(root_image_path + single_image)
        """
        image = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/Images/image1.png")
        """
        image = image.copy()
        image.putalpha(128)
        font = ImageFont.truetype("/Library/Fonts/Arial Black.ttf", 130)
        # draw the image
        draw = ImageDraw.Draw(image)
        draw.text((10,10), name, (0,0,0), font=font,)
        draw = ImageDraw.Draw(image)
        
        font = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 110)
        draw.text((20,120), tweet, (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
        image.save('transparentCopy.png')
        status = self.twitter_api.api.update_with_media("transparentCopy.png",hashtags)
        
        
            

twitter_api= TwitterAPI()
bot = Bot(twitter_api)
bot.run()



    

   
