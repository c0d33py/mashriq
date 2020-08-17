import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# secret keys
config.encoding = 'cp1251'
SECRET_KEY = config('SECRET_KEY')
# django robots.txt
ROBOTS_USE_SITEMAP = True
ROBOTS_USE_HOST = False
ROBOTS_USE_SCHEME_IN_HOST = True
# django deploy
CSRF_COOKIE_SECURE = True

# Keep our policy as strict as possible
# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
# CSP_IMG_SRC = ("'self'",)

SITE_ID = 1


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    'accounts.apps.AccountsConfig',
    'news.apps.NewsConfig',
    'epaper.apps.EpaperConfig',

    'django_social_share',
    'django_extensions',
    'ckeditor_uploader',
    'multiselectfield',
    'reset_migrations',
    'django_filters',
    'widget_tweaks',
    'embed_video',
    'ckeditor',
    'ads_txt',
    'robots',
    'taggit',
    'meta',
    'ads',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'
# AUTH_USER_MODEL = 'accounts.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'article/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'width': 'auto',
        # 'extraPlugins': ','.join(['youtube']),
        'toolbar': [
            ['Bold', 'Italic', 'Underline'],
            ['Font', 'FontSize', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', 'Image', 'Youtube']
        ],
    }
}

'''Login redirects'''
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
)

ALLOW_UNICODE_SLUGS = True
TAGGIT_CASE_INSENSITIVE = True
