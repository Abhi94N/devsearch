from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    #can set this to empty
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # Django does have id by default but you can overwride with encoding
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
        
    