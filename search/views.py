# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import TopList
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('search/index.html')
    context = {
        'top_project': 'wulalalal',
    }
    return HttpResponse(template.render(context, request),)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

