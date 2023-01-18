from django.contrib import admin
from .models import Kata, Stances, Move, Technique

admin.site.register(Kata)
admin.site.register(Stances)
admin.site.register(Move)
admin.site.register(Technique)