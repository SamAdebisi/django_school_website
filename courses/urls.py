from django.urls import path

from .views import (
    CoursePageView, CourseDetailPageView, CourseCreatePageView,
    CourseDeletePageView, CourseUpdatePageView,
)

urlpatterns = [
    path('', CoursePageView.as_view(), name='course_list'),
    path('<uuid:pk>', CourseDetailPageView.as_view(), name='course_detail'),
    path('course_create/', CourseCreatePageView.as_view(), name='course_create'),
    path('course_update/', CourseUpdatePageView.as_view(), name='course_update'),
    path('course_delete/', CourseDeletePageView.as_view(), name='course_delete'),
]
