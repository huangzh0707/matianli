# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import TopList
from django.template import loader

# Create your views here.

def index(request):
    companies = TopList.objects.order_by('amount')[:3]
    template = loader.get_template('trends/index.html')
    context = {
        'companies': companies
    }
    return HttpResponse(template.render(context, request))
