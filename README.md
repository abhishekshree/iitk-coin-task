## Web server

Instructions to run locally:
1. Run ```pip install -r requirements.txt``` to install dependencies.
2. Use command ```python app.py``` to start the server.


### Server details

The server listens at ```PORT 8080``` and accepts a POST request at ```/coins``` endpoint.


The body of the request should be a JSON object:
```json
{
	"rollno":"201010"
}
```

An example response would be:
```json
{
  "coins": 10
}
```

> An example post request is available [here](./post.sh) using cURL.