# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import Http404
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

def profile(request, company_id):
    try:
        company = TopList.objects.get(pk=company_id)
    except TopList.DoesNotExist:
        raise Http404("Company does not exist")
    template = loader.get_template('trends/profile.html')
    context = {
        'company': company
    }
    return HttpResponse(template.render(context, request))