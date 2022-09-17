# todo_api


## Setup Guide

### Install Required Python modules
Run command : 
```
pip install -r requirement.txt
```

### Start Project 
Run Command to Start Server
```
python manage.py runserver
```
Run to Create tables in database
```
python manage.py makemigrations
python manage.py migrate
```

Open 
```
http://127.0.0.1:8000/api/tasks/
```

### API URLS
```
api/register  - To register 
api/tasks - To see all tasks
api/tasks/<id> - To get particular task
```

### api/register - POST
Input
```
{
"email" : "your_email@example.com",
"password" : "your_password"
}
```

### api/login - POST
Input
```
{
"email" : "your_email@example.com",
"password" : "your_password"
}
```

### api/tasks - POST
Input
```
{
"task" : "your_task",
"completed" : false
}
```

### api/tasks/<id> - PUT
Input
```
{
"task" : "your_updated_task",
"completed" : true
}
```

### Django Rest Framwork 

You can interact with api using DRF, Postman or Thunder Cilent
```
GET - To get all objects
POST - Create object
PUT - Update object
DELETE - Delete object
```
