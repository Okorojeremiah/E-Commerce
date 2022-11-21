from django.shortcuts import render
from http import HTTPStatus


# Create your views here.
def index(request):
    return render(request, 'store/store.html', status=HTTPStatus.ACCEPTED)