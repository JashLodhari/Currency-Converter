from home import apps
from home.views import contact
from django.contrib import admin
from home.models import Contact
from home.models import images  
from home.models import pdf 
from home.models import book 

# Register your models here.
admin.site.site_header = 'Multipurpose Converter admin'
admin.site.site_title = 'Multipurpose Converter admin'
admin.site.index_title = 'Multipurpose Converter administration'
admin.site.register(Contact)
class AdminImages(admin.ModelAdmin):    
    list_display = ['id_no','name','loc','image','profile'] 

admin.site.register(images,AdminImages)

class AdminFiles(admin.ModelAdmin):
    list_display = ['No','Description','File']
    
admin.site.register(pdf,AdminFiles)

class AdminBooks(admin.ModelAdmin):
    list_display = ['Sr_no','Book_name',' Publication','Semester','Edition']

    admin.site.register(book)