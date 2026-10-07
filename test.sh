#!/bin/sh
# Runs the tests (D3). Run build.sh first.
exec docker run --rm notification-system python -m unittest discover -s tests -v
