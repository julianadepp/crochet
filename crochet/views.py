from urllib import request
from django.shortcuts import render, redirect
from .models import Hook
from .forms import HookForm
# Create your views here.

#------HOOK CRUD------------------------------

def hook_list(req):
    hooks = Hook.objects.all()
    return render(req, 'crochet/hook_list.html', {'hooks': hooks})

def hook_info(req, pk):
    hook = Hook.objects.get(id=pk)
    return render(req, 'crochet/hook_info.html', {'hook': hook})

def hook_create(req):
    if req.method == 'POST':
        form = HookForm(req.POST, req.FILES)
        if form.is_valid():
            hook = form.save()
            return redirect('hook_info', pk=hook.pk)
    else:
        form = HookForm()
    return render(req, 'crochet/hook_form.html', {'form': form})

def hook_update(req, pk):
    hook = Hook.objects.get(pk=pk)
    if req.method == 'POST':
        form = HookForm(req.POST, req.FILES, instance=hook)
        if form.is_valid():
            hook = form.save()
            return redirect('hook_info', pk=hook.pk)
    else:
        form = HookForm(instance=hook)
    return render(req, 'crochet/hook_form.html', {'form': form})

def hook_delete(req, pk):
    Hook.objects.get(pk=pk).delete()
    return redirect('hook_list')

#------STITCH CRUD----------------------------



#------YARN CRUD------------------------------



#------GAUGE CRUD-----------------------------



#------PATTERN CRUD---------------------------
