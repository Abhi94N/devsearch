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