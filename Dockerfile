FROM python:3.10-slim

WORKDIR /app

# Creates an appuser and change the ownership of the application's folder
RUN useradd appuser \
    && chown appuser ./

# Installs poetry and pip
RUN pip install --upgrade pip

COPY --chown=appuser . ./

EXPOSE 8080

# Switching to the non-root appuser for security
USER appuser