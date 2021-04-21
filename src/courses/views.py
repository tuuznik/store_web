from django.shortcuts import get_object_or_404, render, redirect
from .models import Course
from .forms import CourseModelForm
from django.views.generic import View
from django.urls import reverse


class CourseObjectMixin(object):
    model = Course
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_create.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        form = CourseModelForm(request.POST)
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                context["object"] = obj
                context["form"] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = "courses/course_create.html"

    def get(self, request, id=None, *args, **kwargs):
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/courses_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context= {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class CourseDetailView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
