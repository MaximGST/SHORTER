
from django.urls import path
from django.urls.conf import include

#from .views import index
from .views import url_create, url_redirect

app_name = 'shorter'

urlpatterns = [
    #path('index/', index)
    #path('', hello, name = 'hello')
    path('', url_create, name='url'),
    path('<str:code>', url_redirect, name = 'url_redir'),
]
