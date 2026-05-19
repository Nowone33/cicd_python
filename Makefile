
.PHONY: help check-type check-type test coverage compile build dependency venv


# cf. https://jiby.tech/post/make-help-documenting-makefile/
help:
	@echo "This makefile contains the following targets," \
          "from most commonly used to least:" \
          "(docs first, then target name)"
	@echo "Set NO_COLOR=1 to disable ANSI color coding\n"
	@awk \
		'/^##/ {sub(/## */,""); print} \
		/^[a-z0-9-]+:/ && !/\.PHONY:/ \
			{sub(/:.*/, ""); \
				print "⮡   ${ANSI_COLOR_RED}" \
					$$0 \
					"${ANSI_COLOR_RESET}\n" \
			}' \
		Makefile

check-style:
	flake8 calculs tests

format:
	black calculs tests

check-type:
	mypy calculs

test:
	pytest --cov=calculs --cov-report=term-missing

coverage:
	pytest --cov=calculs --cov-report=term-missing --cov-fail-under=90

compile:
	python main.py

build:
	pyinstaller --onefile --name calculs-snapshot main.py

check-build-presence:
	ls dist/calculs

dependency:
	pip install -r requirements.txt

venv:
	python3 -m venv .venv
	source .venv/bin/activate

