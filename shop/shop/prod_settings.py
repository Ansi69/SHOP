from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insesdafewqr2342345wetwert342ukjyd0m37iffa)ss6w'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'db_user',
        'PASSWORD': 'QwErTy123!!!',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "main/static",
]