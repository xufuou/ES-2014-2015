from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from boto.sqs.message import Message
import cPickle
import boto.sqs

consumer_key="96Kk7232Cz6niLZUGh8lyHkNr"
consumer_secret="neAvWx6LfFvz3HMqIz18NS15bNm1VF5ODimwfRSQxmFCpwQiEx"
access_token="802485133-qDGGvRTX8sCMCSEzmWws58zGhb181HyxDtBwQctI"
access_token_secret="j7QU8kltmziYPDDILtwqxutLIvFZxssAvPh1IrxxTJrHn"

import boto.sqs
conn=boto.sqs.connect_to_region("us-east-1")

q=conn.get_all_queues(prefix='arsh-queue')


class StdOutListener(StreamListener):
	def on_data(self,data):
		print data
		ms=cPickle.dumps(data)
		m=Message()
		m.set_body(msg)
		status=q[0].write(m)
		return True

if __name__ == '__main__':
	keywords=['India']
	I=StdOutListener
	auth=OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream=Stream(auth,I)
	stream.filter(track=keywords)