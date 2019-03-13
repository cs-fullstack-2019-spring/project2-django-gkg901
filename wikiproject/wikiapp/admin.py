from django.contrib import admin
from .models import PostModel, RelatedModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(RelatedModel)
