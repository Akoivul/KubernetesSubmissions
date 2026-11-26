# Todo app

Todo page with an image from Lorem Picsum that is cached for 10 minutes. Todos are fetched from the todo-backend and new todos are posted to it through the form.

## Run in k3d

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
kubectl create namespace project
kubectl apply -f ../../volumes/
kubectl apply -f manifests/
kubectl apply -f ../todo_backend/manifests/
```

View at http://localhost:8081 after a short time.

## Run in GKE

Make sure the cluster has Gateway API enabled.

To run the backup CronJob, first create the key:

```bash
kubectl create secret generic storage-sa-key -n project --from-file=key.json=<path to key file>
kubectl apply -f backup/backup-cronjob.yaml
```

Run from the_project/:

```bash
kubectl create namespace project
kubectl apply -k .
kubectl get gateway -n project
```

View at http://ADDRESS/ after some time. (See ADDRESS with the last command)


## Exercise 3.9:

### DBaaS:

Pros:
- Required work for setting up and maintenance is small
- Automated backups are built in
- A backup can be restored with a single operation in the console

Cons:
- Costs to initialize and maintain are higher
- Extra cost because of backup storage

### DIY:

Pros:
- No extra costs

Cons:
- Required work for setting up is higher as files have to be written manually
- Required work for maintenance is higher as everything needs to be done manually
- No backups by default and need to be built
- Restoring requires more work as everything is done manually
