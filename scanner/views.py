from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import scanner.scanner as dorkscan

def scanner(request):
    dorks = request.POST.get("dorks")
    return render(request, 'scanner/scan.html',{"dorks":dorks})

def AjaxDorkScan(request):
    dork = request.POST.get('dork')
    _scanner = dorkscan.dscr()
    result = _scanner.search_results(dork)
    print(result)
    return JsonResponse(result, safe=False)