## Стек технологий

- [🐍 Python](https://www.python.org/) — основной язык программирования  
- [🎯 Django 5.1](https://www.djangoproject.com/) — современный веб-фреймворк  
- [📡 Django REST Framework (DRF)](https://www.django-rest-framework.org/) — построение RESTful API  
- [⚙️ Celery](https://docs.celeryq.dev/en/stable/) — асинхронные задачи и очереди  
- [⏰ django-celery-beat](https://django-celery-beat.readthedocs.io/en/latest/) — периодические задачи Celery  
- [♻️ django-cors-headers](https://pypi.org/project/django-cors-headers/) — поддержка CORS-запросов  
- [🐘 PostgreSQL](https://www.postgresql.org/) — реляционная база данных  
- [🔌 psycopg2-binary](https://pypi.org/project/psycopg2-binary/) — драйвер PostgreSQL для Python  
- [📦 Redis](https://pypi.org/project/redis/) — брокер сообщений для Celery  
- [🌿 python-dotenv](https://pypi.org/project/python-dotenv/) — управление переменными окружения через `.env`  
- [🧪 Gunicorn](https://gunicorn.org/) — WSGI-сервер для запуска Django в production  
- [🗂️ django-admin-rangefilter](https://pypi.org/project/django-admin-rangefilter/) — фильтры по диапазону дат в Django admin

---

## Быстрый старт

Для работы с проектом используются **Docker**.

#### 1. Клонирование репозитория и переход в папку проекта
```bash
git clone https://github.com/Donatell000/django_cash_flow.git && cd django_cash_flow
```

#### 2. Создание файлов окружения  
Создайте `.env` и `.env.db`, используя `.env.example`,\
`.env.db.example` в качестве шаблонов.

#### 3. Запуск контейнеров
```bash
make up
```

#### 4. Перезапуск контейнеров при необходимости
```bash
make down && make up
```

#### 5. (Опционально) Создание суперпользователя
```bash
make createsuperuser
```

---

## Архитектура

Проект представляет собой монолитное веб-приложение, реализованное на Django. Все компоненты развернуты в изолированных Docker-контейнерах:

#### Django Backend
- Веб-приложение реализует интерфейс для управления движением денежных в стандартной admin панели

- Поддержка фильтрации по дате, статусу, типу, категории и подкатегории

- Автоматическая фильтрация с помощью JavaScript категорий и подкатегорий, в зависимости от выбранного типа операции, у подкатегорий дополнительная фильтрация по родительской категории

- Заложено полноценное RESTful API для будущего frontend разработчика

- Первично настроены Celery и Redis

#### Инфраструктура (Docker Compose)
Для развертывания проекта используется docker-compose, который автоматически поднимает все необходимые сервисы:

- PostgreSQL разворачивается из собственного Dockerfile \
Все переменные окружения вынесены в .env.db файл

- Redis используется как брокер сообщений для Celery

- Celery и Celery Beat запускаются как отдельные сервисы (celery_worker и celery_beat) с общим кодом Django-приложения

- Все сервисы объединены в единую пользовательскую сеть (django_network) с типом драйвера bridge

---

## Тестовые данные

Готовые тестовые данные можно загрузить в базу.

#### Импорт тестовых данных из fixture в БД
```bash
make load_fixtures
```

#### Экспорт данных из БД в fixture
```bash
make dump_fixtures
```

---

## Дополнительная информация

### Makefile
Проект использует `Makefile` для удобства работы. Примеры команд:
```bash
make up      # Запуск контейнеров
make down    # Остановка контейнеров
make logs    # Просмотр логов
make ps      # Просмотр запущенных контейнеров
```
