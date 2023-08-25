from django.db import models
from apps.posts.models import Media

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=255
    )
    work = models.CharField(
        max_length=50
    )
    image = models.ImageField(
        upload_to="team_images/"
    )
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        
class Students(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=255
    )
    image = models.ImageField(
        upload_to="team_images/"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        
class Parents(models.Model):
    name = models.CharField(
        max_length=355
    )
    description = models.TextField()
    parents = models.ForeignKey(
        Media,
        related_name="media_parents",
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"
        
class Stakeholder(models.Model):
    name = models.CharField(
        max_length=355
    )
    description = models.TextField()
    
    stakeholder = models.ForeignKey(
        Media,
        related_name="stakeholder",
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "Стейкхолдер"
        verbose_name_plural = "Стейкхолдеры"