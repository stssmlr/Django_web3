from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def news_list(request):
    return render(request, "news_list.html")

# Створення нового посту
@login_required
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user      
            post.save()   
            return redirect('news:list')
    else:
        form = forms.PostForm()
    return render(request, 'posts/post_form.html', {'form': form})