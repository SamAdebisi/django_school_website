from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogSearchResultsListView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_search/', BlogSearchResultsListView.as_view(), name='blog_search_results'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
