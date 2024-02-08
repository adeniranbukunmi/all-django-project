from django.db import models

# Create your models here.
    # id=models.BigAutoField(primary_key=True) this will be created automatically so there is no need to recreate it.#
class students(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) :
        return self.name