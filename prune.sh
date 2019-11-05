#! /usr/bin/env bash

dirs=( \
  '.tox' \
  '.coverage*' \
  '.mypy_cache' \
  '*.egg-info' \
  '__pycache__' \
)

for glob in ${dirs[@]}
do
  find . -type d -name "${glob}" | xargs -n1 rm -rf
done
