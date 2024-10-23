from django.shortcuts import render, redirect, request
from .models import Article
# from .forms import PostForm


def articles():
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context=context)  
# memgoni am contexts ar vikeneb arsad


def create_articles():
    postfrom = PostForm()
    if request.method == 'POST':
        postfrom = PostForm(request.POST)
        if postfrom.is_valid():
            postfrom.save()
            return redirect('home') 
    return render(request, 'create_articles.html', context={'form': postfrom})

# azrzearvar