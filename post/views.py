from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from post.models import Post
from django.db.models import Q

# Create your views here.

def index(request):
    posts_lst = Post.objects.order_by('-dt').filter(Q(posttag1='all') | Q(posttag1='tech'))
    posts_dckt = {'post':posts_lst}
    return render(request,'post/home.html',context=posts_dckt)

def kacik(request):
    posts_lst = Post.objects.order_by('-dt').filter(Q(posttag1='all') | Q(posttag1='kultura'))
    posts_dckt = {'post':posts_lst}
    return render(request,'post/home.html',context=posts_dckt)

def offtop(request):
    posts_lst = Post.objects.order_by('-dt').filter(Q(posttag1='all') | Q(posttag1='offtop'))
    posts_dckt = {'post':posts_lst}
    return render(request,'post/home.html',context=posts_dckt)

def detail(request, post_id):
    posts_lst = Post.objects.filter(id=post_id)
    posts_dckt = {'post':posts_lst}
    post_id=post_id-1
    if post_id > 0:
        bfr_post = Post.objects.filter(id=post_id).values('id')
        posts_dckt['bfr'] = bfr_post
    post_id=post_id+2
    if Post.objects.filter(id=post_id).exists():
        nxt_post = Post.objects.filter(id=post_id).values('id')
        posts_dckt['nxt'] = nxt_post
    return render(request,'post/detail.html',context=posts_dckt)
