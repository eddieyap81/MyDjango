from django.shortcuts import render, get_object_or_404, redirect
from .forms import ChairForm
from .models import Chair

def chair_create_view(request):
	form = ChairForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ChairForm()
	context = {
		'form': form
	}
	return render(request, "products/chair_create.html", context)

def chair_update_view(request, my_id):
	obj = get_object_or_404(Chair, id=my_id)
	form = ChairForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/chair_create.html", context)

def chair_detail_view(request, my_id):
	obj = get_object_or_404(Chair, id=my_id)
	context = {
		'object': obj
	}
	return render(request, "products/chair_detail.html", context)


def chair_list_view(request):
	queryset = Chair.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "products/chair_list.html", context)

def chair_delete_view(request, my_id):
	obj = get_object_or_404(Chair, id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		'object': obj
	}
	return render(request, "products/chair_delete.html", context)

# def render_initial_data (request):
# 	initial_data = {
# 		'title': "My awesome title"
# 	}
# 	obj = Chair.objects.get(id=2)
# 	form = ChairForm(request.POST or None, instance=obj) #initial=initial_data
# 	if form.is_valid():
# 		form.save()
# 	context = {'form': form}
# 	return render (request, "products/chair_create.html", context)