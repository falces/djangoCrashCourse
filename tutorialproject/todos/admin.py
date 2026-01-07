from re import search
from django.contrib import admin
from .models import Todos, Person

admin.site.register(Person)
# admin.site.register(Todos)

@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'deadline', 'done', 'person')
    search_fields = ('title',)
    list_filter = ('priority', 'person')
    
