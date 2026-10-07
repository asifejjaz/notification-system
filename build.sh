#!/bin/sh
# Builds the image (R8). Docker is the only prerequisite (A29).
exec docker build -t notification-system "$(dirname "$0")"
