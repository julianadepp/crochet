from urllib import request
from django.shortcuts import render, redirect
from .models import Hook, Stitch, Yarn
from .forms import HookForm, StitchForm, YarnForm
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

def stitch_list(req):
    stitches = Stitch.objects.all()
    return render(req, 'crochet/stitch_list.html', {'stitches': stitches})

def stitch_info(req, pk):
    stitch = Stitch.objects.get(id=pk)
    return render(req, 'crochet/stitch_info.html', {'stitch': stitch})

def stitch_create(req):
    if req.method == 'POST':
        form = StitchForm(req.POST, req.FILES)
        if form.is_valid():
            stitch = form.save()
            return redirect('stitch_info', pk=stitch.pk)
    else:
        form = StitchForm()
    return render(req, 'crochet/stitch_form.html', {'form': form})
    
def stitch_update(req, pk):
    stitch = Stitch.objects.get(pk=pk)
    if req.method == 'POST':
        form = StitchForm(req.POST, req.FILES, instance=stitch)
        if form.is_valid():
            stitch = form.save()
            return redirect('stitch_info', pk=stitch.pk)
    else:
        form = StitchForm(instance=stitch)
    return render(req, 'crochet/stitch_form.html', {'form': form})

def stitch_delete(req, pk):
    Stitch.objects.get(pk=pk).delete()
    return redirect('stitch_list')

#------YARN CRUD------------------------------

def yarn_list(req):
    yarns = Yarn.objects.all()
    return render(req, 'crochet/yarn_list.html', {'yarns': yarns})

def yarn_info(req, pk):
    yarn = Yarn.objects.get(id=pk)
    return render(req, 'crochet/yarn_info.html', {'yarn': yarn})

def yarn_create(req):
    if req.method == 'POST':
        form = YarnForm(req.POST)
        if form.is_valid():
            yarn = form.save()
            return redirect('yarn_info', pk=yarn.pk)
    else:
        form = YarnForm()
    return render(req, 'crochet/yarn_form.html', {'form': form})
    
def yarn_update(req, pk):
    yarn = Yarn.objects.get(pk=pk)
    if req.method == 'POST':
        form = YarnForm(req.POST, instance=yarn)
        if form.is_valid():
            yarn = form.save()
            return redirect('yarn_info', pk=yarn.pk)
    else:
        form = YarnForm(instance=yarn)
    return render(req, 'crochet/yarn_form.html', {'form': form})

def yarn_delete(req, pk):
    Yarn.objects.get(pk=pk).delete()
    return redirect('yarn_list')

#------GAUGE CRUD-----------------------------



#------PATTERN CRUD---------------------------
