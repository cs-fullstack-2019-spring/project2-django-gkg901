from django.contrib import admin
from .models import postModel, relatedModel

# Register your models here.
admin.site.register(postModel)
admin.site.register(relatedModel)
