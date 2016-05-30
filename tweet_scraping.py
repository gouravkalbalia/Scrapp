#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

#Variables that contains the user credentials to access Twitter API 
access_token = "2325877399-NYyFeXjaJmTXMAeDH0qp9LsV9KWYb6uiJrePNrg"
access_token_secret = "MTabv0xxyzlmwPAvfWIBKilYcL1FSOI20V0WlTuyHXlMe"
consumer_key = "vcd3NiBISjaxpDW7QXGH7380e"
consumer_secret = "MdLsBNRWvYeya6HGRZOoSwaIZA8Gh1gR7qR7Iww5BFD9UlqlMq"

class listener(StreamListener):

	def on_data(self, data):
		try:
			#print data
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			#saveThis = str(time.time())+'::'+tweet
			saveThis = tweet
			saveFile = open('twitDB3.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException,e:
			print 'failed ondata,',str(e)
			time.sleep(5)

	def on_error(self, status):
		print status

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["python"])