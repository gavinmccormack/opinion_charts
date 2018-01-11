from visualisations.sentiments import sentimentItem
from datetime import datetime


# Shoehorning in some database saving
from webscrapers.models import RedditItem


# Formatting for visualisations

class lineChart:
	""" Return data for line charts """
	def __init__(self):
		pass

	def reddit(self, submissions):
		#save_submissions_db(submissions)
		graph_data = [["Time", "Opinion"]]
		for submission in submissions:
			raw_text = submission.title + " " + submission.selftext
			created = datetime.fromtimestamp(submission.created).strftime('%c')
			sentiment = sentimentItem(raw_text)
			graph_data += [[created, sentiment.polarity]]
		return graph_data

		def save_submissions_db(submissions):
			""" Save new entries from the API to the DB """
			for submission in submissions:
				raw_text = submission.title + " " + submission.selftext
				created = datetime.fromtimestamp(submission.created).strftime('%c')
				sentiment = sentimentItem(raw_text)
				reddit_db = RedditItem()
				reddit_db.api_id = submission.id
				reddit_db.title = submission.title
				reddit_db.raw_text = raw_text
				reddit_db.subreddit = submission.subreddit
				reddit_db.created = submission.created
				reddit_db.opinion = sentiment.polarity
				reddit_db.save()

		def get_stored_submissions():
			""" Semi-test method for retrieving items from the db """
			return RedditItem.objects.all()