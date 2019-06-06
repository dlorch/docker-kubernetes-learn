# Frontend/Backend Webserver

Key concepts
* Kubernetes deployments
* Kubernetes services

Build images

```
$ docker build -t daniel/frontend frontend
$ docker build -t daniel/backend backend
$ docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
daniel/backend                             latest              2c0ab781e9c9        About an hour ago   96.8MB
daniel/frontend                            latest              e0a2df6ef706        About an hour ago   96.8MB
..
```

Start Kubernetes deployment for backend

```
$ kubectl apply -f backend/deployment.yaml
$ kubectl get pods --selector app=backend
NAME                       READY     STATUS    RESTARTS   AGE
backend-7bd9f7f686-8bkpn   1/1       Running   0          3s
```

Start Kubernetes service for backend

```
$ kubectl apply -f backend/service.yaml
$ kubectl get service --selector app=backend
NAME      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend   ClusterIP   10.108.87.179   <none>        5000/TCP   1m 
$ kubectl port-forward service/backend 5000:5000
```

Go to http://localhost:5000

Abort with CTRL-C

Start Kubernetes deployment for frontend

```
$ kubectl apply -f frontend/deployment.yaml
$ kubectl get pods --selector app=frontend
NAME                       READY     STATUS    RESTARTS   AGE
frontend-dcd4454bb-xnnt2   1/1       Running   0          9m
```

Start Kubernetes service for frontend

```
$ kubectl apply -f frontend/service.yaml
$ kubectl get service --selector app=frontend
NAME       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
frontend   ClusterIP   10.99.69.178   <none>        5000/TCP   22m
$ kubectl port-forward service/frontend 5000:5000
```

Go to http://localhost:5000

Abort with CTRL-C

Check logs from backend

```
$ kubectl logs backend-7bd9f7f686-8bkpn
 * Serving Flask app "backend" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [24/May/2019 19:41:51] "GET / HTTP/1.1" 200 -
10.1.0.19 - - [24/May/2019 23:11:50] "GET / HTTP/1.1" 200 -
10.1.0.19 - - [24/May/2019 23:11:55] "GET / HTTP/1.1" 200 -
```

Cleanup

```
kubectl delete deployment -l app=frontend
kubectl delete service -l app=frontend
kubectl delete deployment -l app=backend
kubectl delete service -l app=backend
```
