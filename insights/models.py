from django.db import models

# Create your models here.
class Message(models.Model):
    first_name = models.CharField(blank = False, max_length = 50)
    last_name  = models.CharField(blank = False, max_length = 50)
    subject    = models.CharField (blank = False, max_length = 20)
    email      = models.EmailField(blank = False, max_length = 50)
    text       = models.TextField(blank = False, max_length = 500)
    
    class Meta:
        verbose_name_plural = "messages"
        db_table = "messages"
    
    def __str__(self):
        return self.email + " " + self.subject
    