from django.shortcuts import render, redirect
from .models import Articles
from main.models import Post
from datetime import datetime

from .forms import ArticlesForm
from django.views.generic import DeleteView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


# Create your views here.




def register(request, id):
    detail = Post.objects.get(pk=id)

    if request.method == "POST": 
        form = ArticlesForm(request.POST)
    
        
        if form.is_valid():
            article = form.save(commit=False)  # Не сохраняем пока в базе, чтобы изменить поля
            
            # Заполняем поля NameClub и NameNews из объекта detail
            article.NameClub = detail.ClubName
            article.NameNews = detail.NewsName
            
            # Сохраняем объект в базе данных
            article.save()
            
            return redirect('home')
    else:
        form=ArticlesForm()
    
    data={
         'form':form ,
         'detail':detail
    }
    return render(request, 'base/RegisterPage.html',data)



class PostRegDetailView(DetailView):   
    model=Post
    template_name = 'base/RegisterPage.html'
    context_object_name = 'reg'