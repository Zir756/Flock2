from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

from django.db import models
class Post(models.Model):
    body = models.CharField(max_length=200) 
    
# objectsマネージャーを追加する。  
    objects = models.Manager()