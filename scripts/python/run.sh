#!/usr/bin/env bash

usage() {
  echo "Usage:"
  echo "$(basename "$0") [options]"
  echo ""
  echo "    -h|--help            Help"
  echo "    --verbose            Verbose"
}

invalid() {
  echo "ERROR: Unrecognized argument: $1" >&2
  usage
  exit 1
}

VERBOSE=NO
APP_PATH=""
APP=""

POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    --path)
      APP_PATH="$2"
      shift # past argument
      shift # past value
      ;;
    --app)
      APP="$2"
      shift; shift;
      ;;
    -h|--help)
      usage
      shift # past value
      ;;
    --verbose)
      VERBOSE=YES
      shift # past argument
      ;;
    -*|--*)
      echo "Unknown option $1"
      invalid $1
      exit 1
      ;;
    *)
      POSITIONAL_ARGS+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}" # restore positional parameters

cd ${APP_PATH}
python3 -m ${APP}