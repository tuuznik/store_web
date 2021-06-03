from django import forms
from .models import Item
from products.models import Product

class ItemForm(forms.ModelForm):
    #title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    #product_id = forms.OneToOneField(Product)
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()
    # description = forms.CharField(required=False, widget=forms.Textarea(
    #     attrs={"placeholder": "Your description"}))  # required set True by default
    # # email = forms.EmailField()
    # price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Item
        fields = ['product', 'quantity']

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     # if "Desktop" not in title:
    #     #     raise forms.ValidationError("This is not a valid title!!")
    #     return title