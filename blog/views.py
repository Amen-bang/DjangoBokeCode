from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
import markdown

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html',context=context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context={
    	'post': post
    }
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context=context)

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context=context)

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})