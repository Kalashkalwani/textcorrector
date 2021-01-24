from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def analyze(request):
    dtext = request.POST.get("text", "Enter text first")
    removepunc = request.POST.get("removepunc", "off")
    capitalizeAll = request.POST.get("CapitalizeAll", "off")
    rnl = request.POST.get("rnl", "off")
    res = request.POST.get("res", "off")
    params = {'purpose': []}

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': params['purpose']+['Removed Punctuations'], 'analyzed_text': analyzed}
        dtext = analyzed

    if capitalizeAll == "on":
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': params['purpose'] + ['Capitalize All'], 'analyzed_text': analyzed}
        dtext = analyzed

    if rnl == "on":
        analyzed = ""
        for char in dtext:
            if char in ['\n' ,'\r']:
                analyzed = analyzed + " "
            else:
                analyzed = analyzed + char
        params = {'purpose': params['purpose'] + ['Capitalize All'], 'analyzed_text': analyzed}
        dtext = analyzed

    if res == "on":
        analyzed = dtext.strip()
        params = {'purpose': params['purpose'] + ['Capitalize All'], 'analyzed_text': analyzed}
        dtext = analyzed

    return render(request, "result.html",params)

def contact(request):
    return render(request,"contact.html")







