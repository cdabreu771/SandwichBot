'''
Created on Nov 14, 2019

@author: Camille
'''

import tweepy
import glob
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
        
    #def tweet(self, tweet):
        #api = tweepy.API(self._authorization)
        

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
                
        self.sleep_timer = int(60*60/tweets_per_hour)
        
    def get_tweet(self):
        tweet = ''
        seed(1)
        meatInt=randint(0,len(self.meat_array))
        cheeseInt = randint(0,len(self.cheese_array))
        toppingInt = randint(0,len(self.topping_array))
        breadInt = randint(0,len(self.bread_array))
        
        meatNum = randint(1,4)
        cheeseNum = randint(0,2)
        toppingNum = randint(1,5)
        
        tweet = self.meat_array[meatInt].capitalize() + " with " + self.cheese_array[cheeseInt] + " cheese and " + self.topping_array[toppingInt] + ", " + self.topping_array[toppingInt] + ", and " + self.topping_array[toppingInt] + " on " + self.bread_array[breadInt] + "."
        wrapper = textwrap.TextWrapper(width=50) 
        string = wrapper.fill(text=tweet) 
        return string 
    
    def get_name(self):
        name = ''
        seed(1)
        adjectiveInt = randint(0,len(self.adjective_array))
        nounInt = randint(0,len(self.noun_array))
        name = "The " + self.adjective_array[adjectiveInt].capitalize()  + " " + self.noun_array[nounInt].capitalize()
        return name
            
    def run(self):
        
        while True:
           
            name = self.get_name()
            tweet = self.get_tweet()
            self.get_image_tweet(tweet, name)
            #tweet = self.get_image_tweet(tweet)
            #self.twitter_api.tweet(tweet)
            print("sleeping")
            time.sleep(self.sleep_timer) #Every 10 minutes
        
        """
        # This is the font selected to write in
        font = ImageFont.truetype("/Users/Camille/Library/Fonts/MontserratAlternates-Medium.otf", 25)
        # This creates a red box image
        img = Image.new("RGBA", (200,200), (120,20,20))
        # This draws the red box
        draw = ImageDraw.Draw(img)
        # This creates the text
        draw.text((0,0), "This is a test", (255,255,0), font=font)
        # This draws the text on to the image
        draw = ImageDraw.Draw(img)
        # This saves the image as a .png
        img.save("a_test.png")
        """
    def get_image_tweet(self,tweet,name):
        #images = glob.glob("/Users/Camille/Documents/COEN296B/FinalProject/Images/")
        #image = images[random.randint(0,len(images))-1]
        image = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/Images/sandwich1.jpg")
        image = image.copy()
        image.putalpha(128)
        font = ImageFont.truetype("/Users/Camille/Library/Fonts/MontserratAlternates-Black.otf", 8)
        # draw the image
        draw = ImageDraw.Draw(image)
        draw.text((10,10), name, (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
        draw.text((10,30), tweet, (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
        
        #draw.text((10,30), "Use " + meat_array[4] + " with " + cheese_array[6] + "." (0,0,0), font = font)
       # draw = ImageDraw.Draw(image)
        image.save('transparentCopy.png')
        status = self.twitter_api.api.update_with_media("transparentCopy.png")
        
        # This posts the image
        #status = self.api.update_with_media("transparentCopy.png")
        #print (tweet)
        
        #print("sleeping")
        #time.sleep(15) #Tweet every 15 minutes
       # time.sleep(1)
        
        #post = randomimagetwitt()
        
        
        
            
        """
        # open image using image path
        #image = Image.open("/Users/Camille/Documents/COEN296B/FinalProject/Images/sandwich1.jpg")
        # make copy of image so that it is not replaced
        image = image.copy()
        # set the alpha (transparency level) of the image
        image.putalpha(128)
        # select font for the text
        font = ImageFont.truetype("/Users/Camille/Library/Fonts/MontserratAlternates-Black.otf", 14)
        # draw the image
        draw = ImageDraw.Draw(image)
        
   
        
        draw.text((10,10), "This is a test recipe.", (0,0,0), font=font)
        draw = ImageDraw.Draw(image)
            
        draw.text((10,30), "This is only a test.", (0,0,0), font = font)
        draw = ImageDraw.Draw(image)
            
        #draw.text((30,80), "This is a test recipe. It is only a test", (0, 0, 0), font = font)
        # draw the text onto the image
        
        # save the image
        image.save('transparentCopy.png')
        """
        
        
        
            

twitter_api= TwitterAPI()
bot = Bot(twitter_api)
bot.run()



    

   
