@echo off
rem Runs the tests (D3). Run build.cmd first.
docker run --rm notification-system python -m unittest discover -s tests -v
