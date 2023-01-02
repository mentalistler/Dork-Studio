from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import dorker.dorkprocess as dorkprocess
from django.http import JsonResponse
from django.template.loader import render_to_string
def index(request):
    return render(request, 'dashboard.html')

def dorker(request):
    dorks = dorktype.objects.all()
    countries = country_codes.objects.all()
    wordlists = wordlistmain.objects.all()
    return render(request, 'dorker.html',{"dorks":dorks,"countries":countries,"wordlists":wordlists})

def dorkresults(request):
    _dorktype = request.POST.get("dorktype")
    _wordlist = request.POST.get("wordlist")
    _country = request.POST.get("country")
    _dorkcount = request.POST.get("dorkcount")
    _dorkcharacter =  request.POST.get("dorkcharacter")
    dorks= dorkprocess.dorkgenerator(_dorktype, _wordlist, _country, _dorkcount,_dorkcharacter)
    
    domain_country = country_codes.objects.filter(domain=_country)
    if(len(domain_country) ==0):
        domain_country = "Rastgele"
    else:
        domain_country = domain_country[0].country
    country = {"domain":_country,"country":domain_country}
    return render(request, 'dorkresults.html',{'context':dorks,"ctry":country})

def dorklist(request):
    dorks = dorktype.objects.all()
    return render(request, 'pages/dorklist.html',{"dorks":dorks})

def dorkdetail(request,pk):
    dorks = dorktype.objects.get(pk=pk)
    return render(request, 'pages/dorkdetail.html',{"dorks":dorks})

def DorkAdd(request):
    dorks = dorktype.objects.all()
    return render(request, 'pages/dorkadd.html',{'dorks':dorks})

def wordlistdetail(request):
    _wordlist = wordlistmain.objects.all()
    return render(request, 'pages/wordlist.html',{'wordlist':_wordlist})
def WordlistAdd(request):
    _wordlist = wordlistmain.objects.all()
    return render(request, 'pages/wordlistadd.html',{'wordlist':_wordlist})

def AjaxRemoveDork(request,pk):
    dorkcontents.objects.get(pk=pk).delete()
    return HttpResponse("ok")

def AjaxTrendQuery(request):
    word = request.POST.get("word")
    print(word)
    result = dorkprocess.trendquery(word)
    return JsonResponse(result, safe=False)
def AjaxAddDork(request):
    _dorklist = request.POST.get("dorks")
    _dorktype = request.POST.get("dorktype")
    _dorkname = request.POST.get("dorkname")
    if(_dorktype == "newdork"):
        add_dork_type = dorktype(name=_dorkname)
        add_dork_type.save()
        for line in _dorklist.splitlines():
            if(line.find("{{word}}") <0):
                line = f"{line} " + "{{word}}"
            add_dork_content = dorkcontents(dork=line)
            add_dork_content.save()
            add_dork_type.dork.add(add_dork_content.pk)
    else:
        get_dork_type = dorktype.objects.get(pk=_dorktype)
        for line in _dorklist.splitlines():
            if(line.find("{{word}}") <0):
                line = f"{line} " + "{{word}}"
            add_dork_content = dorkcontents(dork=line)
            add_dork_content.save()
            get_dork_type.dork.add(add_dork_content.pk)
    return HttpResponse("ok")
def AjaxAddWordlist(request):
    _wordlist = request.POST.get("wordlist")
    _wordlistType = request.POST.get("wordtype")
    _wordname = request.POST.get("wordlistname")
    if(_wordlistType == "newwordlist"):
        add_wordlist = wordlistmain(name=_wordname)
        add_wordlist.save()
        for line in _wordlist.splitlines():
            add_word = wordlist(word=line)
            add_word.save()
            add_wordlist.wordlist.add(add_word)
    else:
        get_wordlist = wordlistmain.objects.get(pk=_wordlistType)
        for line in _wordlist.splitlines():
            add_word = wordlist(word=line)
            add_word.save()
            get_wordlist.wordlist.add(add_word)
    return HttpResponse("ok")