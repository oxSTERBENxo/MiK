# djangoProject/settings.py

from pathlib import Path
import os
import dj_database_url  # <-- add this

BASE_DIR = Path(__file__).resolve().parent.parent

# ---- Core flags from environment (prod-ready, still fine locally) ----
DEBUG = os.getenv("DEBUG", "1") == "1"   # default to 1 for local dev
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret-key")  # set real one on Render

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]
CSRF_TRUSTED_ORIGINS = ["https://*.onrender.com"]

# ---- Apps ----
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# ---- Middleware (add WhiteNoise right after SecurityMiddleware) ----
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- add this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

# ---- Templates ----
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # (debug removed is fine; request/auth/messages kept)
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# ---- Database (SQLite locally; Postgres on Render via DATABASE_URL) ----
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR/'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=not (os.getenv("DEBUG", "1") == "1"),
    )
}

# ---- Password validators (unchanged) ----
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---- I18N / TZ ----
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---- Static files (WhiteNoise) ----
STATIC_URL = "/static/"                               # ensure leading & trailing slash
STATIC_ROOT = BASE_DIR / "staticfiles"                # where collectstatic puts files
STATICFILES_DIRS = [BASE_DIR / "static"]              # your source static dir
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---- Media (use disk on Render with MEDIA_ROOT=/var/media) ----
MEDIA_URL = "/media/"
MEDIA_ROOT = Path(os.getenv("MEDIA_ROOT", BASE_DIR / "media"))

# ---- Security behind proxy (https) ----
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not (os.getenv("DEBUG", "1") == "1")
CSRF_COOKIE_SECURE = not (os.getenv("DEBUG", "1") == "1")

# ---- Default PK type ----
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
