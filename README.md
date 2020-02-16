ToDo List
=========

### Development environment preparation (in virtualenv):
```
pip install -r requirements.txt
```

### Running server:
```shell script
./runserver.sh
```

### Desired functionality of application and methods to gather data:

1. Index - list of all tasks containing task name, date, status and user who created task.
```bash
curl -X GET http://127.0.0.1:8000/api/v1/index -H "Content-Type: application/json"
```

2. My Tasks - list of current user task
```bash
curl -X GET http://127.0.0.1:8000/api/v1/tasks/ -u admin:testpassword123 -H "Content-Type: application/json"
```

3. Search - simple search (name or description contain text, tasks of all users), should return Task list
```bash
curl -X GET http://localhost:8000/api/v1/index/?search=done -H "Content-Type: application/json"
```

4. Task details - details about task
```bash
curl -X GET http://127.0.0.1:8000/api/v1/details/4/ -H "Content-Type: application/json"
```

5. Create new task - only authorized user can create tasks
```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks/ -u admin:testpassword123 -H "Content-Type: application/json" -d '{"user":"admin","name":"New task created for admin","task_status":"NEW","due_date":"2020-02-29","description":"Some description for new task"}'
```

6. Change task status - user can change status from NEW to DONE (only his/her own tasks)
```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/tasks/1/ -u admin:testpassword123 -H "Content-Type: application/json" -d '{"task_status": "DONE"}'
```
