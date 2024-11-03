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

        fields = ['name', 'email', 'time','date', 'choice_field']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control'
            }),

            'choice_field': forms.Select(attrs={
                'class': 'orm-select form-select-lg mb-3 custom-select bg-transparent border-primary px-4'
            },choices=[
                ('psersn1', 'Person 1'),
                ('person2', 'Person 2'),
                ('peson3', 'Person 3'),
            ])
        }



