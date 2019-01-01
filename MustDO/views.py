from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(
                request, ('The Must_DO has been added to the List'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('The Must_DO has been Deleted'))
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = True
    item.save()
    messages.success(request, ('Congrats!! You are grate...keep going'))
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = False
    item.save()
    messages.success(request, ('You have to work more for this Goal'))
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("The Must_Do has been Edited"))
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
