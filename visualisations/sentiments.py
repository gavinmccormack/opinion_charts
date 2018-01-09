from textblob import TextBlob

class sentimentItem:
	def __init__(self, text):
		self.text = text
		self.polarity = self.polarity()

	def polarity(self, polarity=None):
		if polarity is not None:
			self.polarity = polarity
			return True
		self.polarity = TextBlob(self.text).polarity
		return self.polarity
