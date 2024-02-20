MAIN = ConvexPolygonArea.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/sample.in | $(PY) $(MAIN) | diff - data/sample.ans
	@cat data/2.in | $(PY) $(MAIN) | diff - data/2.ans
	@cat data/3.in | $(PY) $(MAIN) | diff - data/3.ans
	@cat data/4.in | $(PY) $(MAIN) | diff - data/4.ans
	@echo "All local tests passed!"

unittest:
	pytest test_ConvexPolygonArea.py test_Polygon.py test_Point.py

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_ConvexPolygonArea.py Point.py Polygon.py

check_types:
	mypy --disallow-untyped-defs --strict ConvexPolygonArea.py Point.py Polygon.py
	mypy --disallow-untyped-defs --strict test_ConvexPolygonArea.py test_Point.py test_Polygon.py

check_style:
	flake8 ConvexPolygonArea.py Point.py Polygon.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

# submit to kattis
submit:
	kattis --problem convexpolygonarea --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc