#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feiraslivresapi.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # A importação acima pode falhar por algum outro motivo. Certifique-se
        # de que o problema é realmente que o Django está ausente para evitar
        # mascarar outras exceções no Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Não foi possível importar o Django. Tem certeza de que está "
                "instalado e disponível na variável de ambiente PYTHONPATH? "
                "Você se esqueceu de ativar um ambiente virtual?"
            )
        raise
    execute_from_command_line(sys.argv)
