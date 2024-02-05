MAIN = sorttwonumbers.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/1.in | $(PY) $(MAIN) | diff - data/1.ans
	@cat data/2.in | $(PY) $(MAIN) | diff - data/2.ans
	@cat data/new.in | $(PY) $(MAIN) | diff - data/new.ans
	@cat data/new2.in | $(PY) $(MAIN) | diff - data/new2.ans
	@cat data/new3.in | $(PY) $(MAIN) | diff - data/new3.ans
	@echo "All local tests passed!"

unittest:
	pytest test_unittests.py

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_unittests.py

check_types:
	mypy --disallow-untyped-defs --strict sorttwonumbers.py
	mypy --disallow-untyped-defs --strict test_unittests.py

check_style:
	flake8 sorttwonumbers.py --count --show-source --statistics

# submit to kattis
submit:
	kattis --problem sorttwonumbers --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc