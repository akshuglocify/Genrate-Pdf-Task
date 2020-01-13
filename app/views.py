from django.shortcuts import render
from app.forms import UserProfileForm, ProfilePictureForm
from django.shortcuts import render, redirect
import pdfkit as pdf
from .models import ProfilePicture , UserProfile
from .utils import Render
from django.utils import timezone
# Create your views here.
def userprofile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/image')
    form = UserProfileForm()
    return render(request , 'form_1.html', {'form': form })


def profile(request):
    if request.method == "POST":
        form = ProfilePictureForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/pdf')
    form = ProfilePictureForm()
    return render(request , 'form2.html', {'form': form })

def pdfview(request):
    userprofile = UserProfile.objects.all().order_by('-id')[0]
    image = ProfilePicture.objects.all().order_by('-id')[0]
    today = timezone.now()
    params = {
            'today': today,
            'profile':userprofile,
            'image': image.profile_pic.url,
            'request': request
        }
    return Render.render('form3.html', params)