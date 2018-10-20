import tweepy
from pprint import pprint
import user_credentials

class user:
    def __init__(self,twtHandler=None):
        self.twtHandler = twtHandler
        
    def genCredentials(self):
        #This function stores twitter API keys in memory
        #Please update this section with your twitter API keys
        self.consumer_key        = user_credentials.consumer_key        
        self.consumer_secret     = user_credentials.consumer_secret     
        self.access_token        = user_credentials.access_token        
        self.access_token_secret = user_credentials.access_token_secret

    def getTimeLine(self,twtHandler=None):
        print("Getting time line of : " , self.twtHandler)
        
def main():
    print("Creating an instance of the user class : ")
    user1 = user()
    user1.getTimeLine()



if __name__ == "__main__" :
    main()
