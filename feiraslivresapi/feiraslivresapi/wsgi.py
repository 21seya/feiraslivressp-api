"""
WSGI config para o projeto feiraslivresapi.

Ele expõe o WSGI chamado como uma variável de nível de módulo nomeada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feiraslivresapi.settings")

application = get_wsgi_application()
