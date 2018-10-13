# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import multipleChoiceQuestions, textQuestions, imageQuestions, objResults, textAnswers

# Register your models here.
admin.site.register(multipleChoiceQuestions)
admin.site.register(textQuestions)
admin.site.register(imageQuestions)
admin.site.register(objResults)
admin.site.register(textAnswers)
