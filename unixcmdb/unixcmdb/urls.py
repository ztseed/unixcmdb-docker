# from django.conf.urls import url
from django.urls import include, re_path

from django.urls import path
 
from . import nnitcmdb

 
urlpatterns = [
    # url(r'^$',nnitcmdb.index),
    re_path(r'^$',nnitcmdb.index),
    path('unixcmdb/',nnitcmdb.nnitcmdb),
    path('serverinout/',nnitcmdb.server_in_out),
    path('api/echarts/', nnitcmdb.echarts_data, name='api-echarts'),
]
