### In process ...

### Running:
```
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8005
```


### Testing

Running first test
```
export PYTHONPATH=$PWD
pytest app/tests/api/test_main.py
```


### Build Docker Image & Run the Container

```
# Leverages DockerBuildKit
export DOCKER_BUILDKIT=1

docker build -t my_auth_api .
docker run -p 8005:8005 --rm my_auth_api
```
