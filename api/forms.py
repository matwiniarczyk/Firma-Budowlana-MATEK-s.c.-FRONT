from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': 'Wprowadź poprawny adres e-mail.',
                        'required': 'To pole jest wymagane.'
                        }
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': 'Wprowadź poprawny numer telefonu.',
                        'required': 'To pole jest wymagane.',
                        }
    )
    topic = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'To pole jest wymagane.',}
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
