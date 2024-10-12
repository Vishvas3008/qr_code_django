from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Total
from .forms import CloudinaryConfigForm
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def cloudinary_config_view(request):
    # Get the first Total object or create one if it doesn't exist
    total, created = Total.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = CloudinaryConfigForm(request.POST, instance=total)
        if form.is_valid():
            form.save()  # Save the form data to the Total model
            return redirect('your_success_url')  # Redirect to a success page
    else:
        form = CloudinaryConfigForm(instance=total)

    return render(request, 'cloudinary_config.html', {'form': form})