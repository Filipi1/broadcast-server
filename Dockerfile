FROM python:3.11.4-slim-bookworm AS base

RUN apt update -qq && apt install -qq --no-install-recomends -y \
    make gcc libffi-dev \
    && pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry install -q

COPY src /app

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache

FROM base AS final

COPY --from=base /app .

ENTRYPOINT [ "sh", "src/start.sh" ]