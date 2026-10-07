# D1: Python 3.13, pinned. The project uses the standard library only (D6),
# so there is nothing to install.
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY notification_system/ notification_system/
COPY tests/ tests/

# R42: the default command runs the example usage.
# The tests have their own command (D3): see test.sh, test.cmd or the README.
CMD ["python", "-m", "notification_system"]
