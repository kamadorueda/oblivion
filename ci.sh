#! /usr/bin/env bash

set -o verbose \
    -o errexit \
    -o pipefail \
    -o functrace \
    -o errtrace \
    -o monitor \
    -o nounset \

tox -e lint
tox -e test
