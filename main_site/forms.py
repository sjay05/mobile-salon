from django import forms

class ShopCreateForm(forms.Form):
    shop_name = forms.CharField(
        label='Shop Name: (If you use prexisting you will not be able to create)',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your Shop Name'
            }
        )
    )
    shop_description = forms.CharField(
        label='Shop Desc: (Max 150 words.)',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your Shop Description '
            }
        )
    )

class BookForm(forms.Form):
    address = forms.CharField(
        label="Enter your Address:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Example: 100 City Centre Dr, Mississauga, ON L5B 2C9'
            }
        )
    )