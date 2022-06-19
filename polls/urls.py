from django.contrib import admin
from django.urls import path, include
from polls.views import *
app_name='polls'

urlpatterns = [
    path('', Genderview, name='genderview'),
    path('<gender_id>/style/', Styleview, name = 'styleview'),
    path('<style_id>/website/', Webview, name = 'webview'),
]
