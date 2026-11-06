# Todo app

Web server that responds to a GET request sent to the / url. Port is set with environment variable PORT in manifests/deployment.yaml which is by default 3000.

## Run in k3d

Create the cluster with node port 30080 mapped to localhost:8082:

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```


```bash
kubectl apply -f manifests/
```
Response can be viewed from http://localhost:8082