from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    # PermissionRequiredMixin,
    PermissionDenied,
)
from django.db.models import Q

from .models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'
    login_url = 'account_login'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blogs/blog_detail.html'
    login_url = 'account_login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blogs/blog_create.html'
    fields = ('title', 'body')
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'body')
    template_name = 'blogs/blog_update.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blogs/blog_list')
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogSearchResultsListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blog.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
            | Q(author__icontains=query)
        )
