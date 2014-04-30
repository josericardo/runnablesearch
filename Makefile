default: pylint_errors test

test:
	 nosetests -s -v $(TEST)

# local update
lup: uninstall install 

uninstall:
	pip uninstall -y -q scriptsearch

install:
	python setup.py sdist
	pip install dist/scriptsearch-0.0.1.tar.gz
	rm -rf MANIFEST dist

up: source_up lup

todos:
	grep -r --include="*.py" "TODO" .

pylint_errors:
	 pylint -E --rcfile=.pylintrc scriptsearch/ --disable=E0611
