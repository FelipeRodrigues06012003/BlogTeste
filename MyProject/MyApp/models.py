from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class News(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author


class SportNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class DataRegistro(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on delete siguifica que o posts vão ser deletados se o autor foi excluido
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # adc data no post automaticamente
    update = models.DateTimeField(auto_now=True)  # Atualiza a data do post sozinho

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("MyApp:detail", kwargs={"slug": self.slug})
