from django.db import models
from datetime import datetime


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Tipo" 
       verbose_name_plural = "Tipos"
       ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Categoria" 
       verbose_name_plural = "Categorias"
       ordering = ['id']

class Employee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete= models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='DNI', unique=True)
    date_joined = models.DateField(default= datetime.now, verbose_name='Fecha de Registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    #gender = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True) #se guardan en una carpeta llamada media
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True) #se guardan en una carpeta llamada media

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']


