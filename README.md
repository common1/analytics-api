# analytics-api

## See also

[https://github.com/codingforentrepreneurs/analytics-api]
[https://fastapi.tiangolo.com/]

## 001 Create a Python Virtual Environment

```
$ git clone https://github.com/common1/analytics-api.git
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install pip --upgrade
```
## 002 Install python packages

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

```
$ uvicorn main:app --reload
```

## 004 Docker Desktop & Docker Compose

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

$ docker pull python:3.6.15
$ docker run python:3.6.15
$ docker run -it python:3.6.15
```

