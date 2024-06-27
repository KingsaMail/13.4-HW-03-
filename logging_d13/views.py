from django.shortcuts import render

from .forms import *

import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def index_2(request):
    if request.method != 'POST':
        form = TestForm()
    else:
        form = TestForm(request.POST)
        number_1 = int(request.POST['number_1'])
        number_2 = int(request.POST['number_2'])
        itog = number_1/number_2
        context = {'number_1': number_1, 'number_2': number_2, 'form': form, 'itog': itog, 'request': request}
        return render(request, 'index_2.html', context)
    
    context = {'form': form}
    return render(request, 'index_2.html', context)
