.DEFAULT_GOAL:=help
SHELL:=/bin/bash

##@ Helpers

.PHONY: help

help:  ## Display this help
	@cat ${MAKEFILE_LIST} | awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } '
