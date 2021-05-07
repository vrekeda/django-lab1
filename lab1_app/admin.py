from django.contrib import admin
from .models import Language, Word
# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ukrainian_name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'ukrainian_name')


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'translation', 'translate_from', 'translate_to', 'learnt', 'date')
    list_display_links = ('id', 'original', 'translation')
    search_fields = ('id', 'original', 'translation')
    # list_filter = ('learnt', 'translate_from', 'translate_to')
    list_filter = ('learnt', 'translate_from', 'translate_to')


admin.site.register(Language, LanguageAdmin)
admin.site.register(Word, WordAdmin)
