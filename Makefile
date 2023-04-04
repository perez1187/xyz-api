build:
	docker compose -f production.yml up --build -d --remove-orphans

up:
	docker compose -f production.yml up -d

down:
	docker compose -f production.yml down

show_logs:
	docker compose -f production.yml logs