# TodoList

Simple todo List

### Technologies:
- python (FastAPI)
- mongodb
- docker

### Build application
```
docker-compose build
```

### Run
```
docker-compose up web
```
go to "localhost:8000/[endpoints]" (or use Postman)

### Apply dummy data
```
docker-compose run web python init_application.py
```
