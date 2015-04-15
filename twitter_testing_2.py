from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
consumer_key="96Kk7232Cz6niLZUGh8lyHkNr"
consumer_secret="neAvWx6LfFvz3HMqIz18NS15bNm1VF5ODimwfRSQxmFCpwQiEx"
access_token="802485133-qDGGvRTX8sCMCSEzmWws58zGhb181HyxDtBwQctI"
access_token_secret="j7QU8kltmziYPDDILtwqxutLIvFZxssAvPh1IrxxTJrHn"

#This is a basic listener that just prints received tweets to stdout

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

#THis handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: Lottery, National Lottery'
    stream.filter(track=['Lottery', 'National Lottery'])