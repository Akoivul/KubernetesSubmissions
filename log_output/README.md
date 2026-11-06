# Log output

Prints a random string generated at startup with a timestamp every 5 seconds. Current status can be seen at `/`.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
kubectl apply -f manifests/
```

The current status can be seen at http://localhost:8081 after a short time.