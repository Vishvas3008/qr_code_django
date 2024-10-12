from django.contrib import admin
from members.models import Member, Total
from django.http import HttpResponse
from django.urls import reverse
import os
import qrcode
import cloudinary
import cloudinary.uploader
import io

class YourModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Save the object first
        super().save_model(request, obj, form, change)

        if not change:  # If this is a new object
            total = Total.objects.first()
            total.total += 1
            total.save()

            # Get the domain from environment variables
            domain = os.getenv('DOMAIN', "https://qr-code-django.vercel.app/.vercel.app")

            # Create the QR code
            qr_data = f"{domain}/admin/members/member/{total.total}/change/"
            img = qrcode.make(qr_data)

            # Upload the QR code directly to Cloudinary using configuration from Total model
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format='PNG')
            img_byte_array.seek(0)

            # Retrieve Cloudinary configuration
            cloudinary.config(
                cloud_name=total.cloudinary_cloud_name,
                api_key=total.cloudinary_api_key,
                api_secret=total.cloudinary_api_secret,
                secure=True
            )

            # Use the firstname and lastname for the public_id
            public_id = f"{getattr(obj, 'firstname')}_{getattr(obj, 'lastname')}_{total.total}"
            upload_result = cloudinary.uploader.upload(img_byte_array, public_id=public_id)
            
            # Store the URL in the object
            obj.qr_code_url = upload_result["secure_url"]  
            obj.save()  # Save the object again to update with the QR code URL

    def response_add(self, request, obj, post_url_continue=None):
        # Redirect to the newly uploaded QR code image link
        if hasattr(obj, 'qr_code_url'):
            script = f"""
                <script type="text/javascript">
                    window.open('{obj.qr_code_url}', '_blank');
                     window.location.href = '{'/admin/members/member/'}';  // Redirect to the member list or desired page
                </script>
            """
            return HttpResponse(script)  # Redirect to the image URL
        return super().response_add(request, obj, post_url_continue)

# Register models
admin.site.register(Member, YourModelAdmin)
admin.site.register(Total)
