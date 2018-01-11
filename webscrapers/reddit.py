import praw
import datetime
from pprint import pprint

# Shoehorning in some code for saving to a model here.




class scraperReddit:
	""" Simple wrapper class for the praw library for the opinion tools """
	def __init__(self, subreddits=[], comments_enabled=False, limit=10):
		self.reddit = praw.Reddit(client_id='jIFEM8LpRrB6Jg',
					 client_secret='lvvM7fAWqaoZXY7Pt1jqqmOq36w',
					 redirect_uri='http://jamdigital.tech',
					 user_agent='Sentiment Analysis Prototype')
		self.code = "J0XCsi7HY6VkbFry6rlNe_6wnII"
		self.subreddits = []
		self.set_subreddits(subreddits)
		self.limit = limit
		self.comments_enabled = comments_enabled

	def run_authorization(self):
		""" Dev script right now. Used for retrieving an access code """
		from .scripts import retrieve_permanent_auth_token
		retrieve_permanent_auth_token.main()

	def set_subreddits(self, subreddits):
		if isinstance(subreddits, list):
			self.subreddits = subreddits
			return True
		self.subreddits = [subreddits]
		return True 

	def set_limit(self, limit):
		self.limit = limit
		return True

	# Rather than  a limit this should be a timeframe to keep a rolling list, or, easier than that,
	# just go far enough back that it can be generated every time.
	def get_submissions(self):
		""" Returns a dict of posts from a subreddit """
		submission_list = []
		for subreddit in self.subreddits:
			submission_list += self.reddit.subreddit(subreddit).new(limit=self.limit)
		# To be checked that the class can be ordered as a dict would
		ordered_submission_list = sorted(submission_list, key=lambda k: k.created)
		return ordered_submission_list

	def get_comments_text(self, submission):
		""" Get the text of all comments for a submission """
		#print(submission.comments)
		#print(dir(submission.comments))
		pass

	def get_raw_text(self):
		submissions = get_posts()
		for submission in submissions:
			combined_text = submission['selftext'] + " " + submission['title'] 
			sentiment_item = sentimentItem(submission['created'], combined_text)
			sentiment_items += [sentiment_item]

	def retrieve_by_keywords(self, keywords):
		""" Play method at the moment , can be removed """
		submissions = reddit.subreddit('all').search('dogs')
		submission_list = get_submission_dict(submissions)
		ordered_submission_list = sorted(submission_list, key=lambda k: k['created'])
		return ordered_submission_list