import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_wsgi_application()

# 🔽 Serve the repo’s media folder via WhiteNoise at /media/**
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # .../djangoProject
MEDIA_DIR = PROJECT_ROOT / 'media'                     # .../djangoProject/media

# Only add if the folder exists (safe for local/prod)
if MEDIA_DIR.exists():
    application = WhiteNoise(application)
    application.add_files(str(MEDIA_DIR), prefix='media/')
