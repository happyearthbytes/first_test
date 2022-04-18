#!/usr/bin/env bash
SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
BASE_PATH=${SCRIPT_PATH}/..

REMOVE_PATTERNS=(
    "./build"
    "*/build"
    "*/**/.pytest_cache"
    "./.pytest_cache"
    "*/**/*.pyc"
    "*/**/.DS_Store"
    "*/**/dist"
)

for i in "${REMOVE_PATTERNS[@]}"
do
    find . -path $i -exec rm -rf {} \;
done


