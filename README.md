# GeoLearn

GeoLearn is an educational web application that helps Macedonian-speaking children learn about countries around the world through short interactive quizzes, photo galleries and country-related music. Each country has its own page combining a small multiple-choice quiz with real photographs and a song from that country.

The interface and all content (country names, questions, answers, captions) are entirely in **Macedonian (Cyrillic)**. The app is built with **Django** and is intended as a classroom/home-learning tool for children, originally designed as a companion to an external picture-book story.

**Live demo:** https://kviz-7zus.onrender.com

> The app is hosted on Render's free tier, which spins down when idle. If the site hasn't been visited recently, the first load can take **around one or two minutes** while the server wakes up — subsequent loads are fast.

## Features

- Country picker showing every country as a flag emoji, sorted alphabetically using Macedonian collation rules
- Per-country multiple-choice quiz with shuffled answer options
- Instant score feedback after finishing a quiz (client-side)
- Photo gallery per country with click-to-enlarge captions
- An example song from the selected country, with a play/pause toggle
- Content fully manageable through the Django admin (countries, questions, choices, photos, songs)

## How It Works

1. Open the app and pick a country from the flag grid on the home screen.
2. Answer the multiple-choice questions for that country.
3. Click **"Заврши"** (Finish) to see your score.
4. Browse the photo gallery and play the included song for that country.

Quiz data (countries, questions, choices, photos, songs) lives in the database and is fully editable through `/admin/` — no code changes are needed to add or update content.

## Technologies

- Python / Django
- SQLite (local development) / PostgreSQL (production, via `dj-database-url`)
- Gunicorn (WSGI server)
- WhiteNoise (static & media file serving)
- Bootstrap 5 (CDN)
- Vanilla JavaScript (no frontend framework or build step)
- Render (hosting)

## Project Structure

```
djangoProject/
├── manage.py
├── Procfile                  # gunicorn start command (Render)
├── requirements.txt          # dependency list 
├── djangoProject/            # Django project settings, URLs, WSGI/ASGI
├── myapp/                    # Models, views, admin for countries/quizzes
├── templates/                # selectCountry.html, countryTemplate.html
├── static/                   # favicon, background image, local Bootstrap copy
├── media/                    # country backgrounds, gallery photos, music
└── website_pictures/         # screenshots used in this README
```



## Getting Started

```bash
cd djangoProject

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# (Optional) create an admin user
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

The app runs at `http://127.0.0.1:8000/` and redirects to the country picker. No environment variables are required for local development; `DATABASE_URL`, `SECRET_KEY` and `DEBUG` can be set for a production-style run.

## Screenshots

**Country selection page**
![Country selection page](djangoProject/website_pictures/Screenshot%202026-07-24%20155612.png)

**Country quiz page**
![Country quiz page](djangoProject/website_pictures/Screenshot%202026-07-24%20155638.png)

**Photo gallery with caption popup**
![Photo gallery with caption popup](djangoProject/website_pictures/Screenshot%202026-07-24%20155714.png)

## Roadmap

- [ ] Validate quiz answers server-side instead of in client-side JavaScript
- [ ] Store quiz results/progress per session or account
- [ ] Show per-question feedback after finishing a quiz
- [ ] Add example songs for the remaining countries that don't have one yet
- [ ] Add automated tests for models and views

## License

Released under the [MIT License](LICENSE).
