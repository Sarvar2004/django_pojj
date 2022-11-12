from django.db import models


class Task(models.Model):
    title = models.CharField("nazvanie" ,max_length=50, )
    task = models.TextField("Opisaniye")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Zadacha'
        verbose_name_plural = 'Zadacha'