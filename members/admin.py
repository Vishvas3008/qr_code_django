from django.contrib import admin
from members.models import Member,Total
from django.urls import reverse
import qrcode
import random
class YourModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        
        data=super().save_model(request, obj, form, change)
        

        print("hdhd",getattr(obj, "firstname")) 
        existing_obj = self.get_object(request, obj.pk)
        changes = {}
        for field in form.changed_data:
                changes[field] = {
                    'old': getattr(existing_obj, field),
                    'new': getattr(obj, field),
                }  
        print(changes)
        if not change:  # This means it's a new object
            total = Total.objects.all()[0]
            total.total=total.total+1
            total.save()
            print(total)
            # print('hey',self, request, obj, form, change)
            img = qrcode.make('http://127.0.0.1:8000/admin/members/member/'+ str(total.total) +'/change/')
            type(img)  # qrcode.image.pil.PilImage
            img.save(getattr(obj, "firstname") + "_" + getattr(obj, "lastname") + ".png")
            # endpoint_url = 'http://your-endpoint-url.com/api/your-endpoint/'
            # response = requests.post(endpoint_url, json={'id': obj.id, 'other_data': obj.other_field})
            # Handle the response if needed

admin.site.register(Member, YourModelAdmin)

admin.site.register(Total)
