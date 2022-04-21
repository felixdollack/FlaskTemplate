# Flask Template

Basic template to build a Flask application with API (Swagger) in Docker.


## Build
Build the Docker container with name `flask_template`
```
docker build --tag flask_template .
```


## Run
```
docker run --rm --publish 8000:5000 --name flask_app flask_template
```

`--rm` will delete the container and all the data when it is stopped.

`--publish port-outside:port-inside` connect the inside of the Docker container to a port on your PC (outside).

`--name container_name` give the container a name.


## Test it!
Open `http://localhost:8000/api` in your browser.

You can test the API from there or use the curl command directly:
```
curl GET "http://localhost:8000/api/ping"
```
or
```
curl -X POST "http://localhost:8000/api/test" -H "accept: application/json" -H "Content-Type: application/json" -d '{"message": "My Message!"}'
```

## See also:
* [Flask Template](https://github.com/felixdollack/FlaskTemplate)
* [Flask Template with Blueprint](https://github.com/felixdollack/FlaskTemplate/tree/blueprint)
