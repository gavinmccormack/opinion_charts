import praw
import datetime
from pprint import pprint



class opinionReddit:
	""" Simple wrapper class for the praw library for the opinion tools """
	def __init__():
		self.reddit = praw.Reddit(client_id='jIFEM8LpRrB6Jg',
                     client_secret='lvvM7fAWqaoZXY7Pt1jqqmOq36w',
                     password='',
                     user_agent='Testscript for sentiment analysis',
                     username='eroficgen') ## To be converted to a sensible auth system

	def retrieve_subreddits(self, subreddits):
		""" Takes a dict of subreddits and a number of posts """
		submission_list = []
		for subreddit, limit in subreddits.items():
			submission_list += retrieve_posts(subreddit, limit)
		return submission_list

	# Rather than  a limit this should be a timeframe to keep a rolling list, or, easier than that,
	# just go far enough back that it can be generated every time.
	def retrieve_posts(self, subreddit, limit):
		""" Returns a dict of posts from a subreddit """
		submissions = reddit.subreddit(subreddit).new(limit=limit)

		# To be checked that the class can be ordered as a dict would
		ordered_submission_list = sorted(submissions, key=lambda k: k.created)
		return ordered_submission_list

	def get_comments_text(self, submission):
		""" Get the text of all comments for a submission """
		pass

	def retrieve_by_keywords(self, keywords):
		""" Play method at the moment , can be removed """
		submissions = reddit.subreddit('all').search('dogs')
		submission_list = get_submission_dict(submissions)
		ordered_submission_list = sorted(submission_list, key=lambda k: k['created'])
		return ordered_submission_list