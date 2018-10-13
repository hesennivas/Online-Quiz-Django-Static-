# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import multipleChoiceQuestions, imageQuestions, textQuestions, objResults, textAnswers
import random

# Create your views here.
def createUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return render(request, 'home/homepage.html',{
                'error': 'Sorry, username is already taken',
            }, content_type="text/html")
        else:
            User.objects.create_user(username=username, password='akhila@123')
            user = authenticate(username=username, password='akhila@123')
            login(request, user)
            return render(request, 'home/homepage.html',{
                'attempt': '1',
            }, content_type="text/html")
    return render(request, 'home/homepage.html', content_type="text/html")

def logoutUser(request):
    logout(request)
    return redirect('createUser')

def questions(request):
    if request.method == "POST" and request.POST.get('complete'):
        dump = textAnswers()
        dump.username = request.user.username
        dump.qnOneAns = request.POST.get('text1')
        dump.qnTwoAns = request.POST.get('text2')
        dump.qnThreeAns = request.POST.get('text3')
        dump.qnFourAns = request.POST.get('text4')
        dump.qnFiveAns = request.POST.get('text5')
        dump.qnSixAns = request.POST.get('text6')
        dump.save()
        return redirect('createUser')

    if request.method == "POST" and request.POST.get('moveToText'):
        data = []
        for i in range(1,6):
            indidata = {}
            indidata['questionNo'] = i
            indidata['ans'] = request.POST.get(str(i))
            data.append(indidata)
        ans = imageQuestions.objects.values('optionOneAns', 'optionTwoAns', 'optionThreeAns', 'optionFourAns', 'questionNo')
        total = 0
        for datum in data:
            for a in ans:
                if(datum['questionNo']==a['questionNo']):
                    try:
                        print(a[str(datum['ans'])+str("Ans")])
                    except:
                        continue
                    if(a[str(datum['ans'])+str("Ans")]):
                        total += 1
        test1 = request.session.get('total')
        total = total + test1
        dump = objResults()
        dump.username = str(request.user.username)
        dump.marks = int(total)
        dump.save()
        data = textQuestions.objects.values('question', 'questionNo')
        data = list(data)
        dataArray = range(len(data))
        dispArray = []
        disp = []
        while len(data) != len(disp):
            ran = random.choice(dataArray)
            if ran not in dispArray:
                dispArray.append(ran)
                disp.append(data[ran])
        return render(request, 'home/questions.html',{
            'typeThree': '3',
            'data': disp,
            'js': len(disp),
            'loop': xrange(1,len(disp)+1),
        }, content_type="text/html")

    if request.method == "POST" and request.POST.get('moveToImage'):
        data = []
        for i in range(1,20):
            indidata = {}
            indidata['questionNo'] = i
            indidata['ans'] = request.POST.get(str(i))
            data.append(indidata)
        ans = multipleChoiceQuestions.objects.values('optionOneAns', 'optionTwoAns', 'optionThreeAns', 'optionFourAns', 'questionNo')
        total = 0
        for datum in data:
            for a in ans:
                if(datum['questionNo']==a['questionNo']):
                    try:
                        print(a[str(datum['ans'])+str("Ans")])
                    except:
                        continue
                    if(a[str(datum['ans'])+str("Ans")]):
                        total += 1
        request.session['total'] = total
        data = imageQuestions.objects.values('question', 'image', 'optionOne', 'optionTwo', 'optionThree', 'optionFour', 'questionNo')
        data = list(data)
        dataArray = range(len(data))
        dispArray = []
        disp = []
        while len(data) != len(disp):
            ran = random.choice(dataArray)
            if ran not in dispArray:
                dispArray.append(ran)
                disp.append(data[ran])
        return render(request, 'home/questions.html',{
            'typeTwo': '2',
            'data': disp,
            'js': len(disp),
            'loop': xrange(1,len(disp)+1),
        }, content_type="text/html")
    data = multipleChoiceQuestions.objects.values('question', 'optionOne', 'optionTwo', 'optionThree', 'optionFour', 'questionNo')
    data = list(data)
    dataArray = range(len(data))
    dispArray = []
    disp = []
    while len(data) != len(disp):
        ran = random.choice(dataArray)
        if ran not in dispArray:
            dispArray.append(ran)
            disp.append(data[ran])
    return render(request, 'home/questions.html',{
        'typeOne': '1',
        'data': disp,
        'js': len(disp),
        'loop': xrange(1,len(disp)+1),
    }, content_type="text/html")
