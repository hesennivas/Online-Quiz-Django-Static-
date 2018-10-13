# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class multipleChoiceQuestions(models.Model):
    questionNo = models.IntegerField(null=True)
    question = models.CharField(null=False, blank=False, max_length=2000)
    optionOne = models.CharField(null=False, blank=False, max_length=1000)
    optionTwo = models.CharField(null=False, blank=False, max_length=1000)
    optionThree = models.CharField(null=False, blank=False, max_length=1000)
    optionFour = models.CharField(null=False, blank=False, max_length=1000)
    optionOneAns = models.BooleanField(null=False)
    optionTwoAns = models.BooleanField(null=False)
    optionThreeAns = models.BooleanField(null=False)
    optionFourAns = models.BooleanField(null=False)

    def __str__(self):
        return  str(self.questionNo)

class imageQuestions(models.Model):
    questionNo = models.IntegerField(null=True)
    question = models.CharField(null=False, blank=False, max_length=2000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    optionOne = models.CharField(null=False, blank=False, max_length=1000)
    optionTwo = models.CharField(null=False, blank=False, max_length=1000)
    optionThree = models.CharField(null=False, blank=False, max_length=1000)
    optionFour = models.CharField(null=False, blank=False, max_length=1000)
    optionOneAns = models.BooleanField(null=False)
    optionTwoAns = models.BooleanField(null=False)
    optionThreeAns = models.BooleanField(null=False)
    optionFourAns = models.BooleanField(null=False)
    def __str__(self):
        return  str(self.questionNo)


class textQuestions(models.Model):
    questionNo = models.IntegerField(null=True)
    question = models.CharField(null=False, blank=False, max_length=2000)
    answer = models.CharField(null=True, blank=True, max_length=2000)
    def __str__(self):
        return  str(self.questionNo)


class objResults(models.Model):
    username = models.CharField(null=False, blank=False, max_length=200)
    marks = models.IntegerField(null=True)
    def __str__(self):
        return  str(self.username)

class textAnswers(models.Model):
    username = models.CharField(null=False, blank=False, max_length=200)
    qnOneAns = models.CharField(null=False, blank=False, max_length=2000)
    qnTwoAns = models.CharField(null=False, blank=False, max_length=2000)
    qnThreeAns = models.CharField(null=False, blank=False, max_length=2000)
    qnFourAns = models.CharField(null=False, blank=False, max_length=2000)
    qnFiveAns = models.CharField(null=False, blank=False, max_length=2000)
    qnSixAns = models.CharField(null=False, blank=False, max_length=2000)
    marks = models.IntegerField(null=True)
    def __str__(self):
        return  str(self.username)
