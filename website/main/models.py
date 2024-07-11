from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_admin_geomap import GeoItem


class Posts(models.Model): #пост
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Пост')
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', null=True)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts", null=True)

    def __str__(self): #метод обращения к каждому элементу таблички
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta: #класс названий для таблички (админ панель)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model): #категория
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Profile(models.Model): #пользователь
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to='profile/', blank=True, null=True)
    phone = models.CharField("Телефон", max_length=25)
    first_name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Фамилия", max_length=50, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиля"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, id=instance.id)

    @receiver
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Comments(models.Model): #комментарии
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="comments")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    text = models.CharField('Текст', max_length=1000, null=True, blank=True)
    datetime = models.DateTimeField(verbose_name="Дата", auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



class Location(models.Model): #ГИСЫ БД
    name = models.CharField(max_length=100)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта


class Location(models.Model, GeoItem):

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)
