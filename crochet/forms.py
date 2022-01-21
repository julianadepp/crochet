from django import forms
from .models import Gauge, Hook, Pattern, Stitch, Yarn

class HookForm(forms.ModelForm):
    class Meta:
        model = Hook
        fields = ('size', 'hook_image')

class StitchForm(forms.ModelForm):
    class Meta:
        model = Stitch
        fields = ('name', 'description', 'pattern_code', 'instructions', 'notes', 'related_stitches', 'stitch_image')

class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = ('nickname', 'weight_description', 'brand', 'material', 'weight', 'notes', 'suggested_hooks', 'yarn_image')

class GaugeForm(forms.ModelForm):
    class Meta:
        model = Gauge
        fields = ('title', 'hook', 'stitch', 'yarn', 'number_of_stitches', 'notes', 'gauge_image')

class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ('name', 'hook', 'stitches', 'yarn', 'gauge', 'description', 'instructions', 'notes', 'pattern_image')