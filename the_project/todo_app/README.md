# Todo app

Web server that outputs "Server started in port NNNN" when it is started. Port is set with environment variable PORT which is by default 3000.

## Run in k3d

```bash
kubectl create deployment todo-app --image=akoivul/todo-app:1.2
kubectl logs -f deployment/todo-app
```
Port can be set with `kubectl set env deployment/todo-app PORT=NNNN`