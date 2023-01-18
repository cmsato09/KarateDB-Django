from django.contrib import admin
from .models import Kata, Stance, Move, Technique

admin.site.register(Kata)
admin.site.register(Stance)
admin.site.register(Move)
admin.site.register(Technique)
