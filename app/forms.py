from django import forms
from .models import ProfilePicture, UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = '__all__'