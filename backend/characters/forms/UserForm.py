from django import forms

from characters.models_dir.UserModel import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'email')