backend:
	docker compose up backend

migrations:
	docker compose exec backend python manage.py makemigrations

migrate:
	docker compose exec backend python manage.py migrate

lint:
	docker compose exec backend ruff check .

format:
	docker compose exec backend ruff format .

test:
	docker compose exec backend pytest
