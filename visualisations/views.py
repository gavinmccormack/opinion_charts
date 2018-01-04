from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from webscrapers.reddit import scraperReddit

def index(request):
    context = {}
    
    #Some sample chart code
    opinion_reddit = scraperReddit(subreddits='BitcoinMarkets')
    print(opinion_reddit)
    subreddits = opinion_reddit.get_submissions()
    print(subreddits)

    #Test context
    context = {'values': [['foo', 32], ['bar', 64], ['baz', 96]]}
    return render_to_response('home/homepage.html', context)