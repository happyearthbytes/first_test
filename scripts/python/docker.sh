#!/usr/bin/env bash
docker-compose --file environments/python/docker-compose.yml build
# docker-compose --file environments/python/docker-compose.yml up
docker-compose --file environments/python/docker-compose.yml run --rm python-ctr
