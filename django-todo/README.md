Django, a high-level Python web framework, encourages rapid development and clean, pragmatic design. Django is the go to **Python web framework** for most of the fortune 500 companies and for any industry grade applications.

## Steps:

### Installation

```console
pip install Django
django-admin startproject todoapp
```

### Start

```console
python manage.py migrate
python manage.py runserver
python manage.py startapp todolist
```

- add 'todolist' to INSTALLED_APPS

### Add views
- implement todolist.views.py and create todolist.urls.py
- add urls to todoapp.urls.py

### Add templates
- add templates folder and file
- add "templates" to DIR in settings.py
- modify view: return render...

### Add models
- implement todolist.models.py

### Put together
```console
manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

- Adding models to the administration site:
    - todolist.admin.py: admin.site.register(Todo)
- login to admin

### add template
- add {% csrf_token %} to template

### CRUD
- implement views


## Core Features of Django Utilized in the To-Do Application

### 1. ORM (Object-Relational Mapping)

Django's ORM is a powerful tool for database interaction. It allows for the definition of data models in Python, which are then translated into database tables. This abstraction layer facilitates data creation, retrieval, update, and deletion operations without the need for raw SQL queries.

In this application, tasks are represented as models, making it easy to interact with task-related data.

```python
from django.db import models

# Create your models here.
class Todo(models.Model):
    #no need to create a 'id' feature django does that for us
    title=models.CharField(max_length=350)
    complete=models.BooleanField(default=False)
    # for accurate description
    def __str__(self):
        return self.title
```

### 2. Admin Interface

### Features of the Django Admin Interface

- **User Management**: View, create, update, and delete user accounts, including managing user permissions.
- **Task Management**: Directly manage the tasks within the database, including editing and deleting.
- **Data Insights**: Get an overview of the application's data, making it easier to analyze user engagement and task completion rates.

### Customizing the Admin Interface 

The Django admin interface is highly customizable. You can tailor it to meet the needs of your To-Do application by registering your models and configuring their admin classes. For example:

```python
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'date_created')
    list_filter = ('completed', 'date_created')
    search_fields = ('title', 'description')
```

This customization allows for a more detailed and user-friendly admin interface, enhancing the administrative experience.

3. Migrate the database:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your username, email, and password. Once created....

5. Run the server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to use the application, and to `http://127.0.0.1:8000/admin` to access the admin interface.

**enter your set credintials**
![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/3d03fc5c-2971-4da3-8263-34d8671d1d2f)
![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/01173891-e97d-445e-a773-856cec0e6ed5)
**We can make changes and modify our database from here has needed**
![image](https://github.com/KarthikGowdaRamakrishna/flaskVfastapiVdjango-/assets/144963620/b9e5c1f5-2a24-44ee-a0f4-1e41d8fda6d0)



### 3. URL Routing

Django's URL dispatcher allows for the design of clean, elegant URLs, which is crucial for a good web application structure. URL patterns are defined in a Python module, making URL changes easy and not tied to the application's design.

For the To-Do application, URL routing is used to direct HTTP requests to the appropriate view functions, handling tasks like displaying, creating, updating, and deleting tasks.

```python
from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
]
```

### 4. Template Engine

Django's template engine allows for dynamic HTML generation. Templates define placeholders and template tags, which get replaced with actual data when the template is rendered. This separation of HTML structure from Python code makes it easier to design and maintain the application's frontend.

### Add templates
- add templates folder and file
- add "templates" to DIR in settings.py
- modify view: return render...

### add template
- add {% csrf_token %} to template


### 5. Forms and Validation

Django forms handle the rendering of HTML form elements and the validation of submitted form data. This feature simplifies data collection and validation, ensuring data integrity for the application.


### 6. Security

Django includes numerous built-in security features that help developers avoid common security mistakes, such as SQL injection, cross-site scripting, cross-site request forgery, and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords.

For more information on Django and its extensive features, visit the [official Django documentation](https://docs.djangoproject.com/en/stable/).


