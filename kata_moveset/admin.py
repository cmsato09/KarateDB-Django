from django.contrib import admin
from .models import Kata, Stance, Move, Technique, TechniqueToMove

admin.site.register(Kata)
admin.site.register(Stance)
admin.site.register(Move)

class TechniqueAdmin(admin.ModelAdmin):
    #list_display = ('id', 'biteid')
    search_fields = ('technique_name',)

admin.site.register(Technique, TechniqueAdmin)
admin.site.register(TechniqueToMove)
