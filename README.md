# mini-online-store


Требования:
    Python 3.6+
    Django 2.2+
    Postgres

Как запустить проект на локальном сервере:

Скачать репозиторий:

    git clone https://github.com/eldardzhorobekov/mini-online-store.git
    cd mini-online-store

Создать и активировать виртуальное окружение (я использовал [virtualenv](https://pypi.org/project/virtualenv/)):
    
    python3 -m virtualenv venv
    source ./venv/bin/activate # под linux

Установить все необходимые пакеты проекта:
    
    pip install -r requirements.txt

Создать .env файл в папке store и указать данные для подключения к базе postgresql:
    
    PSQL_DBNAME=<имя базы данных>
    PSQL_USER=<имя пользователя>
    PSQL_PASSWORD=<пароль>

Заполнить базу данными:
    
    cd store
    ./manage.py loaddata ./fixtures/db.json

Миграция и запуск:
    
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py runserver