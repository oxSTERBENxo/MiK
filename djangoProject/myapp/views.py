from django.shortcuts import render
from .models import *
import random

# Create your views here.

from django.shortcuts import redirect

def redirect_to_country(request):
    country_name = request.GET.get('country_name')
    if country_name:
        return redirect('country_questions', country_name=country_name)
    return redirect('select')  # fallback


def select(request):
    countries = Country.objects.all()
    return render(request, 'selectCountry.html', {'countries': countries})


def country_questions(request, country_name):
    if not country_name:
        country_name = "Јапонија"
    country = Country.objects.filter(name=country_name).first()
    questions = country.question_set.all().prefetch_related('choice_set')
    polaroids = country.polaroid_set.all()

    # Shuffle choices for each question
    for question in questions:
        choices = list(question.choice_set.all())
        random.shuffle(choices)
        question.shuffled_choices = choices  # attach for template

    context = {
        'country': country,
        'questions': questions,
        'polaroids': polaroids,
        'app_name': 'myapp',
    }
    return render(request, 'countryTemplate.html', context)
