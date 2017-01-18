# feiraslivressp-api

# Instale django e djangorestframework através do pip
pip install -r requirements.txt

# Para instalar ferramentas de apoio com os requirements fundamentais da aplicação
pip install -r requeriments_dev.txt

# Configura um novo projeto para uma única aplicação
django-admin.py startproject feiraslivressp

# Acessa diretório do projeto para criar aplicação
cd feiraslivressp/
django-admin.py startapp djangoapi
cd ..

# Sincroniza o banco de dados pela primeira vez
python manage.py migrate

# Cria usuário admin
python manage.py createsuperuser