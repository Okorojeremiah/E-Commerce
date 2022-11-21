from django.shortcuts import render
from http import HTTPStatus


# Create your views here.
def index(request):
    return render(request, 'tags/product_tags.html', status=HTTPStatus.ACCEPTED)