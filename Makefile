include Makefile.venv

.PHONY: test
test:
	$(VENV)/python -m unittest -vvv tests/**/test_*.py

.PHONY: coverage
coverage:
	$(VENV)/coverage run --omit=".venv/*" -m unittest -vvv tests/**/test_*.py && \
	$(VENV)/coverage report -m

.PHONY: lint
lint:
	$(VENV)/yapf --diff --recursive --verify youtube2notion tests
	$(VENV)/flake8 youtube2notion tests

.PHONY: format
format:
	$(VENV)/yapf --in-place --recursive --verify youtube2notion tests
