from django.contrib import admin
from blog.models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "avatar", "Description"]

admin.site.register(UserProfile , UserProfileAdmin)



class CategoryAmin(admin.ModelAdmin):
    list_display = ["title", "cover"]


admin.site.register(Category , CategoryAmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]
    search_fields = ["title" , "content"]

admin.site.register(Article , ArticleAdmin)


