# Todo app

Todo page with an image from Lorem Picsum that is cached for 10 minutes. Todos are fetched from the todo-backend and new todos are posted to it through the form.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
kubectl apply -f ../../volumes/
kubectl apply -f manifests/
kubectl apply -f ../todo_backend/manifests/
```

View at http://localhost:8081 after a short time.