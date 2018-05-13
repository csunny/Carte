#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/12 
"""

from django import forms


class CardModalForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    position = forms.CharField()
    company = forms.CharField()
    website = forms.CharField(required=False)
    phone = forms.CharField()
    sex = forms.CharField()
    birthday = forms.CharField()


