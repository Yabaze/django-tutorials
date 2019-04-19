from django.shortcuts import render , get_object_or_404

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404

from .forms import PostModelForm
from .models import PostModel

@login_required(login_url='/admin')
def post_model_list_view_with_login_required(request):
    qs = PostModel.objects.all()
    context = {
        "object_list":qs,
        "fruits" : ["apple", "banana", "cherry"],
    }
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        template_path = "blog/list-view.html"
        print ("Logged in")
    else:
        template_path = "blog/list-view-public.html"
        print("Not Logged in")   
        # raise Http404 
    #template_path = "blog/list-view.html"
    return render(request,template_path,context)
    #return HttpResponse("Some Data...")

def post_model_list_view(request):
    qs = PostModel.objects.all()
    context = {
        "object_list":qs,
        "fruits" : ["apple", "banana", "cherry"],
    }
    template_path = "blog/list-view.html"
    return render(request,template_path,context)

def post_model_create_view(request):
    # if request.method == "POST" :
    #     print(request.POST)
    #     form = PostModelForm(request.POST or None)
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         print(form.cleaned_data)        

    form = PostModelForm(request.POST or None)
    context = {
            'form':form
        }
    if form.is_valid():
        obj = form.save(commit=False)
        print(form.cleaned_data)       
        
    template_path = "blog/create-view.html"
    return render(request,template_path,context)


def post_model_detail_view(request,id=None):
    obj = get_object_or_404(PostModel)
    context = {
        "object":obj,
        #"fruits" : ["apple", "banana", "cherry"],
    }
    template_path = "blog/detail-view.html"
    return render(request,template_path,context)