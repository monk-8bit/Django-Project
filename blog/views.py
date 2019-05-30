from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blogs-Home'
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # Model to query in order to create list
    model = Post
    # <app>/<model>_<viewtype>.html
    #   blog / post_list.html
    template_name = 'blog/home.html'
    # Instead of objects.attribute  -> post.attribute
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # self.request = request !!!
    model = Post
    fields = ['title', 'content']
    # Success_URL defaults to a DetailView of the Model.instance created
    # get_absolute_ url() in the Model helps CreateView redirect to
    # the DetailView of the model
    # Success_URL can be modifed to redirect to another path

    def form_valid(self, form):
        # CreateView doesn't know which User the FORM created belongs to
        # Must overide form_valid from Parent class, set owner of FORM,
        # then call Parent.form_valid()
        form.instance.author = self.request.user
        # Acces the current User <self>.<request>.<user>
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'Django-Blog'})
