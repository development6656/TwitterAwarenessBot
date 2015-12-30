import tweepy, time, sys
from twitterkeys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, 
	wait_on_rate_limit_notify=True)

twitterIDs = ["AmericanCancer", "UNICEF" ,"RedCross", "CR_UK", "amnesty", "SU2C", "theNCI", "CDC_Cancer"]

def main():
	for twitterID in twitterIDs:
		retweetStatuses(twitterID)

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			time.sleep(15*60)

def retweetStatuses(id):
	for status in limit_handled(tweepy.Cursor(api.user_timeline, id=id).items(10)):
		try:
			#print(status.text) debugging purposes only
			api.retweet(status.id)
		except tweepy.TweepError as e:
			print(e)

if __name__ =="__main__":
	main()

