"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views #here . means root directory and from this root directory we are importing our views.py file

#thiscode is only for index page and for about page
'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #this is the home page of our project, the name of this page is "index"
    #and views.index is a function which is written in our view.py file which we are using here

    path('about/', views.about, name='about'),#here 'about/' means we are in about page, and we are using views.about Function
    #and the name of this page is 'about'
]'''

urlpatterns=[
  path('admin/',admin.site.urls),
  path('',views.index,name='index'),#home page
  path('analyze', views.analyze, name='analyze'),#page to remove punctuations
  # path('capitalizedfirst/',views.capitalizedfirst, name='capitalizedfirst'),#page to capitalized first character
  # path('newlineremover/',views.newlineremover, name='newlineremover'),#page to remove new line
  # path('spaceremover/',views.spaceremover, name='spaceremover'),#page to remove spaceremover
  # path('charcount/',views.charcount, name='charcount'),#page to count the character from the sentences

]
