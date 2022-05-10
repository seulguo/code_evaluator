from django.contrib import admin

# Register your models here.
from evaluator.models import Classroom


@admin.register(Classroom)
class Classroom(admin.ModelAdmin):

    list_display = ['name']