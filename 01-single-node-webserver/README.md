# Single-Node Webserver

Key concepts
* Build and run docker images

Build image

```
$ docker build -t daniel/frontend .
..
$ docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
daniel/frontend                            latest              45edd3cd36f0        33 seconds ago      87MB
..
```

Run image

```
$ docker run -i -t -p 5000:5000/tcp daniel/frontend

  -i, --interactive                    Keep STDIN open even if not attached
  -t, --tty                            Allocate a pseudo-TTY
  -p, --publish list                   Publish a container's port(s) to the host
```

Go to http://localhost:5000
