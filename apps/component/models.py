from django.db import models
from apps.person.models import DbObject, Students, Teachers
from apps.users.models import User
# Create your models here.

class ImageCategories(models.Model):
    db_obj = models.ForeignKey(
        DbObject,
        related_name="db_img_cat",
        on_delete=models.CASCADE
    )
    image = models.FileField(upload_to="img_cat/")
    
class FileCategories(models.Model):
    db_obj = models.ForeignKey(
        DbObject,
        related_name="db_file_cat",
        on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="file_cat/")
    
class Component(models.Model):
    db_obj = models.ForeignKey(
        DbObject,
        related_name="comp_db",
        on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=255)
    description = models.TextField()
    fullInfo = models.TextField()
    files = models.FileField(upload_to="file/")
    images = models.FileField(upload_to="img/")
    img_cat = models.ForeignKey(
        ImageCategories,
        related_name="com_img",
        on_delete=models.CASCADE
    )
    file_cat = models.ForeignKey(
        FileCategories,
        related_name="com_file",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'
        
class News(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_news",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="news_user",
        on_delete=models.CASCADE
    )
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.component.caption
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
class Awards(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_awards",
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Students,
        related_name="awards_stud",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'
        
class Advantages(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_advant",
        on_delete=models.CASCADE
    )
    teachers = models.ForeignKey(
        Teachers,
        related_name="teach_advant",
        on_delete=models.CASCADE
    )
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимуществы'
        
class Comments(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_com",
        on_delete=models.CASCADE
    )
    news = models.ForeignKey(
        News,
        related_name="com_news",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="user_com",
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class Courses(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_courses",
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Students,
        related_name="stud_courses",
        on_delete=models.CASCADE
    )
    teachers = models.ForeignKey(
        Teachers,
        related_name="teach_courses",
        on_delete=models.CASCADE
    )
    direction = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direction
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        
class Professions(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_prof",
        on_delete=models.CASCADE
    )
    direction = models.CharField(max_length=555)
    teachers = models.ForeignKey(
        Teachers,
        related_name="prof_teach",
        on_delete=models.CASCADE
    )
    add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.direction
    
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        
class Stakeholders(models.Model):
    component = models.ForeignKey(
        Component,
        related_name="comp_stakeholders",
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Students,
        related_name="stakeh_student",
        on_delete=models.CASCADE
    )
    teachers = models.ForeignKey(
        Teachers,
        related_name="stakeh_teach",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=555)
    add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Стейкхолдер'
        verbose_name_plural = 'Стейкхолдеры'

class MediaCategory(models.Model):
    db_obj = models.ForeignKey(
        DbObject,
        related_name="med_cat_obj",
        on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=300)
    description = models.TextField()
    name = models.CharField(max_length=255)
    items = models.FileField(upload_to="items/")
    
class ComponentIMGCategories(models.Model):
    img_cat = models.ForeignKey(
        ImageCategories,
        related_name="com_img_cat",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    
class ComponentFileCategories(models.Model):
    file_cat = models.ForeignKey(
        FileCategories,
        related_name="com_file_cat",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    
class File(models.Model):
    db_obj = models.ForeignKey(
        DbObject,
        related_name="file_db_obj",
        on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    size = models.IntegerField(blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    file = models.FileField(upload_to="file/")
    
class Image(models.Model):
    file = models.ForeignKey(
        File,
        related_name="file_img",
        on_delete=models.CASCADE
    )
    width = models.IntegerField(blank=True, null=True)
    heigth = models.IntegerField(blank=True, null=True)
    alt = models.FileField(upload_to="alt/")
    
class ComponentImage(models.Model):
    img = models.ForeignKey(
        Image,
        related_name="comp_img",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    
class ComponentFile(models.Model):
    file = models.ForeignKey(
        File,
        related_name="comp_file",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    
        
