lint:
	cd src && find . -type f -name "*.py" | xargs pylint --fail-under=8.5

test:
	python3 -m unittest discover tst
	coverage run -m unittest discover tst
	coverage report -m --include="src/*" --fail-under 85

mypy:
	cd src && find . -type f -name "*.py" | xargs mypy

.PHONY: all
all: lint mypy test
