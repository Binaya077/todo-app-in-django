from django.db import models

#python manage.pymakemigrations
#python manage.py migrate

class Todo(models.Model): #PascalCase
    title=models.CharField(max_length=200) #varchar, char

    def __str__(self):
        return self.title