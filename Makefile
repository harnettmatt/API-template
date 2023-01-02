## starts a new fast server
docs:
	open http://127.0.0.1:8000/docs

lint:
	git add --all && pipenv run pre-commit

start:
	pipenv run uvicorn main:APP --reload

test:
	pipenv run pytest

test-vv:
	pipenv run pytest -vv

get-rankings:
	curl http://127.0.0.1:8000/rankings | jq
