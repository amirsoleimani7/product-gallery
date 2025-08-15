from django.db import models

class NewsEmail(models.Model):
    user_email = models.CharField(max_length=255 , blank=False)

    def __str__(self):
        return self.user_email
    
    
