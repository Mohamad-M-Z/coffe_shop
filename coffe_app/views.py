from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Menu, Category, Contact, Reservation
from django.contrib import messages
from .form import ContactForm, NewsletterForm, ReservationForm





# Create your views here.
def index_view(request):
    return render(request, 'coffe_shop/index.html')


def about_view(request):
    return render(request, 'coffe_shop/about.html')



def service_view(request):
    return render(request, 'coffe_shop/service.html')


def menu_view(request):
    menus = Menu.objects.filter(status=True)
    context = {'menus': menus}
    return render(request, 'coffe_shop/menu.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message was sent successfully")
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent! Please try again!')

    form = ContactForm()
    return render(request, 'coffe_shop/contact.html',  {'form': form})


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message was sent successfully")
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent! Please try again!')

    form = ReservationForm()
    return render(request, 'coffe_shop/reservation.html', {"form": form})


def testimonial_view(request):
    return render(request, 'coffe_shop/testimonial.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRdirect('/')

