#  from django.contrib import admin
from django.urls import path
#  from MyApp.views import home
from . import views

app_name = 'MyApp'

urlpatterns = [
    #  path('admin/', admin.site.urls),
    #  path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('news/', views.news, name='news'),
    path('year/<int:year>', views.news_annual, name='newsannual'),
    path('registro', views.registro, name='add'),
    path('addUser', views.addUser, name='addUser'),
    path('', views.PostListView.as_view(), name='list'),
    path("<slug:slug>/", views.PostDetailView.as_view(), name='detail'),
]
