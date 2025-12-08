# Task 3: Logger
Steps to test the API (`App/main.py`):

In terminal:
2. go to directory src/task3_logger/App
2. Run `uvicorn main:app --reload`

Using curl or POSTMAN:
* Add a log line with PUT endpoint `http://127.0.0.1:8000/log`
  * Sample input:  use a raw JSON body of `{ "message": "This is my log message", "level": "INFO"}`
* View available logs with GET endpoint `http://127.0.0.1:8000/logs`
* Search with the endpoint `http://127.0.0.1:8000/logs/search`
  * Sample input:  use keyword=mess and level=INFO, i.e. the full
    endpoint will be http://127.0.0.1:8000/logs/search?keyword=mad&field=message
  * The response will be the record you added with the PUT `/log` will 
```

