MAIN = cups.py
PY = python3

# target and its dependencies followed by command
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/cups-01.in | $(PY) $(MAIN) | diff - data/cups-01.ans
	@echo "All local tests passed!"

unittest:
	pytest test_cup_sequence.py test_cup_stacking.py test_cups.py

test-coverage:
	pytest --cov=cup_sequence test_cup_sequence.py test_cup_stacking.py --cov-report=term-missing --cov-report=html
	pytest --cov=cup_stacking test_cup_stacking.py --cov-report=term-missing --cov-report=html
	pytest --cov=cups test_cups.py --cov-report=term-missing --cov-report=html

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_cup_sequence.py test_cup_stacking.py test_cups.py

check_types:
	mypy --disallow-untyped-defs --strict cups.py cup_stacking.py cup_sequence.py
	mypy --disallow-untyped-defs --strict test_cups.py test_cup_stacking.py test_cup_sequence.py

check_style:
	flake8 cups.py cup_sequence.py cup_stacking.py test_cups.py test_cup_sequence.py test_cup_stacking.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

# submit to kattis
submit:
	kattis --problem cups --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .coverage