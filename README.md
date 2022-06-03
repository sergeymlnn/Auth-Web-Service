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
