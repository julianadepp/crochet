from urllib import request
#from django.shortcuts import render, redirect
from .models import Gauge, Hook, Pattern, Stitch, Yarn
#from .forms import GaugeForm, HookForm, PatternForm, StitchForm, YarnForm

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import GaugeSerializer, HookSerializer, PatternSerializer, YarnSerializer, StitchSerializer


# Create your views here.

#------Hook Serializer------------------------

class HookList(generics.ListCreateAPIView):
    queryset = Hook.objects.all()
    serializer_class = HookSerializer
    parser_classes = (MultiPartParser, FormParser)

class HookInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hook.objects.all()
    serializer_class = HookSerializer
    parser_classes = (MultiPartParser, FormParser)


#------Yarn Serializer------------------------

class YarnList(generics.ListCreateAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

class YarnInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

#------Stitch Serializer----------------------

class StitchList(generics.ListCreateAPIView):
    queryset = Stitch.objects.all()
    serializer_class = StitchSerializer
    parser_classes = (MultiPartParser, FormParser)


class StitchInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stitch.objects.all()
    serializer_class = StitchSerializer
    parser_classes = (MultiPartParser, FormParser)


#------Gauge Serializer----------------------

class GaugeList(generics.ListCreateAPIView):
    queryset = Gauge.objects.all()
    serializer_class = GaugeSerializer
    parser_classes = (MultiPartParser, FormParser)


class GaugeInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gauge.objects.all()
    serializer_class = GaugeSerializer
    parser_classes = (MultiPartParser, FormParser)

    
#------Pattern Serializer----------------------

class PatternList(generics.ListCreateAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    parser_classes = (MultiPartParser, FormParser)


class PatternInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    parser_classes = (MultiPartParser, FormParser)


#------HOOK CRUD------------------------------

# def hook_list(req):
#     hooks = Hook.objects.all()
#     return render(req, 'crochet/hook_list.html', {'hooks': hooks})

# def hook_info(req, pk):
#     hook = Hook.objects.get(id=pk)
#     return render(req, 'crochet/hook_info.html', {'hook': hook})

# def hook_create(req):
#     if req.method == 'POST':
#         form = HookForm(req.POST, req.FILES)
#         if form.is_valid():
#             hook = form.save()
#             return redirect('hook_info', pk=hook.pk)
#     else:
#         form = HookForm()
#     return render(req, 'crochet/hook_form.html', {'form': form})

# def hook_update(req, pk):
#     hook = Hook.objects.get(pk=pk)
#     if req.method == 'POST':
#         form = HookForm(req.POST, req.FILES, instance=hook)
#         if form.is_valid():
#             hook = form.save()
#             return redirect('hook_info', pk=hook.pk)
#     else:
#         form = HookForm(instance=hook)
#     return render(req, 'crochet/hook_form.html', {'form': form})

# def hook_delete(req, pk):
#     Hook.objects.get(pk=pk).delete()
#     return redirect('hook_list')

#------STITCH CRUD----------------------------

# def stitch_list(req):
#     stitches = Stitch.objects.all()
#     return render(req, 'crochet/stitch_list.html', {'stitches': stitches})

# def stitch_info(req, pk):
#     stitch = Stitch.objects.get(id=pk)
#     return render(req, 'crochet/stitch_info.html', {'stitch': stitch})

# def stitch_create(req):
#     if req.method == 'POST':
#         form = StitchForm(req.POST, req.FILES)
#         if form.is_valid():
#             stitch = form.save()
#             return redirect('stitch_info', pk=stitch.pk)
#     else:
#         form = StitchForm()
#     return render(req, 'crochet/stitch_form.html', {'form': form})
    
# def stitch_update(req, pk):
#     stitch = Stitch.objects.get(pk=pk)
#     if req.method == 'POST':
#         form = StitchForm(req.POST, req.FILES, instance=stitch)
#         if form.is_valid():
#             stitch = form.save()
#             return redirect('stitch_info', pk=stitch.pk)
#     else:
#         form = StitchForm(instance=stitch)
#     return render(req, 'crochet/stitch_form.html', {'form': form})

# def stitch_delete(req, pk):
#     Stitch.objects.get(pk=pk).delete()
#     return redirect('stitch_list')

#------YARN CRUD------------------------------

# def yarn_list(req):
#     yarns = Yarn.objects.all()
#     return render(req, 'crochet/yarn_list.html', {'yarns': yarns})

# def yarn_info(req, pk):
#     yarn = Yarn.objects.get(id=pk)
#     return render(req, 'crochet/yarn_info.html', {'yarn': yarn})

# def yarn_create(req):
#     if req.method == 'POST':
#         form = YarnForm(req.POST)
#         if form.is_valid():
#             yarn = form.save()
#             return redirect('yarn_info', pk=yarn.pk)
#     else:
#         form = YarnForm()
#     return render(req, 'crochet/yarn_form.html', {'form': form})
    
# def yarn_update(req, pk):
#     yarn = Yarn.objects.get(pk=pk)
#     if req.method == 'POST':
#         form = YarnForm(req.POST, instance=yarn)
#         if form.is_valid():
#             yarn = form.save()
#             return redirect('yarn_info', pk=yarn.pk)
#     else:
#         form = YarnForm(instance=yarn)
#     return render(req, 'crochet/yarn_form.html', {'form': form})

# def yarn_delete(req, pk):
#     Yarn.objects.get(pk=pk).delete()
#     return redirect('yarn_list')

#------GAUGE CRUD-----------------------------

# def gauge_list(req):
#     gauges = Gauge.objects.all()
#     return render(req, 'crochet/gauge_list.html', {'gauges': gauges})

# def gauge_info(req, pk):
#     gauge = Gauge.objects.get(id=pk)
#     return render(req, 'crochet/gauge_info.html', {'gauge': gauge})

# def gauge_create(req):
#     if req.method == 'POST':
#         form = GaugeForm(req.POST, req.FILES)
#         if form.is_valid():
#             gauge = form.save()
#             return redirect('gauge_info', pk=gauge.pk)
#     else:
#         form = GaugeForm()
#     return render(req, 'crochet/gauge_form.html', {'form': form})
    
# def gauge_update(req, pk):
#     gauge = Gauge.objects.get(pk=pk)
#     if req.method == 'POST':
#         form = GaugeForm(req.POST, req.FILES, instance=gauge)
#         if form.is_valid():
#             gauge = form.save()
#             return redirect('gauge_info', pk=gauge.pk)
#     else:
#         form = GaugeForm(instance=gauge)
#     return render(req, 'crochet/gauge_form.html', {'form': form})

# def gauge_delete(req, pk):
#     Gauge.objects.get(pk=pk).delete()
#     return redirect('gauge_list')

#------PATTERN CRUD---------------------------

# def pattern_list(req):
#     patterns = Pattern.objects.all()
#     return render(req, 'crochet/pattern_list.html', {'patterns': patterns})

# def pattern_info(req, pk):
#     pattern = Pattern.objects.get(id=pk)
#     return render(req, 'crochet/pattern_info.html', {'pattern': pattern})

# def pattern_create(req):
#     if req.method == 'POST':
#         form = PatternForm(req.POST, req.FILES)
#         if form.is_valid():
#             pattern = form.save()
#             return redirect('pattern_info', pk=pattern.pk)
#     else:
#         form = PatternForm()
#     return render(req, 'crochet/pattern_form.html', {'form': form})
    
# def pattern_update(req, pk):
#     pattern = Pattern.objects.get(pk=pk)
#     if req.method == 'POST':
#         form = PatternForm(req.POST, req.FILES, instance=pattern)
#         if form.is_valid():
#             pattern = form.save()
#             return redirect('pattern_info', pk=pattern.pk)
#     else:
#         form = PatternForm(instance=pattern)
#     return render(req, 'crochet/pattern_form.html', {'form': form})

# def pattern_delete(req, pk):
#     Pattern.objects.get(pk=pk).delete()
#     return redirect('pattern_list')