from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    phone=forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = User
        fields=("username","email","phone","password1","password2")
    
    def save(self, commit=True):
        user=super(NewUser,self).save(commit=False)
        user.phone=self.cleaned_data['phone']
        if commit:
            user.save()
        return user
        