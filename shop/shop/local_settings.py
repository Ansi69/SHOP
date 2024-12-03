from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-l@ol9+obncle)4t#zori2=6po2vm&yb3ukjyd0m37iffa)ss6w'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': 'QWERTy123',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "main/static",
]