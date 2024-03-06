MAIN = morsecodepalindromes.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat data/m0000.in | $(PY) $(MAIN) | diff - data/m0000.ans
	@cat data/m0001.in | $(PY) $(MAIN) | diff - data/m0001.ans
	@cat data/m0002.in | $(PY) $(MAIN) | diff - data/m0002.ans
	@cat data/m0003.in | $(PY) $(MAIN) | diff - data/m0003.ans
	@cat data/m0004.in | $(PY) $(MAIN) | diff - data/m0004.ans
	@cat data/m0005.in | $(PY) $(MAIN) | diff - data/m0005.ans
	@echo "All local tests passed!"

unittest:
	pytest test_convert_to_morse_code.py test_morsecodepalindromes.py test_palindrome_checker.py

test-coverage:
	pytest --cov=palindrome_checker --cov=convert_to_morse_code --cov=morsecodepalindromes --cov-report term-missing test_palindrome_checker.py test_convert_to_morse_code.py test_morsecodepalindromes.py

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_convert_to_morse_code.py test_morsecodepalindromes.py test_palindrome_checker.py

check_types:
	mypy --disallow-untyped-defs --strict morsecodepalindromes.py palindrome_checker.py convert_to_morse_code.py
	mypy --disallow-untyped-defs --strict test_convert_to_morse_code.py test_morsecodepalindromes.py test_palindrome_checker.py

check_style:
	flake8 morsecodepalindromes.py convert_to_morse_code.py palindrome_checker.py --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 --count --show-source --statistics .

# submit to kattis
submit:
	kattis --problem morsecodepalindromes --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf .coverage