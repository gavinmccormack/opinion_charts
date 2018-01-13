from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from visualisations.data_processors import lineChart
from django.views.generic import TemplateView
from django.template import RequestContext
import json


from webscrapers.reddit import scraperReddit, storedReddit
from webscrapers.bitcoin_api import BitcoinPrices


from django.views.decorators.csrf import csrf_exempt ## Need to pass CSRF token to index

def index(request):
    """ Main visualisations page """
    context = {}
    return render_to_response('index.html', context)


@csrf_exempt
def line_chart(request):
    """ Prototype: Display a simple line chart """
    print('RECEIVED REQUEST: ' + request.method)
    if not request.method == 'POST':
        return HttpResponse("Denied: Requires a POST connection") # Return a status code here
    
    context = {}
    context_instance=RequestContext(request)
    
    request_data = json.loads(request.body)

    #Testing database retrieval
    stored = storedReddit(subreddits=['BitcoinMarkets'], limit=100)
    submissions = stored.submissions()
    chart_data = lineChart().reddit(submissions)
    stored_data = lineChart().reddit(submissions)
    context['chart_data_opinion'] = chart_data
    return render_to_response('charts/line.html',context)

    #unpack json for opinion charts
    sources = request_data['sources']
    limit = int(request_data['limit'])
    start_date = request_data['date_range'].split('-')[0]
    end_date = request_data['date_range'].split('-')[1]

    #Some sample chart code for opinion
    chart_data = lineChart().reddit(submissions)
    context['chart_data_opinion'] = chart_data

    # Some sample chart code for bitcoin prices
    bp = BitcoinPrices()
    price_data = bp.get_price_in_range(start_date,end_date)
    context['chart_data_prices'] = price_data

    return render_to_response('charts/line.html',context)