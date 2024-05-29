from django.db import models
# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.TextField()
    date = models.DateField()
   
    def __str__(self):
        return self.fname

class images(models.Model):
    id_no=models.IntegerField(primary_key=True,editable=True)
    name=models.CharField(max_length=20)  
    loc=models.CharField(max_length=20)    
    image=models.ImageField(upload_to='images')   
    profile=models.FileField(upload_to='files')
 
    def __str__(self):        
        return self.name
    
class pdf(models.Model):
    No = models.IntegerField(primary_key=True, editable=True)
    Description=models.CharField(max_length=200)
    File=models.FileField(upload_to='')
    
    def __str__(self):        
        return self.Description

class book(models.Model):
    Sr_no = models.IntegerField(primary_key=True, editable=True)
    Book_name=models.CharField(max_length=60)
    Publication=models.CharField(max_length=60)
    Semester=models.IntegerField(editable=True)
    Edition=models.CharField(max_length=4,editable=True)

    def __str__(self):        
        return self.Book_name