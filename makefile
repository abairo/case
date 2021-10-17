DOCKER_CMD = docker-compose -f docker-compose.dev.yaml
EXTRA ?=

run-on-docker:
	$(DOCKER_CMD) $(EXTRA)

build:
	EXTRA="build" \
	make run-on-docker

up:
	EXTRA="up --force-recreate" \
	make run-on-docker

stop:
	EXTRA="stop $(service)" \
	make run-on-docker

volumes-prune:
	EXTRA="down --volumes" \
	make run-on-docker

migrate:
	EXTRA="run --rm --entrypoint="" web python manage.py migrate" \
	make run-on-docker

migrations:
	EXTRA="run --rm --entrypoint="" web python manage.py makemigrations" \
	make run-on-docker

createsuperuser:
	EXTRA="run --rm --entrypoint="" web python manage.py createsuperuser" \
	make run-on-docker

down:
	EXTRA="down" \
	make run-on-docker

manage:
	EXTRA="run --rm --entrypoint="" web python manage.py $(cmd)" \
	make run-on-docker

bash:
	EXTRA="run --rm --entrypoint="" web bash" \
	make run-on-docker

runserver:
	EXTRA="run --rm --entrypoint="" --service-ports web python manage.py runserver 0.0.0.0:8000" \
	make run-on-docker

loaddata:
	EXTRA="run --rm --entrypoint="" web python manage.py loaddata fixtures/*.json" \
	make run-on-docker

dumpdata:
	EXTRA="run --rm --entrypoint="" web python manage.py dumpdata --indent 4 $(cmd)" \
	make run-on-docker

shell:
	EXTRA="run --rm --entrypoint="" web python manage.py shell" \
	make run-on-docker

pytest:
	EXTRA="run --rm --entrypoint="" web py.test" \
	make run-on-docker

heroku-run:
	heroku run python manage.py $(cmd)

heroku-requirements:
	poetry export -f requirements.txt --output requirements.txt

heroku-deploy: heroku-requirements
	git push heroku master
