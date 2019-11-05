from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	#sucess_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
	#	return '/'

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all() # <blog>/<modelname>_list.html

# class ArticleDetailView(DetailView): ## if use 'pk' as id in urls.py
# 	template_name = 'articles/article_detail.html'
# 	queryset = Article.objects.all() #select all
# 	queryset = Article.objects.filter(id_gt=1)  # filter greater than 1

class ArticleDetailView(DetailView): ## if use 'id' as id in urls.py
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	#sucess_url = '/'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)
		
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
	#	return '/'

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	#queryset = Article.objects.all()
	#sucess_url = '/'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
   		return reverse("blog:article-list") 

	#def get_success_url(self):
	#	return '/'