from django.db import models
from apps.person.models import DbObject, Students, Teachers
from apps.users.models import User
# Create your models here.
class Component(DbObject):
    caption = models.CharField(max_length=255)
    description = models.TextField()
    fullInfo = models.TextField()
    files = models.FileField(upload_to="file/")
    images = models.FileField(upload_to="img/")
    img_cat = models.FileField(upload_to="com_img_cat/")
    file_cat = models.FileField(upload_to="com_file_cat/")
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'
        
class News(Component):
    user = models.ForeignKey(
        User,
        related_name="news_user",
        on_delete=models.CASCADE
    )
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
class Awards(Component):
    student = models.ForeignKey(
        Students,
        related_name="awards_stud",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.student.first_name
    
    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'
        
class Advantages(Component):
    teachers = models.ForeignKey(
        Teachers,
        related_name="teach_advant",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.teachers.first_name
    
    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимуществы'
        
class Comments(Component):
    com_news = models.ForeignKey(
        News,
        related_name="comment_news",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="user_comment",
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class Courses(Component):
    teachers = models.ForeignKey(
        Teachers,
        related_name="teach_courses",
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        
class Professions(Component):
    teachers = models.ForeignKey(
        Teachers,
        related_name="prof_teach",
        on_delete=models.CASCADE
    )
    add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        
class Stakeholders(Component):
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
    add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'Стейкхолдер'
        verbose_name_plural = 'Стейкхолдеры'

class MediaCategory(DbObject):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    name = models.CharField(max_length=255)
    items = models.FileField(upload_to="items/")
    
class ImageCategories(DbObject):
    image = models.FileField(upload_to="img_cat/")
    
class FileCategories(DbObject):
    file_cat = models.FileField(upload_to="file_cat/")
    
class ComponentIMGCategories(ImageCategories):
    title = models.CharField(max_length=255)
    
class ComponentFileCategories(FileCategories):
    title = models.CharField(max_length=255)
    
class File(DbObject):
    caption = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    size = models.IntegerField(blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    files = models.FileField(upload_to="files/")
    
class Image(File):
    width = models.IntegerField(blank=True, null=True)
    heigth = models.IntegerField(blank=True, null=True)
    alt = models.FileField(upload_to="alt/")
    
class ComponentImage(Image):
    title = models.CharField(max_length=255)
    
class ComponentFile(File):
    title = models.CharField(max_length=255)
    
        
