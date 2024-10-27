from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'coffe_shop/index.html')


def about_view(request):
    return render(request, 'coffe_shop/about.html')



def service_view(request):
    return render(request, 'coffe_shop/service.html')


def menu_view(request):
    return render(request, 'coffe_shop/menu.html')


def contact_view(request):
    return render(request, 'coffe_shop/contact.html')


def reservation_view(request):
    return render(request, 'coffe_shop/reservation.html')


def testimonial_view(request):
    return render(request, 'coffe_shop/testimonial.html')

