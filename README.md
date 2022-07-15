# devsearch

1. devsearch - django project
2. projects - django app in `djangoproject start project`
3. templates - html templates with file project with the name of the projects


### Database Relationships

1. One-To-One - One Table record can relate to one record in another table
2. One-To-Many - One table record can relate to many records in another table
   1. using forign key in many table
3. Many-To-Many - occurs when multiple records in one table are associated with multiple records in another table
   1. using a table, intermediary table that records FK in table. Django does it by default
   2. Reference in html template
    ```html
    
        {% comment %} many to many relationship {% endcomment %}
                        {% for tag in project.tags.all %}
    ```
    ```
  
## Models

```python
    #attribute is attribute of model class
    queryset = ModelName.objects.all()
    .get()
    .get(attribute='value')
    .filter()
    .filter(attribute__startswith='value')
    .filter(attribute__contains='value')
    .filter(attribute__icontains='value') #ingore case
    .filter(attribute__gt='value') #greater than
    .filter(attribute__gte='value')
    .filter(attribute__lt='value') #less than and equal to
    .filter(attribute__lte='value')
    .exclude()
    .exclude(attribute='value')
    .filter().order_by('key1', '-key2') #- equals descending
    .create(attribute='value') # Create instance of model
    .save() # save instance of model
    .attribute = "New Value"
    .last()
    object.delete()
    object.childmodel_set.all()
    object.relationshipname.all()
```


## form references


```python
  {{form.as_p}}
  form.field
  form.field.label
  {% for field in form %}
  
```

1. can also update form types by overwriding constructor for modelforms and updating fields




## Static Files

1. create static directory and sub directories images, styles, and js in base_dir 
2. update STATICFILES_DIR variable in settings.js
3. when using static files you must load static files `{% load static %}`
4. Can reference static files like this `<link rel="stylesheet" href='{% static "styles/main.css" %}'>`
5. Set This directory in order to provide where to upload image content `MEDIA_ROOT = BASE_DIR / 'static/images'`
6. create MEDIA_URL in settings.py and configure MEDIA_ROOT to MEDIA_URL - `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`  
7. update forms `form = ProjectForm(request.POST,request.FILES, instance=project)`

8. update enctype for images
```html
<form action="" method ="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit">
    </form>
```
9. Create 'Static_ROOT' variable in setting.py - defines where static files in production will be
10. set this as 'BASE_DIR / 'staticfiles' - run `python manage.py collectstatic`
    1.  creates staticfile folder for production
    2.  Will be changed to third party tool in the future
11. When Setting `DEBUG=False` - URLS set in production for static is what will show. `python manage.py collectstatic`
12. 'pip install whitenoise` - is required to serve static files
13. add the following as middleware `"whitenoise.middleware.WhiteNoiseMiddleware",`


## User App

1. This will be in a seperate app in project which needs to updated to installed projects
2. Steps Completed
   1. Create application
   2. Create Views and register them to urls and create a urlspatterns and register them to project 
   3. Create models and register them in admins.py
   4. Create templates with directory of app as subdirectory where you place your templates and reference them for your view renders

### Signals 

1. Sender - sends of original actions
2. Reciever - recieves action and triggers an action
   1. create an action that listens for events at life event cycle
3. https://docs.djangoproject.com/en/4.0/topics/signals/
4. Signals can either be linked to methods as decorators or as part of their signal connect method
5. seperate signals out in an app and update the use of signals by updating `apps.py` and import signals
```html
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals
```

## Auth and Auth

1. Authentication - who the user is
2. Authorization - Grants or denies you permissions to access certain resources
3. Session based authentication with sessionid
4. Imports required
   1. `from django.contrib.auth import login, authenticate, logout`
    `from django.contrib.auth.models import User`
    2. Methods
       1. authenticate - Checks User model to see if user exists
       2. login - creates a session and passes id to cookies
       3. logout - removes session and deletes id from cookies
5. data fetched from is request.POST
6. Import messages from contrib for flash messages
7. Set the output to main.html so it always shows up
8. Use UserCreationForm to overwride forms in forms.py pertaining to User model: `form = CustomUserCreationForm(request.POST)`
9. 