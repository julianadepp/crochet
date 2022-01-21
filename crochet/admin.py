from django.contrib import admin
from .models import Gauge, Hook, Pattern, Stitch, Yarn
# Register your models here.
admin.site.register(Hook)
admin.site.register(Stitch)
admin.site.register(Yarn)
admin.site.register(Gauge)
admin.site.register(Pattern)
