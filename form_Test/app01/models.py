from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    # 浮点数，后面表示 最大8位数加上两个小数
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')
    def __str__(self):return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):return self.name
