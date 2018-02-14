 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from helloworld.models import Post

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
   
    def posts(request):
      data = Post.objects.all()
      return TemplateResponse(request,'helloworld/index.html',{ "data" : data } )
