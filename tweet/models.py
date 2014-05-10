from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms.fields import IntegerField, DateField

# Create your models here.

class tweet(models.Model):
    utiliateur = CharField(max_length=25)
    message = TextField(max_length=140)
    date_tweet = DateField()
    likes = IntegerField() 
    
    def __unicode__(self):
            return self.utiliateur 
    
    