from django import forms
from .models import Hook

class HookForm(forms.ModelForm):
    class Meta:
        model = Hook
        fields = ('size', 'hook_image')