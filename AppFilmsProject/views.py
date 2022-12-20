from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Film, Category
from .forms import ProjectFilmsForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy


def index(request):
    films = Film.objects.all()
    return render(request, 'AppFilmsProject/index.html', {'films': films})


def add(request):
    if Category.objects.all().count() == 0:
        Category.objects.create(genre='Комедия')
        Category.objects.create(genre='Триллер')
        Category.objects.create(genre='Мультфильмы')
    if request.method == 'POST':
        film = Film()
        film.first_date = request.POST.get('first_date')
        film.actors = request.POST.get('actors')
        film.name = request.POST.get('name')
        film.show_date = request.POST.get('show_date')
        film.genre_id = request.POST.get('category')
        film.save()
        return redirect('main')
    else:
        categories = Category.objects.all()
        FormFilmsProject = ProjectFilmsForm()
        return render(request, 'AppFilmsProject/add.html', {'form': FormFilmsProject, 'categories': categories})


def edit(request, id):
    try:
        film = Film.objects.get(id=id)
        if request.method == 'POST':
            film.name = request.POST.get('name')
            film.genre_id = request.POST.get('category')
            film.first_date = request.POST.get('first_date')
            film.actors = request.POST.get('actors')
            film.show_date = request.POST.get('show_date')
            film.save()
            return redirect('main')
        else:
            categories = Category.objects.all()
            return render(request, 'AppFilmsProject/edit.html', {'film': film, 'categories': categories})
    except Film.DoesNotExist:
        return HttpResponseNotFound('Фильм не найден')


def delete(request, id):
    try:
        film = Film.objects.get(id=id)
        film.delete()
        return redirect('main')
    except film.DoesNotExist:
        return HttpResponseNotFound('Фильм не найден')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
