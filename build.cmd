@echo off
rem Builds the image (R8). Docker is the only prerequisite (A29).
docker build -t notification-system "%~dp0."
