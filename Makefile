# Tutorial: https://makefiletutorial.com/#top

server:
	  gunicorn app.main:app -c gunicorn_config.py

dev_setup:
	 pip3 install -r requirements.dev.txt

test:
	pytest

html_test_coverage:
	pytest --cov-report html --cov=app tests/
