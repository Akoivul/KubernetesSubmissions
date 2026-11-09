# Todo app

Web server that responds to a GET request sent to `/` with an HTML page that has a random image from Lorem Picsum. The image is cached on a persistent volume and replaced when it's older than 10 minutes. Port is set with environment variable `PORT` in `manifests/deployment.yaml` which is by default 3000.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
kubectl apply -f ../../volumes/todo-persistentvolume.yaml
kubectl apply -f ../../volumes/todo-persistentvolumeclaim.yaml
kubectl apply -f manifests/
```

Response can be viewed at http://localhost:8081 after a short time.