from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    """Form for creating a new user."""
    verify_email = forms.EmailField(label="Please verify your email address.")

    class Meta:
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'password1',
            'password2'
        ]
        model = get_user_model()

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        verify = data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )
        return data