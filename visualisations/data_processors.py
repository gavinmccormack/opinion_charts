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
		graph_data = [["Time", "Opinion"]]
		for submission in submissions:
			raw_text = submission.title + " " + submission.raw_text
			created = datetime.fromtimestamp(submission.created).strftime('%c')
			sentiment = sentimentItem(raw_text)
			graph_data += [[created, submission.opinion]]
		return graph_data

