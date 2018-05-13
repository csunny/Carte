#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/12 
"""

import logging
import json
import copy
from django.shortcuts import render, HttpResponse
from card import settings
from django.views.decorators.csrf import csrf_exempt
# from card.models import Contact
# from card.forms import ContactForm

django_log = logging.getLogger("django")


@csrf_exempt
def contact(request):
    """

    :param request:
    :return:
    """
    rsp_data = copy.copy(settings.ERROR["SUCC"])
    print(request.POST)

    # cnt = ContactForm(request.POST)
    # if cnt.is_valid():
    #     info = contact.cleaned_data
    #
    #     cnt_model = Contact()
    #     cnt_model.name = info['name']
    #     cnt_model.email = info['email']
    #     cnt_model.title = info['title']
    #     cnt_model.content = info['content']
    #
    #     cnt_model.save()
    return HttpResponse(json.dumps(rsp_data), content_type="application/json")