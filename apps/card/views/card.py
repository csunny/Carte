#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/10 
"""
import copy
import json
import logging
from card import settings
from django.shortcuts import render, HttpResponse
from card.models import CardModal
from card.forms import CardModalForm
from django.db.models import Q

django_log = logging.getLogger("django")


def index(request):
    SITE_NAME = '名片网'
    return render(request, 'index.html', locals())


def save(request):
    """
    保存名片数据
    :param request:
    :return:
    """
    card = CardModalForm(request.POST)
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    if card.is_valid():
        info = card.cleaned_data

        card_model = CardModal()
        card_model.name = info['name']
        card_model.email = info['email']
        card_model.position = info['position']
        card_model.company = info['company']
        card_model.website = info['website']
        card_model.phone = info['phone']
        card_model.sex = info['sex']
        card_model.birthday = info['birthday']
        card_model.save()

        rsp_data.update(**info)

        rsp_data['website'] = card_model.website if card_model.website.startswith(
            'http') else 'http://' + card_model.website
        return HttpResponse(json.dumps(rsp_data), content_type="application/json")
    else:
        rsp_data = copy.copy(settings.ERROR['NOT_EXIST_ERR'])
        return HttpResponse(json.dumps(rsp_data), content_type="application/json")


def search(request):
    """

    :param request:
    :return:
    """
    rsp_data = copy.copy(settings.ERROR["SUCC"])
    val = request.GET.get('value')
    try:
        card_model = CardModal.objects.filter(Q(name=val) | Q(phone=val)).order_by('-id')[0]
    except IndexError:
        card_model = None
    if card_model:
        rsp_data['name'] = card_model.name
        rsp_data['email'] = card_model.email
        rsp_data['position'] = card_model.position
        rsp_data['company'] = card_model.company
        rsp_data['website'] = card_model.website if card_model.website.startswith('http') else 'http://' + card_model.website
        rsp_data['phone'] = card_model.phone
        rsp_data['sex'] = card_model.sex
        rsp_data['birthday'] = card_model.birthday
    else:
        rsp_data = copy.copy(settings.ERROR['NOT_EXIST_ERR'])
    return HttpResponse(json.dumps(rsp_data), content_type="application/json")
