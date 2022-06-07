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

# Using docker
docker exec -it my_auth_api pytest tests/api/test_main.py
```


### Build Docker Image & Run the Container

```
# Leverages DockerBuildKit
export DOCKER_BUILDKIT=1
export APP_PORT=8006

docker build -t my_auth_api .
docker run -p $APP_PORT:$APP_PORT --rm my_auth_api

# Using docker-compose
docker-compose up app
```


### Configuration for JWT
 - JWT_SCHEMA (default: *Bearer*)
 - JWT_SIGNING_ALGORITHM (default: *HS256*)
 - JWT_TOKEN_EXPIRATION_PERIOD (default: 1 minute)
 - JWT_SECRET_KEY
 
Define these **Environment Variables** to fit the configuration of the application to your own
requirements.
