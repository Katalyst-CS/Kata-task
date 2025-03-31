deps:
	pip freeze > requirements.txt

infra:
	docker compose up -d

infra-down:
	docker compose down

.PHONY: deps