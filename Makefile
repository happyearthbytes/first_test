include scripts/make/common.mk


BASH_SCRIPTS := local_setup other
PY_SCRIPT := build
PY_APP := py_app

default:
	@./start.sh
${BASH_SCRIPTS}:
	@./scripts/bash/$@.sh
configure:
	@./scripts/python/configure.sh --path py_app
publish:
	@./scripts/python/publish.sh --path py_app
install:
build:
	@./scripts/python/build.sh --path py_app
docs:
	@./scripts/python/docs.sh --path py_app
run:
	@./scripts/python/run.sh --path py_app --app joe_first_test_app
scan:
	@./scripts/python/scan.sh --path py_app
test:
	@./scripts/python/test.sh --path py_app
clean:
	@./scripts/clean.sh