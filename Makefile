include scripts/make/common.mk
.SECONDEXPANSION:

.PHONY: build docs scan test env configure publish

BASH_SCRIPTS := local_setup
PY_SCRIPT = build docs scan test docker configure publish
PY_SCRIPT_2=$(addprefix py., $(PY_SCRIPT))

PY_PATH := py_app

default:
	@./start.sh
setup: local_setup
${BASH_SCRIPTS}:
	@./scripts/bash/$@.sh
${PY_SCRIPT_2}: _$$@
_py.%:
	@./scripts/python/$*.sh --path ${PY_PATH}
run:
	@./scripts/python/run.sh --path py_app --app joe_first_test_app
clean:
	@./scripts/clean.sh
install:
