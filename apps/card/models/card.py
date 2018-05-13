#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/5/12 
"""

from django.db import models


class CardModal(models.Model):
    name = models.CharField(max_length=128, default="", verbose_name="姓名")
    email = models.EmailField(max_length=64, default="", verbose_name='邮箱')
    position = models.CharField(max_length=256, default="", verbose_name='职位')
    company = models.CharField(max_length=128, default="", verbose_name="公司")
    website = models.CharField(max_length=512, null=True, verbose_name="网站")
    phone = models.CharField(max_length=15, unique=True, verbose_name="手机号码")
    sex = models.CharField(max_length=32, default="", verbose_name="性别")
    birthday = models.CharField(max_length=128, default="", verbose_name="出生年月")

    def __str__(self):
        return self.name

    class Meta:
        app_label = "card"
        verbose_name = "名片"
        verbose_name_plural = verbose_name

