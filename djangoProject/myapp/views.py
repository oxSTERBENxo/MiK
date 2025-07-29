from django.shortcuts import render
from .models import *

# Create your views here.

from django.shortcuts import redirect

def redirect_to_country(request):
    country_name = request.GET.get('country_name')
    if country_name:
        return redirect('country_questions', country_name=country_name)
    return redirect('select')  # fallback


def select(request):
    return render(request, 'selectCountry.html', context={})

def country_questions(request, country_name):
    if not country_name:
        country_name = "Јапонија"
    country = Country.objects.filter(name=country_name).first()
    questions = country.question_set.all().prefetch_related('choice_set')
    polaroids = country.polaroid_set.all()

    context = {
        'country': country,
        'questions': questions,
        'polaroids': polaroids,
        'app_name': 'myapp',
    }
    return render(request, 'countryTemplate.html', context)