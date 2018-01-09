from django.db import models


class RedditItem(models.Model):
	api_id = models.CharField(max_length=30, unique=True, primary_key=True, blank=False)
	title = models.CharField(max_length=300)
	subreddit = models.CharField(max_length=20)
	raw_text = models.TextField()
	created = models.IntegerField()
	opinion = models.IntegerField()

