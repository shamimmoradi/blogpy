from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

def Validate_File_Extention(value) :
    import os 
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    vali_extention = [".jpg" ,".png"]
    if not ext.lower() in vali_extention :
        raise ValidationError("unsupported file extention .")





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user_avatar" , null=True , blank= True , validators=[Validate_File_Extention] )
    Description = models.CharField(max_length= 512 , null=False , blank= False)

    def __str__(self):
        return self.user.first_name+""+self.user.last_name

class Category (models.Model):
    title = models.CharField(max_length=128 , null= False , blank= False)
    cover = models.FileField(upload_to="files/category_cover" , validators= [Validate_File_Extention])
    

    def __str__(self) :
        return self.title

class Article(models.Model):
    title = models.CharField(max_length= 120 , null= False , blank= False)
    cover = models.FileField(upload_to="files/article_cover/" , null= False , blank=False ,validators= [Validate_File_Extention])
    content =RichTextField()
    created_at = models.DateTimeField(default=datetime.now , blank= False)
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    author = models.ForeignKey(UserProfile , on_delete= models.CASCADE)
