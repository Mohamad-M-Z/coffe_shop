from django.shortcuts import render
from .models import Menu, Category, Contact
from django.contrib import messages
from .form import ContactForm





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
    return render(request, 'coffe_shop/reservation.html')


def testimonial_view(request):
    return render(request, 'coffe_shop/testimonial.html')

