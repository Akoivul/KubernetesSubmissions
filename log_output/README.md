# Log output

Two containers within a single pod and share a volume. log-writer generates a random string on startup and writes a line with the random string and timestamp to a file every 5 seconds. log-reader reads the file and provides the content at `/`.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
kubectl apply -f ../volumes/
kubectl apply -f manifests/
kubectl apply -f ../ping_pong/manifests/
```

View at http://localhost:8081 after a short time. Increase the count by making requests to http://localhost:8081/pingpong