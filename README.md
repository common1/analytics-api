# analytics-api

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

