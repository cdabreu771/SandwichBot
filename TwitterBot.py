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


"""
This class handles the TwitterAPI and authenticates the twitter account.
"""
class TwitterAPI():
    def __init__(self):
            
        consumer_key = #removed for github privacy
        consumer_secret = #removed for github privacy
        access_token = #removed for github privacy
        access_token_secret = #removed for github privacy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        ####self.follow()
        self.retweet()
        
    # This method follows back any new followers   
    def follow(self):
        for follower in tweepy.Cursor(self.api.followers).items():    
            follower.follow() 
    
    # This method retweets 2 tweets that contain the word "sandwich"
    def retweet(self):
        search = "sandwich"
        numberOfTweets = 2

        for tweet in tweepy.Cursor(self.api.search, search).items(numberOfTweets):    
            try:        
                tweet.retweet()        
                print('Retweeted the tweet')

            except tweepy.TweepError as e:        
                print(e.reason)

            except StopIteration:        
                break   
"""
This function handles the Twitter Bot.
"""   
class Bot:
    # This method initializes the twitter API, as well as the thread that runs the bot. It reads
    # the .txt files and sorts items into arrays. It also creates an array of hashtags.
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
           
        self.vegetable_array = []
        with open('vegetable.txt') as f:
            for line in f:
                line = line.strip()
                self.vegetable_array.append(line)
               
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
        
     # This method generates the recipe string by choosing a random number of each item, and then randomly
     # selecting items from each array.   
    def get_tweet(self):
        tweet = ''
        
        # Randomly select number of each item for recipe
        seed()
        meatNum = randint(0,2)
        cheeseNum = randint(0,1)
        # If there is no meat, load up on vegetables.
        if meatNum == 0:
            vegNum = randint(1,3)
        else:
            vegNum = randint(1,2)
        toppingNum = randint(1,2)
        
        # Start forming the recipe string.
        # Meat
        if meatNum!=0:
            tweet = self.meat_array[randint(0,len(self.meat_array)-1)].capitalize()
        
            for i in range(meatNum - 2):
                tweet += ", " + self.meat_array[randint(0,len(self.meat_array)-1)]
        
            tweet += " with "
        
        # Cheese
        if cheeseNum!=0:
            tweet += self.cheese_array[randint(0,len(self.cheese_array)-1)] + " cheese, "
        
        # Vegetables    
        tweet += self.vegetable_array[randint(0,len(self.vegetable_array)-1)]
        for i in range(vegNum -1):
            tweet += ", " + self.vegetable_array[randint(0,len(self.vegetable_array)-1)]
        tweet += ", "
        
        # Toppings
        tweet += self.topping_array[randint(0,len(self.topping_array)-1)]
        for i in range(toppingNum -1):
            tweet += ", " + self.topping_array[randint(0,len(self.topping_array)-1)]
        
        # Bread
        tweet += " on " + self.bread_array[randint(0,len(self.bread_array)-1)] + "."
        
        # Wrap text so that it fits into the recipe card.
        wrapper = textwrap.TextWrapper(width=35) 
        string = wrapper.fill(text=tweet) 
        
        return string 
    
    # This method generates a name for each sandwich.
    def get_name(self):
        name = ''
        
        # Select a random adjective and noun.
        seed()
        name = "The " + self.adjective_array[randint(0,len(self.adjective_array)-1)].title()  + " " + self.noun_array[randint(0,len(self.noun_array)-1)].title()
        
        # Wrap text so that it fits into the recipe card.
        wrapper = textwrap.TextWrapper(width=35) 
        string = wrapper.fill(text=name) 
        
        return string
    
    # This method generates the hashtags.    
    def get_hashtags(self):
        hashtags = ''
        
        # Select a random number of hashtags.
        seed()
        hashtagNum = randint(2,4)
        
        # Create a string of hashtags.
        for i in range(hashtagNum):
            hashtags += self.hashtag_array[randint(0,len(self.hashtag_array)-1)] + " "
            
        return hashtags
    
    # This method is the thread that runs the bot. It will call the get_name, get_tweet, and get_hashtags
    # functions, as well as the get_image_tweet function. This method will also cause the bot to sleep for 
    # 60 seconds.
    def run(self):
        
        while True:
           
            name = self.get_name()
            tweet = self.get_tweet()
            hashtags = self.get_hashtags()
            self.get_image_tweet(tweet,name,hashtags)
            print("sleeping")
            time.sleep(self.sleep_timer) #Every 1 minute
        
    # This method creates the recipe image and posts it to Twitter.    
    def get_image_tweet(self,tweet,name,hashtags):
        
        # Create a root path for the bug images.
        root_image_path = "/Users/Camille/Documents/COEN296B/FinalProject/BugImages/"
        images_files = os.listdir(root_image_path)
        if '.DS_Store' in images_files:
            images_files.remove('.DS_Store')  
        
        # Open the background image and make more transparent.
        image = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/Images/blanket.png")
        image = image.copy()
        image.putalpha(90)
        draw = ImageDraw.Draw(image)
        
        # Open the picnic basket image and transpose onto the background image. 
        picnicBasket = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/picnic.png")
        newsize = (600,600)
        picnicBasket = picnicBasket.resize(newsize)
        image.paste(picnicBasket, (20,500), picnicBasket)
        draw = ImageDraw.Draw(image)
        
        # Open the ants image and transpose onto the background image.
        ants = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/antSandwich.png")
        newsize = (250,250)
        ants = ants.resize(newsize)
        image.paste(ants, (650,800), ants)
        draw = ImageDraw.Draw(image)
        
        # Select a random value of bugs.
        randnum=randint(2,3)
        
        # Select random bugs and transpose onto the background image in random locations.
        for i in range(randnum):
            randXloc=randint(900,1800)
            randYloc=randint(800,950)
            single_image = random.sample(images_files, 1)[0]
            littleBug = Image.open(root_image_path + single_image)
            newsize = (200,200)
            littleBug=littleBug.resize(newsize)
            image.paste(littleBug, (randXloc, randYloc), littleBug)
            draw = ImageDraw.Draw(image)
            
        # Select a font for the name.
        font = ImageFont.truetype("/Library/Fonts/Courier New Bold.ttf", 90)
    
        # Draw the name onto the recipe card.
        draw.text((10,10), name, (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
        
        # Select a font for the recipe.
        font = ImageFont.truetype("/System/Library/Fonts/Courier.dfont", 85)
        
        # Draw the recipe onto the recipe card.
        draw.text((20,175), tweet, (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
        
        # Save new image.
        image.save('transparentCopy.png')
        
        # Post image to Twitter.
        status = self.twitter_api.api.update_with_media("transparentCopy.png",hashtags)
        
        
            

twitter_api= TwitterAPI()
bot = Bot(twitter_api)
bot.run()



    

   
