from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from post import views

urlpatterns = [
    path('',views.index,name='index'),
    path('kacik-kulturalny/',views.kacik,name='kacik-kulturalny'),
    path('offtop/',views.offtop,name='offtop'),
    path('cv/',TemplateView.as_view(template_name="post/cv.html"),name='cv'),
    path('<int:post_id>/', views.detail,name='detail'),
]
