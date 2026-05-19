ARG DOCKER_REGISTRY=ghcr.io
ARG VERSION=0.8.0-beta6
FROM $DOCKER_REGISTRY/kagent-dev/kagent/kagent-adk:$VERSION

WORKDIR /app

COPY agentdemo/ agentdemo/
COPY pyproject.toml pyproject.toml
COPY README.md README.md
COPY .python-version .python-version

RUN uv sync

ENV OTEL_SERVICE_NAME=agentdemo

CMD ["agentdemo"]
