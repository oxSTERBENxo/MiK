from django.shortcuts import render
from .models import *
import random
import locale
from django.utils.encoding import force_str

# Create your views here.

from django.shortcuts import redirect

def redirect_to_country(request):
    country_name = request.GET.get('country_name')
    if country_name:
        return redirect('country_questions', country_name=country_name)
    return redirect('select')  # fallback


def select(request):
    countries = list(Country.objects.all())
    try:
        # Try Macedonian locale (works locally)
        locale.setlocale(locale.LC_COLLATE, "mk_MK.UTF-8")
    except locale.Error:
        # Fallbacks for Render (it doesn’t have mk_MK)
        try:
            locale.setlocale(locale.LC_COLLATE, "C.UTF-8")
        except locale.Error:
            locale.setlocale(locale.LC_COLLATE, "C")  # last resort

    countries.sort(key=lambda c: locale.strxfrm(force_str(c.name)))
    return render(request, 'selectCountry.html', {'countries': countries})


def country_questions(request, country_name):
    if not country_name:
        country_name = "Јапонија"
    country = Country.objects.filter(name=country_name).first()
    questions = country.question_set.all().prefetch_related('choice_set')
    polaroids = country.polaroid_set.all()

    song = getattr(country, 'song', None)

    for question in questions:
        choices = list(question.choice_set.all())
        random.shuffle(choices)
        question.shuffled_choices = choices

    context = {
        'country': country,
        'questions': questions,
        'polaroids': polaroids,
        'song': song,
        'app_name': 'myapp',
    }
    return render(request, 'countryTemplate.html', context)
