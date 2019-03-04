
prereq:
1. Docker installed

Steps:

1. Create the image and start container
```
docker build . -t airflow
docker run -d -p 8080:8080 --rm    --name airflow_container    airflow
```

2. WebUI
go  to http://locallhost:8080
