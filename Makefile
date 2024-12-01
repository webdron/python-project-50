install:
	poetry install
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
lint:
	poetry run flake8 gendiff
selfcheck:
	poetry check
check: selfcheck test lint
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall dist/*.whl --break-system-packages

.PHONY: install test lint selfcheck check build