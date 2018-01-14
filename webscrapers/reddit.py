import praw
import datetime
from pprint import pprint
from webscrapers.models import RedditItem
from webscrapers.scraper import Scraper
# This file is the major reason it would be good to plan out a revised structure for the system
# but the majority of the functional code should be re-usable in that instance.

class RedditScraper(Scraper):
    """ First point of contact for queries to hit the database though it will use
        the scraperClass to fill any additional blanks for the time being """
    def __init__(self, subreddits=[], date_range=None, keywords=None, comments_enabled=False, limit=10):
        super().__init__(date_range,keywords, limit)
        self._subreddits = subreddits
        self._comments = comments_enabled

    def submissions(self):
        # a check here for whether the database is up to date
        opinion_reddit = scraperReddit(subreddits='BitcoinMarkets', limit=self._limit)
        submissions = opinion_reddit.submissions()
        submissions = RedditItem.objects.all()
        return submissions


    def subreddits(self, subreddits): # Add assigned param here 
        """ Assign or return a subreddit """
        # BUG: A ['NAME'] single entry list can be passed and break the praw code.
        if isinstance(subreddits, list):
            self._subreddits = subreddits
        self._subreddits = [subreddits] 

    def save_submissions(self,submissions):
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

