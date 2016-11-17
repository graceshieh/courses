from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description

# Create your views here.
def index(request): 
	course = Course.objects.all()
	description = Description.objects.all()
	# print description
	context = {
		'course': course,
		'description': description
	}
	return render(request, 'courses/index.html', context)

def course(request): 
	course = Course.objects.create(name = request.POST['name'])
	Description.objects.create(course = course, description= request.POST['description'])
	return redirect('/')

def remove(request, id):
	course = Course.objects.get(id=id)
	description = Description.objects.get(course=course)
	context = {
		'course': course,
		'description': description
	}
	return render(request, 'courses/delete.html', context)

def delete(request, id): 
	deleteCourse = Course.objects.get(id=id)
	deleteDescrip = Description.objects.get(course=deleteCourse)
	deleteDescrip.delete()
	deleteCourse.delete() 
	return redirect('/')