.DEFAULT_GOAL:=help
SHELL:=/bin/bash

##@ Dependencies

.PHONY: deps

deps:  ## Check dependencies
	$(info Checking and getting dependencies)

##@ Building

.PHONY: watch

watch: ## Watch file changes and build
	$(info Watching and building the project)

##@ Helpers

.PHONY: help

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
