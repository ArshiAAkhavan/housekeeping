dev-ls:
	python3 housekeeping.py keep --all-houses --dry-run
dev-cl:
	python3 housekeeping.py keep --all-houses
install:
	PYTHON_PATH = which python3
	PWD= pwd
	echo "${PWD}"
	sed "1 i\\#!${PYTHON_PATH} " -i housekeeping.py
	chmod +x housekeeping.py
	ln -s ${PWD}/housekeeping.py /usr/bin/housekeeping