from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from .views import *
from django.contrib.auth import views as authViews
from django.views.decorators.cache import cache_page

urlpatterns = [
    re_path(r'^$', index, name="home"),
    re_path(r'^about/', cache_page(60)(about), name="about"),
    path('post/', post_home, name="post_home"),
    path('post/create', create, name="create"),
    path('post/<int:post_id>', show_post, name='post-detail'),
    path('profile/<int:profile_id>', post_author, name='profile-detail'),
    re_path(r'^registration/', registration, name='reg'),
    re_path(r'^login/', authViews.LoginView.as_view(template_name='main/login.html'), name='user'),
    re_path(r'^exit/', authViews.LogoutView.as_view(template_name='main/index.html'), name='exit'),
    path('category/<int:cat_id>', show_category, name='category'),
    path('profile/edit', edit, name="edit"),
    path('cAdd/', csrf_exempt(cAdd), name='cAdd')
]
