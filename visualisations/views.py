from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from webscrapers.reddit import scraperReddit
from webscrapers.bitcoin_api import BitcoinPrices
from visualisations.data_processors import lineChart
from django.views.generic import TemplateView
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt ## Need to pass CSRF token to index

def index(request):
    """ Main visualisations page """
    context = {}
    return render_to_response('index.html', context)


@csrf_exempt
def line_chart(request):
    """ Prototype: Display a simple line chart """
    context_instance=RequestContext(request)
    print('RECEIVED REQUEST: ' + request.method)
    if not request.method == 'POST':
        return HttpResponse("Failed to load chart")
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
    return render_to_response('charts/line.html',context)