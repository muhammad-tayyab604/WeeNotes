from django.contrib import admin
from .models import Notes, Contact

@admin.register(Notes)
class AdminNotes(admin.ModelAdmin):
    list_display = ['id', 'title', 'discription']
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','email', 'contactNo', 'message']