from django.db import models



from django.contrib.auth.models import User


class Task(models.Model):

    title=models.CharField(max_length=200)

    status=models.BooleanField(default=False)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
