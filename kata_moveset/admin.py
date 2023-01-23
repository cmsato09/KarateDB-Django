from django.contrib import admin
from .models import Kata, Stance, Move, Technique, TechniqueToMove


@admin.register(Kata)
class KataAdmin(admin.ModelAdmin):
    list_display = ['name', 'series', 'hiragana', 'kanji']
    search_fields = ['name', 'series']
    list_filter = ['series']
    ordering = ['pk']


@admin.register(Stance)
class StanceAdmin(admin.ModelAdmin):
    list_display = ['stance_name', 'hiragana', 'kanji']
    search_fields = ['stance_name']
    ordering = ['pk']


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ['technique_name', 'technique_type', 'hiragana', 'kanji']
    search_fields = ['technique_name', 'technique_type']
    list_filter = ['technique_type']
    ordering = ['pk', 'technique_type']


admin.site.register(Move)
admin.site.register(TechniqueToMove)
