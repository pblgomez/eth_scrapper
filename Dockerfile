FROM python:3.8-alpine as base


FROM base as python-deps
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
COPY requirements.txt /app
RUN pip install --user -r requirements.txt


FROM base as runtime
WORKDIR /app
COPY --from=python-deps /root/.local/lib /root/.local/lib
COPY src .
ENTRYPOINT ["python", "/app/main.py"]