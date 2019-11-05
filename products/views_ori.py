from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ChairForm, RawProductForm
from .models import Chair
# Create your views here.

def chair_list_view(request):
	queryset = Chair.objects.all() # list of objects
	context = {
		"object_list": queryset
	}
	return render (request, "products/chair_list.html", context)


def chair_delete_view(request, my_id):
	obj = get_object_or_404(Chair, id=my_id)
	#POST request
	if request.method == "POST":
		#confirming delete
		obj.delete()
		return redirect('../../');
	context = {
		"object": obj
	}
	return render (request, "products/chair_delete.html", context)


def dynamic_lookup_view(request, my_id):
	#obj = Chair.objects.get(id=my_id)
	#obj = get_object_or_404(Chair, id=my_id)
	try:
		obj = Chair.objects.get(id=my_id)
	except Chair.DoesNotExist:
		raise Http404
	context = {
		"object": obj
	}
	return render (request, "products/chair_detail.html", context)

def render_initial_data (request):
	initial_data = {
		'title': "My awesome title"
	}
	obj = Chair.objects.get(id=2)
	form = ChairForm(request.POST or None, instance=obj) #initial=initial_data
	if form.is_valid():
		form.save()
	context = {'form': form}
	return render (request, "products/chair_create.html", context)

# def chair_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			#now the data is good
# 			print(my_form.cleaned_data)
# 			Chair.objects.create(**my_form.cleaned_data)
# 		else:
# 			print (my_form.errors)
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "products/chair_create.html", context)

# def chair_create_view(request):
# 	print(request.GET)
#	print (request.POST)
#	if request.method == "POST":
#		my_new_title = request.POST.get('title')
#		print (my_new_title)
#		#Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/chair_create.html", context)


def chair_create_view(request):
	form = ChairForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ChairForm()
	context = {
		'form': form
	}

	return render(request, "products/chair_create.html", context)


def chair_detail_view(request):
    obj = Chair.objects.get(id=1)
    # context = {
    #     'title': obj.Title,
    #     'description': obj.Description,
    #     'price': obj.Price
    # }
    context = {
    	'object': obj
    }

    return render(request, "products/chair_detail.html", context)

