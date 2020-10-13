from django.contrib import admin
from .models import user_model, result_model


admin.site.register(user_model)
admin.site.register(result_model)
