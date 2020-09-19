from django.contrib import admin
from .models import Article,Category
# Register your models here.
# class AdminClock (admin.ModelAdmin):
#     list_display = ['name','module','color','image','mony']
#     search_fields = ['name','module']
#     list_filter = ['mony']

# admin.site.register(Clock,AdminClock)

class ArticleAdmin(admin.ModelAdmin) : 
    list_display  = ['title','slug','img','category_to_str','athor','status']
    search_fields = ['title','body']
    list_filter   = ['status','created_at']

class CategoryAdmin(admin.ModelAdmin) : 
    list_display  = ['name','slug']
    search_fields = ['name']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)