from django.contrib import admin
from add.models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title',)
    list_filter = ('is_done',)

