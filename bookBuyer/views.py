from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404 ,render
from django.views import generic
from django.template import Context
from django.contrib.auth.decorators import login_required

import exceptions

from .forms import isbnForm
from .models import Book, Cost

from media.BookScouter import BookScouter


class IndexView(generic.ListView):
    template_name = 'bookBuyer/index.html'

class IsbnView(generic.ListView):
    template_name = 'bookBuyer/isbn.html'

    def get_queryset(self):
        return 'null'

class RetrievePriceView(generic.ListView):
    template_name = 'bookBuyer/retrievePrice.html'


def index(request):
    return render(request, 'bookBuyer/index.html')

@login_required
def isbn(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = isbnForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data
            data = form.cleaned_data
            print data
            # Hold isbn from Form in the Session dictionary
            request.session['isbn'] = form.cleaned_data['isbn']
            # ...
            #get prices from bookScouter
            bookScouter = BookScouter(request.session['isbn'])
            price_list = bookScouter.getPrice()
            print price_list

            # hold price information in a list stored in session}
            request.session['price_list'] = price_list

            return HttpResponseRedirect( 'retrievePrice')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = isbnForm()

    return render(request, 'bookBuyer/isbn.html', {'form': form})

    # return HttpResponse("Hello World")
    # return render(request, 'bookBuyer/index.html')
# @login_required
def retrievePrice(request):
    #Redirects from isbn Page. displays scraped book & price data stored in Session
    # isbn = request.session['isbn']


    if 'list' in request.GET :
        print "CLICKED THE BUY bUTTON??? /n DID YOU DO IT /n"

        # try :
        #     book = question.choice_set.get(request.session['isbn']
        # except Exception as e:
        #    book = Book()
        #    book.isbn = request.session['isbn']

        #save book data to Database
        book = Book()
        book.isbn = request.session['isbn']
        book.stock += 1
        book.title = request.session['price_list'][2]
        book.save()

        #save cost data to database
        cost = Cost()
        cost.book = book
        cost.book_cost = request.session['price_list'][0]
        cost.user = request.user.username
        cost.save()


        return HttpResponse(request.session['price_list'])

    else:
        # bookScouter = BookScouter(isbn)
        # price_list = bookScouter.getPrice()
        # print price_list
        #
        # context_dict = {'price_list' : price_list}
        # request.session['price_list'] = price_list
        context_dict = {'price_list' : request.session['price_list']}

        return render(request, 'bookBuyer/retrievePrice.html' , context_dict)

@login_required
def buy(request):
    return HttpResponse("Hello World")
# Create your views here.
