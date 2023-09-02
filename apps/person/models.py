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
    
class Person(models.Model):
    dbobject = models.ForeignKey(
        DbObject,
        related_name="dbObj_person",
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=555)
    last_name = models.CharField(max_length=555)
    patronymic = models.CharField(max_length=555)
    date_of_birth = models.CharField(max_length=777)
    gender = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=155)
    email = models.EmailField()
    address = models.CharField(max_length=666)
    

class Teachers(models.Model):
    dbobject = models.ForeignKey(
        DbObject,
        related_name="dbObj",
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        related_name="Teach_per",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.person.first_name
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        
class Parents(models.Model,):
    dbobject = models.ForeignKey(
        DbObject,
        related_name="dbObj_par",
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        related_name="par_pers",
        on_delete=models.CASCADE
    )

    
    def __str__(self):
        return self.person.first_name
    
    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"
        
class Students(models.Model):
    dbobject = models.ForeignKey(
        DbObject,
        related_name="dbObj_stu",
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        related_name="par_stu",
        on_delete=models.CASCADE
    )
    courses = models.CharField(
        max_length=555
    )
    parent = models.ForeignKey(
        Parents,
        related_name="parent",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.person_first_name
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        
