from django.contrib import admin
from .models import News
# Register your models here.
#admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # здесь перечисляем, что показывать
    list_filter = ('author', 'created_at')  # фильтры справа
    search_fields = ('title', 'content')  # поиск по заголовку и тексту