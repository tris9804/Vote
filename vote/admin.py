from django.contrib import admin

from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'last_name', 'first_name', 
    )


