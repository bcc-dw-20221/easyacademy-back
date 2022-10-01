from entities.models import Teacher
from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class ClassHours(models.Model): 
    DAYS_WEEK = [
        #('DOM', 'Domingo'),
        ('SEC', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sabado-feira'),
    ]
    
    CLASS_SHIFT = [
        ('MNH', 'Manhã'),
        ('TRD', 'Tarde'),
        ('NT', 'Noite'),
    ]

    TIME_CLASS = [

        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ] 

    day_week = models.CharField(
        max_length=3, 
        choices=DAYS_WEEK,
    )

    time_class = models.CharField(
        max_length=1,
        choices=TIME_CLASS,
    )
    
    class_shift = models.CharField(
        max_length=3,
        choices=CLASS_SHIFT
    )

    def __str__(self):
        return f"{0} - {1} - {2}".format(
            self.day_week,
            self.time_class,
            self.class_shift
        )

class ClassRoom(models.Model):
    floor=models.CharField(max_length=2)
    number=models.CharField(max_length=3)
    
    
    def __str__(self):
        return f"{0}-{1}".format(
            self.floor,
            self.number,
        )
        
class Subject(models.Model):
    name=models.CharField(max_length=50, unique=True)
    teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    class_hours=models.ManyToManyField(ClassHours, related_name='subject')
    classroom=models.ManyToManyField(ClassRoom, related_name='subject')
    
    def __str__(self):
        return self.namegis 
    
class Course(models.Model):
    name=models.CharField(max_length=50, unique=True)
    #coordenador= models.ForeignKey(Professor, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name 
    
class Job(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(
        max_length=300,
        blank=False,
        default='This is void'
    )
    
    def __str__(self):
        return self.title
    

