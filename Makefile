VENV = .
VIRTUALENV = virtualenv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python

INSTALL = $(BIN)/pip install --no-deps

.PHONY: all test docs build_extras

all: build

$(PYTHON):
	$(VIRTUALENV) $(VTENV_OPTS) $(VENV)

build: $(PYTHON)
	$(PYTHON) setup.py develop

clean:
	rm -rf $(VENV)

test_dependencies:
	$(BIN)/pip install flake8 tox

test: build test_dependencies
	$(BIN)/flake8 example_service
	$(BIN)/tox

run:
	FLASK_APP=example_service bin/flask run