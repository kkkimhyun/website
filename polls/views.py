from django.shortcuts import render, get_object_or_404
from polls.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def Genderview(request):
    gender = Gender.objects.all()

    return render(request, 'polls/gender.html', {'gender' : gender})

def Styleview(request, gender_id):
    select_gender = get_object_or_404(Gender, pk = gender_id)

    style = select_gender.style_set.values()

    return render(request, 'polls/style.html', {'select_gender' : select_gender, 'style' : style})



def Webview(request, style_id):
    select_style = get_object_or_404(Style, pk = style_id)
    web = select_style.stylewebsite_set.all()

    return render(request, 'polls/web.html', {'select_style' : select_style, 'web' : web})
