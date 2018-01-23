from textblob import TextBlob

class ScraperItem:
    """ Super class for individual data points. """
    def __init__(self, api_id, title, raw_text, created, polarity):
        self._id = api_id
        self._title = title
        self._raw_text = raw_text
        self._created = created
        self._polarity = self.polarity(raw_text)

    def sentiment(self, text=None):
        """ Calculate or return polarity of raw_text """
        if not text:
            return self._polarity
        blob = TextBlob(text)
        self._polarity = blob.polarity

class Scraper:
    """ Super class for scrapers. Should include common search functions """
    def __init__(self, date_range=None, keywords=None, limit=100):
        self._date_range = ""
        self._limit = limit
        self._keywords = keywords
        self._entries = [] 

    def limit(self, limit=None):
        """ Set or return limit. Returns true if set """
        if not limit:
            return self._limit
        self._limit = limit
        return True

    def keywords(self, keywords=None):
        """ Set or return keywords. Returns true if set """
        if not keywords:
            return self._keywords
        self._keywords = keywords
        return True

    def date_range(self, date_range=None):
        """ Set the date range for the scraper to return """
        if not date_range:
            return self._date_range
        self._date_range = date_range
        return True

    def save_entries_to_database(self, database_model):
        """ Saves entries to database. """
        return True



