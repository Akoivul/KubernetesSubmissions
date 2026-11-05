# Todo app

Web server that outputs "Server started in port NNNN" when it is started. Port is set with environment variable PORT in manifests/deployment.yaml which is by default 3000.

## Run in k3d

```bash
kubectl apply -f manifests/deployment.yaml
kubectl logs -f deployment/todo-app-dep
```