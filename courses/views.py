from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from django.contrib.auth.mixins import (
    PermissionRequiredMixin, PermissionDenied,
)
from django.urls import reverse_lazy
from .models import Course, Instructor


class CoursePageView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/course_list.html'


class CourseDetailPageView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'


class CourseCreatePageView(PermissionRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/course_create.html'
    fields = (
        'name', 'description', 'details',
        'curriculum', 'track',
        'cross_price', 'discount_price', 'cover'
    )
    permission_required = 'courses.special_status'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseUpdatePageView(PermissionRequiredMixin, UpdateView):
    model = Course
    template_name = 'courses/course_update.html'
    fields = (
        'name', 'description', 'details',
        'curriculum', 'track',
        'cross_price', 'discount_price', 'cover'
    )
    permission_required = 'courses.special_status'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CourseDeletePageView(PermissionRequiredMixin, DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('course_list')
    permission_required = 'courses.special_status'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class InstructorListPage(ListView):
    model = Instructor
    template_name = 'courses/course_detail.html'


class InstructorCreatePage(PermissionRequiredMixin, CreateView):
    model = Instructor
    template_name = 'courses/course_create.html'
    fields = (
        'role', 'body',
    )
    permission_required = 'courses.special_status'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class InstructorUpdatePage(PermissionRequiredMixin, UpdateView):
    model = Instructor
    template_name = 'courses/course_update.html'
    fields = (
        'role', 'body',
    )
    permission_required = 'courses.special_status'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class InstructorDeletePage(PermissionRequiredMixin, DeleteView):
    model = Instructor
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('course_list')
    permission_required = 'courses.special_status'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
