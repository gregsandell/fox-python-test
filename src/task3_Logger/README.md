# Task 3: Logger
Steps to test the API (`App/main.py`):

In terminal:
2. go to directory src/task3_logger/App
2. Run `uvicorn main:app --reload`

> Note: entered logs do not persist beyond the current uvicorn session

Testing with Curl:
Add a log line with the `/log` PUT endpoint:

1. View stored logs with the `/logs` GET endpoint:
> curl --location 'http://127.0.0.1:8000/logs'

2. Add a log with the `/log` PUT endpoint:
```javascript
curl --location 'http://127.0.0.1:8000/log' \
--header 'Content-Type: application/json' \
--data '{ "message": "Hello world, how are you?", "level": "INFO"}'
```
3. Search logs with the `/logs/search` GET endpoint:
* Search by message:
```javascript
curl --location 'http://127.0.0.1:8000/logs/search?keyword=world&field=message'
``` 
* Search by level (e.g. INFO, ERROR, DEBUG)
```javascript
curl --location 'http://127.0.0.1:8000/logs/search?keyword=world&field=message'
``` 

