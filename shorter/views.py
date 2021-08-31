from django.forms.widgets import HiddenInput
from .utils import get_full_url

from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponseRedirect

from .forms import UrlCreateforum
from .models import Url

def url_create(request):
    form = UrlCreateforum(request.POST or None)
    urls = Url.objects.all()
    default_len = 5
    if len(urls) <= 5:
        default_len = len(urls)-1
    urls = urls[len(urls) - default_len:]
    urls = [get_full_url(url.code_url) for url in urls]
    print()
    data = {'form': form, 'urls': urls}
    if request.method == 'POST' and form.is_valid():
        try:
            origin_url = request.POST.get('origin_url')
            url = Url.objects.get(origin_url = origin_url)
            data['code'] = get_full_url(url.code_url)
        except Url.DoesNotExist:
            instance = form.save()
            data['code'] = get_full_url(instance.code_url)
    return render(request,'index.html', data)

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def hello(request):
#     return HttpResponse('Hello world!')

def url_redirect(request, code):
    url = get_object_or_404(Url, code_url = code)
    return HttpResponseRedirect(url.origin_url)

