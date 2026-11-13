# Todo backend

Stores the todos in a Postgres database running as a stateful set. GET /todos returns the todos as JSON and POST /todos creates a new todo. A cronjob generates a new todo every hour that reminds to read a random Wikipedia article. All todos sent to the backend are logged.

## Run in k3d

Follow the instructions in [todo_app/README.md](../todo_app/README.md)