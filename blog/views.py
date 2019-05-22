from django.shortcuts import render

posts = [

    {
        'author': 'monk',
        'title': 'Blog post 1',
        'content': 'My first blog post.',
        'date_posted': 'May 18, 2019'
    },
    {
        'author': 'Joy',
        'title': 'Got milk?',
        'content': 'I want milk!',
        'date_posted': 'May 19, 2019'
    }

]


def home(request):
    context = {
        'posts': posts,
        'title': 'Blogs-Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Django-Blog'})
