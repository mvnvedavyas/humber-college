install:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - source $$HOME/.poetry/env && poetry install

lint:
	docker run --rm -i cruelplatypus67/msg < Dockerfile
	pylint --disable=R,C,W1203,W0702 app.py

test:
	python -m pytest -vv --cov=app tests.py

build:
	docker build -t cruelplatypus67/msg:latest .

run:
	docker run -p 8080:8080 cruelplatypus67/msg:latest

invoke:
	curl http://127.0.0.1:8080/change/1/34

run-kube:
	kubectl apply -f kube-def.yaml

all: install lint test