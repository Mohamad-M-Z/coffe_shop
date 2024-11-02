from django import forms
from .models import Contact, Newsletter, Reservation
# from captcha.fields import CaptchaField



class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }




