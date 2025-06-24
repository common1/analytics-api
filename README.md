# analytics-api

## See also
[https://github.com/codingforentrepreneurs/analytics-api]

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

