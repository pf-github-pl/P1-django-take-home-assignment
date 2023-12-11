FROM python:3.11.6-slim-bookworm as base

WORKDIR /app

RUN apt-get update;
RUN apt-get -y upgrade;
RUN apt-get clean;
RUN rm -rf /var/lib/apt/lists/*

FROM base as build
COPY ./requirements/ ./requirements/
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
RUN rm -rf .env*

FROM base as prod
COPY --from=build /app /app
COPY --from=build /usr/local /usr/local
RUN mkdir -p logs/
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "info", "--log-file", "logs/gunicorn.log", "--access-logfile", "logs/access.log", "food_trucks.wsgi:application"]

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
