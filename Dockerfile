# FROM python:3.9-buster
# ENV PYTHONUNBUFFERED=1

# WORKDIR /src

# RUN pip3 install poetry
# # RUN pip3 install requests

# COPY pyproject.toml* poetry.lock* ./
# COPY poetry.lock poetry.lock

# RUN poetry config virtualenvs.in-project true
# RUN poetry install --no-root

# COPY . /src

# # uvicornのサーバーを立ち上げる
# ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]

FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /src
RUN pip3 install poetry
# Poetryをインストール
COPY pyproject.toml poetry.lock ./

# プロジェクト内に .venv を作成し、依存をインストール
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-root --no-interaction --no-ansi
COPY . .

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]