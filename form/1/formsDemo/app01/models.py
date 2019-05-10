from django.db import models

# Create your models here.



class Book(models.Model):

    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)  # 999999.99
    date=models.DateField()
    publish=models.ForeignKey("Publish")
    authors=models.ManyToManyField("Author")
    def __str__(self):
        return self.title
class Publish(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name




