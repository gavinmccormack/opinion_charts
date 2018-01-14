from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from visualisations.data_processors import lineChart
from django.views.generic import TemplateView
from django.template import RequestContext
import json


from webscrapers.reddit import RedditScraper
from webscrapers.bitcoin_api import BitcoinPrices


from django.views.decorators.csrf import csrf_exempt ## Need to pass CSRF token to index

def index(request):
    """ Main visualisations page """
    context = {}
    return render_to_response('index.html', context)


def test_scraper():
    """ Delete me """
    scraper = RedditScraper()
    print(scraper.limit())


@csrf_exempt
def line_chart(request):
    """ Prototype: Display a simple line chart """
    if not request.method == 'POST':
        return HttpResponse("Denied: Requires a POST connection") # Return a status code here
    
    context = {}
    context_instance=RequestContext(request)
    
    request_data = json.loads(request.body)

    test_scraper()

    return render_to_response('charts/line.html',context)