from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('car-list')
	context = {
		'form': form

	}
	return render(request, 'create.html', context)


def car_update(request, car_id):
	update = Car.objects.get(id=car_id)
	form = CarForm(instance=update)
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES, instance=update)
		if form.is_valid():
			form.save()
			return redirect('car-list')
	context = {
		'form': form,
		'update': update

	}
	return render(request, 'update.html', context)


def car_delete(request, car_id):
	delete = Car.objects.get(id=car_id)
	delete.delete()
	return redirect('car-list')