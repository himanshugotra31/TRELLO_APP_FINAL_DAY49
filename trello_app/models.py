from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class task_list(models.Model):
    name=models.CharField(max_length=50)  
    created_at=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}----{self.created_at}"
class task(models.Model):
    # def __init__(self,name,desc,due_date):
    #     self.name=name
    #     self.desc=desc
    #     self.due_date=due_date
    name=models.CharField(max_length=50)
    desc=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField()
    list=models.ForeignKey(task_list, on_delete=models.CASCADE)

    
