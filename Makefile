default: pylint_errors test

test:
	nosetests -s -v $(TEST)

# local update
lup: uninstall install 

uninstall:
	pip uninstall -y -q runnablesearch

install:
	python setup.py sdist
	pip install dist/runnablesearch-0.0.1.tar.gz
	rm -rf MANIFEST dist

up: source_up lup

todos:
	grep -r --include="*.py" "TODO" .

pylint_errors:
	pylint -E --rcfile=.pylintrc runnablesearch/ --disable=E0611
