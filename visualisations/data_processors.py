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
		graph_data = []
		for submission in submissions:
			raw_text = submission.title + " " + submission.selftext
			created = datetime.fromtimestamp(submission.created).strftime('%c')
			sentiment = sentimentItem(raw_text)
			graph_data += [[created, sentiment.polarity, submission.title]]

			# Saving these to DB
			# Super simple implementation, probably better to not do single queries.
			reddit_db = RedditItem()
			reddit_db.api_id = submission.id
			reddit_db.title = submission.title
			reddit_db.raw_text = raw_text
			reddit_db.subreddit = submission.subreddit
			reddit_db.created = submission.created
			reddit_db.opinion = sentiment.polarity
			reddit_db.save()

		return graph_data

