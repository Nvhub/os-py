from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField ( max_length=50, verbose_name='نام' )
    slug = models.CharField ( max_length=100, unique=True, verbose_name='ادرس') 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'  
        verbose_name_plural = 'دسته بندی ها'
class Article(models.Model):

    # --> for status Feilds
    STATUS_CHOICES =(
        ('p','منتشر'),
        ('d','پیش نویس')
        )
    # --> Releyted Models
    category    =    models.ManyToManyField (Category,related_name="articles")
    athor       =    models.ForeignKey      ( User , on_delete=models.CASCADE , verbose_name='نویسنده' )
    # --> End Releyted Models
    title       =    models.CharField       ( max_length=100 , verbose_name='سرتیتر' )
    slug        =    models.CharField       ( max_length=100 , unique=True , verbose_name='ادرس' )
    image       =    models.ImageField      ( upload_to='image' , verbose_name='تصویر' )
    body        =    models.TextField       ( verbose_name='بدنه متن' )
    created_at  =    models.DateTimeField   ( verbose_name='تاریخ' )
    status      =    models.CharField       ( max_length=1 , choices=STATUS_CHOICES , verbose_name='وضعیت' )


    def category_to_str (self):
        return " , ".join([category.name for category in self.category.all()])
    category_to_str.short_description = 'تصویر'

    class Meta:
        verbose_name = 'پست'  
        verbose_name_plural = 'پست ها'
    
    def img(self):
        return format_html("<img width='200' src='{}'>".format(self.image.url))