# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from unixcmdb_mysql.models import UnixLinuxActFull
from unixcmdb_mysql.models import UnixLinuxRetFull
from unixcmdb_mysql.models import ServerInOut

from django.shortcuts import render

from django.views.decorators import csrf

from django.db.models import Count

from django.http import JsonResponse
 
def index(request): 

    return render(request, 'index.html')

def nnitcmdb(request):
    ctx ={}
    serverlist1 = UnixLinuxActFull.objects.all().values()
    serverlist2 = UnixLinuxRetFull.objects.all().values()
    ctx['list1'] = serverlist1
    ctx['list2'] = serverlist2

    return render(request, 'main_table.html' ,ctx)

def echarts_data(request):
    _x = UnixLinuxActFull.objects.values_list('customer').annotate(Count('customer')).order_by('-customer__count')

    jsondata = {
        "key": [i[0] for i in _x],
        "value": [i[1] for i in _x]
    }

    return JsonResponse(jsondata)

def server_in_out(request):
    ctx ={}
    serverlist = ServerInOut.objects.all().values()
    ctx['list'] = serverlist
    
    return render(request, 'server_in_out.html' ,ctx)
