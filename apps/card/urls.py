#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/10 
"""

from django.conf.urls import url
from card.views import card

urlpatterns = [
    url('^$', card.index, name='index'),
    url('^save$', card.save, name='save'),
    url('^contact$', card.save, name='contact'),
    url('^search$', card.search, name='search')
]