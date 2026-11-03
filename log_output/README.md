# Log output

Prints a random string generated at startup with a timestamp every 5 seconds.

## Deploy and view logs

```bash
kubectl apply -f manifests/deployment.yaml
kubectl logs -f deployment/log-output-dep
```