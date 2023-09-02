from django.db import models

# Create your models here.
class WebOrders(models.Model):
    name = models.CharField(max_length=1555)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        
class Questions(models.Model):
    name = models.CharField(max_length=1555)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"