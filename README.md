sudo# analytics-api

## See also

[https://www.youtube.com/watch?v=tiBeLLv5GJo]
[https://github.com/codingforentrepreneurs/analytics-api]
[https://fastapi.tiangolo.com/]

## 000 System

```
Do not run postgresql server on startup
$ sudo systemctl disable postgresql

Run postgresql server on startup
$ sudo systemctl enable postgresql

```

## 001 Create a Python Virtual Environment

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=940s]

```
$ git clone https://github.com/common1/analytics-api.git
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install pip --upgrade
```
## 002 Install python packages

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=1224s]

```
File: requirements.txt
fastapi
uvicorn
gunicorn
sqlmodel
pydantic
sqlalchemy
timescaledb

$ pip install -r requirements.txt
```
## 003 FastAPI Hello World

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=1673s
]
```
$ uvicorn main:app --reload
```

## 004 Docker Desktop & Docker Compose

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=2022s]

```
List all docker processes
$ docker ps

Show docker images
$ docker images

Show all running containers
$ docker container ls

Show all containers
$ docker container ls -a

Stop all docker containers
$ docker stop $(docker ps -a -q)

Remove stopped container
$ docker rm 50f3042d203d

Remove all docker containers
$ docker rm $(docker ps -a -q)

Remove stopped container - docker rm <container_id>
$ docker rm 50c0e1d67f3f

Remove image - docker rmi <image_id>
$ docker rmi 9f8358e67991

Remove all images
$ docker image prune --all --force

Remove any resources that are not associated with a container
$ docker system prune

Delete everything
WARNING! This will remove:
    - all stopped containers
    - all networks not used by at least one container
    - all volumes not used by at least one container
    - all images without at least one container associated to them
    - all build cache
$ docker system prune -a --volumes

$ docker pull python:3.6.15
$ docker run python:3.6.15
$ docker run -it python:3.6.15
```

## 005 Production Dockerfile for FastAPI

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=2644s]

[https://codingforentrepreneurs.com/blog/deploy-fastapi-to-railway-with-this-dockerfile]

## 006  Build & Run FastAPI Container

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=3167s]

```
$ docker build -t analytics-api -f Dockerfile .
$ docker run analytics-api
```

## 007 Development Mode with Docker Compose

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=3474s]

```
$ docker compose up --watch

$ docker compose down
or
$ docker compose down -v

$ docker compose run app /bin/bash
$ docker compose run app python
$ docker compose run app python --remove-orphans
```

## 008 Section Wrap Up

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=4296s]

## 009 Routing & Data Validation

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=4467s]

## 010 Our First API Endpoint - Part 1

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=4611s]

## 010 Our First API Endpoint - Part 2

...

## 011  FastAPI Routing Module - Part 1

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=4871s]

## 011  FastAPI Routing Module - Part 2

...

## 012 Verify API Endpoint - Part 1

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=5163s]

## 012 Verify API Endpoint - Part 2

...

## 013 Basic Data Types

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=5361s]

## 014 List Data Types

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=5830s]

## 015 POST Method to Send our API Data

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=6101s]

## 016 Incoming Data Validation with Pydantic Schemas

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=6707s]

## 017 Optional Values with Pydantic

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=7076s]

## 18 Section Wrap Up

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=7470s]

## 019 Storing Data with SQLModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=7573s]

## 020 Postgres or TimescaleDB with Docker Compose -  Part 1

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=7668s]

## 020 Postgres or TimescaleDB with Docker Compose -  Part 2

...

## 021 Load Environment Variables with Python

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=8199s]

## 022 Pydantic to SQLModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=8647s]

## 023 First SQL Table with SQLModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=8795s]

## 024 Create Database Tables with FastAPI Lifespan

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=9230s]

## 025 Database Connection Issues

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=9644s]

## 026 Store Data using SQLModel Sessions

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=9959s]

## 027 SQLModel Query for List View

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=10308s]

## 028 Detail Lookup via SQLModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=10621s]

## 029 Update Data with SQLModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=10910s]

## 030 Adding a Datetime Field

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=11130s]

## 031 Updated At Timestamp Field

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=11439s]

## 032 Section Wrap Up

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=11652s]

## 033 Time Series Data in Postgres

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=11730s]

## 034 SQLModel to TimescaleModel

[https://www.youtube.com/watch?v=tiBeLLv5GJo&t=11853s]

