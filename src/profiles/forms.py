from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile
from django_countries import widgets, countries
from django.contrib.auth.models import User
from smartfields import fields


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

class UserProfileUpdateForm(forms.ModelForm):
    """Update user profile information."""
    #avatar = fields.ImageField(blank=True)
    dob = forms.DateTimeField(required=False,label='Date of Birth',
                            input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                            widget=forms.SelectDateWidget(
                                years=range(1917,2017)
                            )
    )
    bio = forms.CharField(required=False, max_length=140, label='Biography',
                    widget=forms.Textarea(attrs={'rows': 6}), min_length=10)
    location = forms.CharField(required=False,
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Enter city, state'}),
    )
    country = forms.ChoiceField(required=False,
        widget=widgets.CountrySelectWidget,
        choices=countries,
        label='Country of Residence'
    )
    fav_animal = forms.CharField(required=False,
        max_length=40,
        label='Favorite Animal',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your favorite animal'}
        )
    )
    hobby = forms.CharField(required=False,
        max_length=40,
        label='Favorite Hobby',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your favorite hobby'}
        )
    )

    class Meta:
        model = UserProfile
        # fields = ['avatar', 'dob', 'bio', 'location', 'country',
        #         'fav_animal', 'hobby']
        fields = ['dob', 'bio', 'location', 'country',
                'fav_animal', 'hobby']
        # labels = {
        #     'avatar': _('Your Photo'),
        # }

class UserUpdateForm(forms.ModelForm):
    """Form for updating user basic information."""
    verify_email = forms.EmailField(label="Please verify your email address.")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'verify_email']

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        verify = data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )