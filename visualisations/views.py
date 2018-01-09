from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from webscrapers.reddit import scraperReddit
from visualisations.data_processors import lineChart

def index(request):
    context = {}
    
    #Some sample chart code
    opinion_reddit = scraperReddit(subreddits=['BitcoinMarkets'], limit=100)
    submissions = opinion_reddit.get_submissions()
    chart_data = lineChart().reddit(submissions)

    #Test context
    context =  {'values': chart_data}
    return render_to_response('index.html', context)