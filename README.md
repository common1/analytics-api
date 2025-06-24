# analytics-api

## See also

[https://github.com/codingforentrepreneurs/analytics-api]
[https://fastapi.tiangolo.com/]

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

Stop all docker containers
$ docker stop $(docker ps -a -q)

Remove all docker containers
$ docker rm $(docker ps -a -q)

Remove image
$ docker rmi -f 143fd71618f9dock

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

