include Makefile.venv

.PHONY: test
test: venv
	$(VENV)/python -m unittest -vvv tests/**/test_*.py

.PHONY: coverage
coverage: venv
	$(VENV)/coverage run --omit=".venv/*" -m unittest -vvv tests/**/test_*.py && \
	$(VENV)/coverage report -m

.PHONY: lint
lint: venv
	$(VENV)/yapf --diff --recursive --verify youtube2notion tests
	$(VENV)/flake8 youtube2notion tests

.PHONY: format
format: venv
	$(VENV)/yapf --in-place --recursive --verify youtube2notion tests

.PHONY: start-server-dev
start-server-dev: venv
	$(VENV)/python app.py
