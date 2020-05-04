# Created by me
from django.http import HttpResponse
from django.shortcuts import render
"""
def navigator(request):
    s='''<h1> Personal Navigator<br></h1>
    <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">DJANGO WITH HARRY BHAI</a><br>
    <a href="https://www.hackerrank.com/aryandaftari7?hr_r=1">HACKERRANK</a><br>
    <a href="https://github.com/">GITHUB</a><br>
    <a href="https://getbootstrap.com/">BOOTSTRAP</a><br>
    <a href="https://www.youtube.com/">YOUTUBE</a><br>'''
    return HttpResponse(s)
"""
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Welcome")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    # Get the text Written by user
    djtext = (request.POST.get('text', 'default'))
    dtext = (request.POST.get('text', 'default'))
    # Checking CheckBox Value
    rempvepunc = (request.POST.get('removepunc', 'off'))

    # Checking CheckBox Value

    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    if rempvepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params={'purpose': 'Removed Punctations','analyzed_text':analyzed}
        djtext=analyzed
       # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Next Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char


        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount  == "on":
        analyzed = len(dtext)
        dtext= djtext +"\nThe charcount is :"+str(analyzed)
        params = {'purpose': 'Char Count', 'analyzed_text': dtext}

        #return render(request, 'analyze.html', params)

    if rempvepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on" :
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)


