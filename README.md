# Flask Template with blueprints

Basic template to build a Flask application with blueprints in Docker.


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
Open `http://localhost:8000` in your browser.
