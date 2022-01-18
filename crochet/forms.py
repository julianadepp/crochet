from django import forms
from .models import Hook, Stitch, Yarn

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