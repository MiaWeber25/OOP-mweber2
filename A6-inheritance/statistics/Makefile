MAIN = statistics1.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/sample.in | $(PY) $(MAIN) | diff - data/sample.ans
	@echo "All local tests passed!"

unittest:
	pytest test_data_set.py test_statistics.py

test-coverage:
	pytest --cov=statistics --cov=data_set test_data_set.py test_statistics.py --cov-report term-missing

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_titlecost.py test_calc_cost.py

check_types:
	mypy --disallow-untyped-defs --strict statistics.py data_set.py
	mypy --disallow-untyped-defs --strict test_titlecost.py test_calc_cost.py

check_style:
	flake8 statistics.py data_set.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

# submit to kattis
submit:
	kattis --problem statistics --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .coverage