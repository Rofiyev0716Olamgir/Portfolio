from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from article.models import Article, Category, Tag, Comments
from .forms import CommentForm


def article_detail_view(request, slug):
    all_articles = Article.objects.all()
    popular_articles = Article.objects.order_by('-id')[:3]
    article = get_object_or_404(Article, slug=slug)
    q = request.GET.get('q')
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    categories = Category.objects.all()
    category = request.GET.get('category')
    comments = Comments.objects.filter(article_id=article.id, top_level_comment_id__isnull=True)
    cid = request.GET.get('cid')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            obj.parent_id = cid
            obj.save()
            return redirect(f'.#comments-{cid}')
    if q:
        all_articles = all_articles.filter(title__icontains=q)
        return redirect('/archive/?q='+q)
    if tag:
        all_articles = all_articles.filter(tags__title__exact=tag)
    if category:
        all_articles = all_articles.filter(tags__title__exact=category)
    ctx = {
        'article': article,
        'all_articles': all_articles,
        'tags': tags,
        'categories': categories,
        'form': form,
        'popular_articles': popular_articles,
        'comments': comments,
    }
    return render(request, 'article/single-blog.html', ctx)


def home_view(request):
    category = request.GET.get('category')
    categories = Category.objects.all()
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    tags = Tag.objects.all()
    objects = Article.objects.all()
    articles_list = Article.objects.order_by('-id')[:6]
    object_list = Article.objects.order_by('-id')[3:]
    last_page = Paginator(object_list, 3)
    last_object = last_page.get_page('page')
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 3)
    page_obj = paginator.get_page('page')
    if q:
        articles_list = articles.filter(title__icontains=q)
    if category:
        articles = articles.filter(category__title__exact=category)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    ctx = {
        'objects': objects,
        'all_list': articles,
        'articles': page_obj,
        'object_list': last_object,
        'article_list': articles_list,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'article/index.html', ctx)


def archive_view(request):
    category = request.GET.get('cat')
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    all_articles = Article.objects.order_by('-id')
    popular_articles = Article.objects.order_by('-id')[:3]
    if q:
        all_articles = all_articles.filter(title__icontains=q)
    if category:
        all_articles = all_articles.filter(category__title__exact=category)
    if tag:
        all_articles = all_articles.filter(tags__title__exact=tag)
    ctx = {
        'tag': tags,
        'categories': categories,
        'articles': all_articles,
        'popular_articles': popular_articles,
        'all_articles': all_articles

    }
    return render(request, 'article/archive.html', ctx)


