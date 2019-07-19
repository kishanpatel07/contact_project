from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','gender','info','phone')
    list_editable=('info',)
    # list_per_page=1
    list_filter=('gender','date_added')
    search_fields=('name','email','phone','gender','info')

admin.site.register(Contact,ContactAdmin)