# Todo app

Web server that responds to a GET request sent to the `/` url. Port is set with environment variable `PORT` in `manifests/deployment.yaml` which is by default 3000.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
kubectl apply -f manifests/
```
Response can be viewed at http://localhost:8081 after a short time.