MAIN = weatherApp.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest unittest_pytest clean
	@echo "All done!"

unittest:
	pytest test_weatherAPI.py test_weatherApp.py

test-coverage:
	pytest --cov=weatherAPI --cov=weatherApp test_weatherAPI.py test_weatherApp.py --cov-report term-missing

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_weatherAPI.py test_weatherApp.py

check_types:
	mypy --disallow-untyped-defs --strict weatherApp.py weatherAPI.py
	mypy --disallow-untyped-defs --strict test_weatherAPI.py test_weatherApp.py

check_style:
	flake8 weatherApp.py weatherAPI.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .coverage