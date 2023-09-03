from django.db import models
# Create your models here.
class DbObject(models.Model):
    state_id = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    class_name = models.TextField()
    create_date = models.TextField()
    last_update = models.TextField()
    create_user_id = models.IntegerField(blank=True, null=True)
    update_user_id = models.IntegerField(blank=True, null=True)
    
class Person(DbObject):
    first_name = models.CharField(max_length=555)
    last_name = models.CharField(max_length=555)
    patronymic = models.CharField(max_length=555)
    date_of_birth = models.CharField(max_length=777)
    gender = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=155)
    email = models.EmailField()
    address = models.CharField(max_length=666)
    

class Teachers(Person):
    direction = models.CharField(max_length=555)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        
class Parents(Person):
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"
        
class Students(Person):
    courses = models.CharField(
        max_length=555
    )
    parent = models.ForeignKey(
        Parents,
        related_name="parent",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        
