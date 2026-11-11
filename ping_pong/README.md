# Ping-pong

Responds to GET requests at `/pingpong` with pong `count` where `count` is the amount of requests that have been sent.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
kubectl apply -f manifests/
kubectl apply -f ../log_output/manifests/
```


Response can be viewed at http://localhost:8081/pingpong after a short time.