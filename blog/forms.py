from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Post,Comment,Profile,PostOrignal


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Mandatory')
    last_name = forms.CharField(max_length=30, help_text='Mandatory')
    image = forms.ImageField(required=False)
    email = forms.EmailField(max_length=254, help_text='Mandatory.')
    birth_date = forms.DateField(help_text='Mandatory. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','birth_date','image', 'password1', 'password2', )

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, help_text='Mandatory')
    last_name = forms.CharField(max_length=30, help_text='Mandatory')
    email = forms.EmailField(max_length=254, help_text='Mandatory.')
    birth_date = forms.DateField(help_text='Mandatory. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('first_name','last_name','email','birth_date','password')

class EditProfileImage(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = {'image'}

class PostForm(forms.ModelForm):
    title=forms.CharField()
    description=forms.CharField()
    class Meta:
        model = Post
        fields=('title','description')

class PostFormOrignal(forms.ModelForm):
    title=forms.CharField()
    description=forms.CharField()
    class Meta:
        model = PostOrignal
        fields=('title','description')

class AddComment(forms.ModelForm):
    comment=forms.CharField()
    class Meta:
        model = Comment
        fields=('comment',)
