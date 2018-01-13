import praw
import datetime
from pprint import pprint
from webscrapers.models import RedditItem

# This file is the major reason it would be good to plan out a revised structure for the system
# but the majority of the functional code should be re-usable in that instance.

class storedReddit:
    """ First point of contact for queries to hit the database though it will use
        the scraperClass to fill any additional blanks for the time being """
    def __init__(self, subreddits=[], comments_enabled=False, limit=10):
        self._subreddits = subreddits
        print(subreddits)
        self._comments = comments_enabled
        self._limit = limit
        self._date_range = ""

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



class scraperReddit:
    """ Simple wrapper class for the praw library """
    def __init__(self, subreddits=[], comments_enabled=False, limit=10):
        self.reddit = praw.Reddit(client_id='jIFEM8LpRrB6Jg',
                     client_secret='lvvM7fAWqaoZXY7Pt1jqqmOq36w',
                     refresh_token='XjbgymmHelvylKwQFDRwGI1lryw',
                     user_agent='Sentiment Analysis Prototype')
        print(self.reddit.auth.scopes())
        # This needs some checking and refreshing code
        # Or I'm being silly and not quite understanding the "state" parameter's permanent option
        self.code = "XjbgymmHelvylKwQFDRwGI1lryw" 
        self._subreddits = subreddits # self.subreddits(subreddits)
        self._limit = limit
        self._comments = comments_enabled

    def run_authorization(self):
        """ Dev script right now. Used for retrieving an access code. 
            Borrowed from PRAW docs, can be run through on the command line.
            Would be ideal to automate this as it'll be less ideal for WSGI setups """
        from .scripts import retrieve_permanent_auth_token
        retrieve_permanent_auth_token.main()

    def subreddits(self, subreddits): # Add assigned param here 
        """ Assign or return a subreddit """
        # BUG: A ['NAME'] single entry list can be passed and break the praw code.
        if isinstance(subreddits, list):
            self._subreddits = subreddits
        self._subreddits = [subreddits] 

    def limit(self, limit):
        self._limit = limit
        return True

    # Rather than  a limit this should be a timeframe to keep a rolling list, or, easier than that,
    # just go far enough back that it can be generated every time.
    def submissions(self):
        """ Returns a dict of posts from a subreddit """
        submission_list = []
        for subreddit in self._subreddits:
            submission_list += self.reddit.subreddit(subreddit).new(limit=self._limit)
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