# Todo app

Web server that responds to a GET request sent to the / url. Port is set with environment variable PORT in manifests/deployment.yaml which is by default 3000.

## Run in k3d

```bash
kubectl apply -f manifests/deployment.yaml
kubectl port-forward deployment/todo-app-dep 3000:3000
```
Response can be viewed from http://localhost:3000