from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from django.db.models import Q
from .models import Record
from django.core.paginator import Paginator, EmptyPage
import os


def home(request):
	records = Record.objects.filter(user=request.user.id)
	if 'q' in request.GET:
		q = request.GET['q']
		records = Record.objects.filter(Q(user=request.user.id),
										(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(phone__icontains=q)
										|Q(city__icontains=q)))
	p = Paginator(records, 3)
	page_num = request.GET.get('page', 1)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)


	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Вход выполнен успешно!")
			return redirect('home')
		else:
			messages.success(request, "Ошибка входа! Повторите ещё раз")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':page})



def logout_user(request):
	logout(request)
	messages.success(request, "Выход успешно выполнен")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Регистрация успешно завершена")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Вы должны войти для просмотра данной страницы")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Запись успешно удалена")
		return redirect('home')
	else:
		messages.success(request, "Вы должны войти для удаления записи")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.instance.user = request.user
				add_record = form.save()
				messages.success(request, "Запись добавлена")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Вы должны войти для добавления записи")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, request.FILES or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Запись была отредактирована")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Вы должны войти для редактирования записи")
		return redirect('home')
