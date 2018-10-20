import tweepy
from pprint import pprint
import user_credentials
import sys

class user:
    def __init__(self,twtHandler=None):
        self.twtHandler = twtHandler
        
    def genCredentials(self):
        #This function fetches twitter API keys in from user_credentials
        #Please update user_credentials.py with your twitter API keys
        
        self.consumer_key        = user_credentials.consumer_key        
        self.consumer_secret     = user_credentials.consumer_secret     
        self.access_token        = user_credentials.access_token        
        self.access_token_secret = user_credentials.access_token_secret

    def genHandler(self):
        self.genCredentials()

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
     
    def getTimeLine(self,twtHandler=None):
        #print("Getting time line of : " , self.twtHandler)
        self.genHandler()
        self.ownTimeline = self.api.home_timeline(count='20')
        for sno, tweet in enumerate(self.ownTimeline):
            #twText = tweet.text.encode('utf-8')
            #print(sno+1, " : ", twText.decode() , "\n")

            ##Following code is to handle charasters outside basic multilingual plane(BMP) such as emojis
            ##This code is required if the script is executed in IDLE/Tk
            
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            twText = (tweet.text.translate(non_bmp_map))
            print(sno+1, " : ", twText , "\n")          
        
def main():
    #print("Creating an instance of the user class : ")
    user1 = user()
    user1.getTimeLine()
    input()


if __name__ == "__main__" :
    main()
    
