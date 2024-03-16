MAIN = titlecost.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/1.in | $(PY) $(MAIN) | diff - data/1.ans
	@cat data/2.in | $(PY) $(MAIN) | diff - data/2.ans
	@cat data/3.in | $(PY) $(MAIN) | diff - data/3.ans
	@echo "All local tests passed!"

unittest:
	pytest test_titlecost.py test_calc_cost.py

test-coverage:
	pytest --cov=titlecost --cov=calc_cost test_titlecost.py test_calc_cost.py --cov-report term-missing

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_titlecost.py test_calc_cost.py

check_types:
	mypy --disallow-untyped-defs --strict titlecost.py calc_cost.py
	mypy --disallow-untyped-defs --strict test_titlecost.py test_calc_cost.py

check_style:
	flake8 titlecost.py calc_cost.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

# submit to kattis
submit:
	kattis --problem titlecost --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .coverage