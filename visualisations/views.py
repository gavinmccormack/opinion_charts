from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from webscrapers.reddit import scraperReddit
from webscrapers.bitcoin_api import BitcoinPrices
from visualisations.data_processors import lineChart

def index(request):
    context = {}
    
    #Some sample chart code for opinion
    opinion_reddit = scraperReddit(subreddits='BitcoinMarkets', limit=1000)
    submissions = opinion_reddit.get_submissions()
    chart_data = lineChart().reddit(submissions)
    context['chart_data_opinion'] = chart_data

    # Some sample chart code for bitcoin prices
    bp = BitcoinPrices()
    price_data = bp.get_price_in_range("Tue Sep 1 23:59:11 2013","Tue Sep 5 23:59:11 2013")
    context['chart_data_prices'] = price_data

    # Will need to adapt the date system here, as google charts doesn't consider this
    # date format to be a cohesive range ( instead each date is taken as an unrelated, 
    # but ordered, point)

    return render_to_response('index.html', context)