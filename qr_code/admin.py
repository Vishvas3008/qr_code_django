from django.contrib import admin
from members.models import Member

admin.site.register(Member)

class YourModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('members/css/admin.css',)
        }
