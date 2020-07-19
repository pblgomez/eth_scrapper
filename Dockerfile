FROM python:3.8.4-alpine as base
# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base as python-deps
RUN pip install pipenv
WORKDIR /app
RUN apk add libxslt-dev
RUN apk add python3-dev
RUN apk add gcc
RUN apk add build-base
COPY Pipfile .
COPY Pipfile.lock .
# We set PIPENV_VENV_IN_PROJECT so we know exactly where it will be located
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base as runtime
WORKDIR /app
# deps
RUN apk add libstdc++ py3-lxml
# Copy virtual env from python-deps stage
COPY --from=python-deps /app/.venv .venv
ENV PATH=".venv/bin:$PATH"
COPY . ./
# Run the application
ENTRYPOINT ["python", "/app/src/main.py"]
