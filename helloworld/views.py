 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from post.models import Post

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
   
def post(request):
  data = Post.objects.all()
  return TemplateResponse(request,'index.html',{ "data" : data } )
