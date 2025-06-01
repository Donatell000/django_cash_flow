COMPOSE_FILE=docker-compose.yml
DOCKER_COMPOSE=docker compose -f $(COMPOSE_FILE)

.PHONY: up down ps migrate createsuperuser load_fixtures dump_fixtures

# Запуск контейнера
up:
	$(DOCKER_COMPOSE) up -d --build --remove-orphans

# Остановка контейнера
down:
	$(DOCKER_COMPOSE) down

# Выполнить миграции внутри контейнера
migrate:
	$(DOCKER_COMPOSE) exec web python manage.py migrate

# Создать суперпользователя
createsuperuser:
	$(DOCKER_COMPOSE) exec web python manage.py createsuperuser

# Импорт тестовых данных из fixture в БД
load_fixtures:
	$(DOCKER_COMPOSE) exec web python manage.py loaddata cashflow/fixtures/test.json

# Экспорт данных из БД в fixture
dump_fixtures:
	$(DOCKER_COMPOSE) exec web python manage.py dumpdata cashflow --indent 4 > app/cashflow/fixtures/test.json
