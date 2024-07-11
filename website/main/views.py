from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, View
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request): #метод главной страницы
    cats = Category.objects.all()
    return render(request, 'main/index.html', {'cats': cats})


def about(request): #метод страницы о нас
    cats = Category.objects.all()
    return render(request, 'main/about.html', {'cats': cats})


def post_home(request): #метод страницы с просмотром постов
    post = Posts.objects.all() #обращение к таблицам БД, получение всех объектов из соответствующих таблиц
    cats = Category.objects.all()

    data = { #словарь, хранящий в себе определённые данные из БД
        'post': post,
        'cats': cats
    }
    return render(request, 'main/post_home.html', data)


@login_required
def create(request): #метод создания поста
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_home')
        else:
            error = 'Форма была неверной'

    form = PostsForm()
    cats = Category.objects.all()
    author = request.user
    data = {
        'cats': cats,
        'form': form,
        'error': error,
        'author': author
    }

    return render(request, 'main/create.html', data)


def post_author(request, profile_id): #метод профиля пользователя
    user = User.objects.get(id=profile_id)
    post = Posts.objects.filter(author=user)
    cats = Category.objects.all()
    profile = get_object_or_404(Profile, pk=profile_id)

    data = {
        'post': post,
        'cats': cats,
        'profile': profile
    }
    return render(request, 'main/user-detail.html', data)


def registration(request): #метод регистрации на сайте
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'main/registration.html', {'form': form})


def show_category(request, cat_id): #метод просмотра категорий
    post = Posts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    data = {
        'post': post,
        'cats': cats,
    }
    return render(request, 'main/post_home.html', data)


@login_required
def show_post(request, post_id): #метод просмотра поста
    error = ''

    form = CommentsForm()
    post = get_object_or_404(Posts, pk=post_id)
    cats = Category.objects.all()
    comm = Comments.objects.all()

    data = {
        'post': post,
        'cats': cats,
        'comm': comm,
        'error': error,
        'form': form
    }

    return render(request, 'main/details_view.html', data)


def edit(request):
    error = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверные данные'

    form = ProfileForm()
    cats = Category.objects.all()
    data = {
        'cats': cats,
        'form': form,
        'error': error
    }

    return render(request, 'main/edit_profile.html', data)


@login_required
def cAdd(request): #функция написания комментария
    if request.method == 'POST':
        text = request.POST.get('text')
        idp = request.POST.get('id')
        content = Comments.objects.create(auth=request.user, post_id=int(idp), text=text)
        dict = {
            'text': text,
            'id': idp,
        }
        return JsonResponse(dict)


