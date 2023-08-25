from django.db import models

# Create your models here.

class Media(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to="media_news/")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = "Медии"

class News(models.Model):
    title = models.CharField(
        max_length=155)
    description = models.TextField()
    media = models.ForeignKey(
        Media,
        related_name="media",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        
class Professions(models.Model):
    title = models.CharField(
        max_length=155)
    description = models.TextField()
    profession = models.ForeignKey(
        Media,
        related_name="profession",
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
    
        
class AdditionalCourses(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField()
    media_cours = models.ForeignKey(
        Media,
        related_name="media_cours",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = "Дополнительный кружок"
        verbose_name_plural = "Дополнительные кружки"
        
class Awards(models.Model):
    title = models.CharField(
        max_length=255
    )
    created = models.DateField(auto_now_add=True)
    text = models.TextField()
    media_awards = models.ForeignKey(
        Media,
        related_name="media_awards",
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
        
class Contact(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=55)
    email = models.EmailField()
    instagram = models.URLField()
    twitter = models.URLField()
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"