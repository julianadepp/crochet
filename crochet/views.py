from django.shortcuts import render
from .models import Hook
# Create your views here.
def hook_list(req):
    hooks = Hook.objects.all()
    return render(req, 'crochet/hook_list.html', {'hooks': hooks})