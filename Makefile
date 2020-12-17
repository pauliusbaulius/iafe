# https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile

setup:
	@mkdir -p reports
	@pip3 install pipenv
	@pipenv install

run:
	@python3 manage.py runserver 0.0.0.0:8000

lint:
	@echo "\nBLACK"
	@black website/ expenses/ --config pyproject.toml
	@echo "\nISORT"
	@isort website/ expenses/
	@echo "\nFLAKE8"
	@flake8 > reports/flake8.txt
	@echo "\nPYLINT"
	@pylint --rcfile=setup.cfg **/*.py > reports/pylint.txt
	@echo "\nBANDIT"
	@bandit *.py > reports/bandit.txt
