from django.db import models

# Create your models here.

class Task3(models.Model):

    input = models.TextField("Field1")
    Title = models.TextField("Put text with phones to extract in here")
    stNumber= models.TextField("+7")
    ndNumber= models.TextField("how to format phones")
    output= models.TextField("output")

    def __str__ (self):
        return self.output


    class Meta:
        verbose_name="Задача"


class MapsModel(models.Model):

    Field1 = models.TextField("Field1")
    Field2 = models.TextField("Field2")
    Field3 = models.TextField("Field3")
    # Field4 = models.TextField("Field4")
    # Field5 = models.TextField("Field5")


    def __str__ (self):
        return self.Field1

    class Meta:
        verbose_name="карты"