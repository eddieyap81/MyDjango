from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
# Create your views here.

class CourseObjectMixin(object):
	model = Course
	lookup = 'id'

	def get_object(self):
		id = self.kwargs.get(self.lookup)
		obj=None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj

class CourseDeleteView(CourseObjectMixin, View):
	template_name = 'courses/course_delete.html' #DetailView

	def get(self, request, id=None, *args, **kwargs):  ## to get data from server
		#GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id = None, *args, **kwargs):  ## to get data from server
		#POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect('/courses/')
		return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
	template_name = 'courses/course_update.html' #DetailView

	def get(self, request, *args, **kwargs):  ## to get data from server
		#GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):  ## to get data from server
		#POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

class CourseCreateView(View):
	template_name = 'courses/course_create.html' #DetailView
	def get(self, request, *args, **kwargs):  ## to get data from server
		#GET method
		form = CourseModelForm()
		context = {'form': form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):  ## to get data from server
		#POST method
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm()
		context = {'form': form}
		return render(request, self.template_name, context)

class CourseListView(View):
	template_name = 'courses/course_list.html'
	queryset = Course.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context = {'object_list':self.get_queryset()}
		return render(request, self.template_name, context)

class MyListView(CourseListView):
	queryset = Course.objects.filter(id=1)

#BASE VIEW Class = VIEW
class CourseView(CourseObjectMixin, View):
	template_name = 'courses/course_detail.html' #DetailView
	def get(self, request, id=None, *args, **kwargs):  ## to get data from server
		#GET method
		context = {'object': self.get_object()}
		return render(request, self.template_name, context)

	# def post(request, *args, **kwargs): ##to submit form to server
	# 	return render(request, 'about.html', {})

# class CourseView(View):
# 	template_name = 'about.html'
# 	def get(self, request, *args, **kwargs):  ## to get data from server
# 		#GET method
# 		return render(request, self.template_name, {})

# 	# def post(request, *args, **kwargs): ##to submit form to server
# 	# 	return render(request, 'about.html', {})


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
	print(request.method)
	return render(request, 'about.html', {})
