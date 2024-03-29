# Проект: запуск docker-compose

## Описание проекта

Результаты тестовых заданий для Python-разработчиков часто просят отправлять в контейнерах. Это делается для того, чтобы человеку, который будет проверять ваше тестовое, не пришлось настраивать окружение на своём компьютере.
В этом финальном проекте ревьюер сыграет роль работодателя, а проект api_yamdb будет результатом вашего тестового задания. Ваша задача — отправить проект «работодателю» «вместе с компьютером» — в контейнере.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

"""
<git@github.com>:baciroff/infra_sp2.git
"""

"""
cd api_yamdb
"""

Cоздать и активировать виртуальное окружение:

"""
python -m venv venv
"""

"""
source venv/bin/activate
"""

Установить зависимости из файла requirements.txt:

"""
python -m pip install --upgrade pip
"""

"""
pip install -r requirements.txt
"""

Выполнить миграции:

"""
python manage.py migrate
"""

Запустить проект:

"""
python manage.py runserver
"""

шаблон наполнения env-файла

"""
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД

"""

### Команды для заполнения базы данными

копируем файл с базами данных из /infra  в папку app

"""
docker cp fixtures.json <id контенера>:/app
"""

запускаем команду для загрузки баз

"""
docker-compose exec web python manage.py loaddata fixtures.json
"""
