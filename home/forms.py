from django import forms
from home.models import pdf
from home.models import book

class books(forms.ModelForm):

    class Meta:
        model =  book
        fields=('Sr_no','Book_name','Publication','Semester','Edition')
        labels={
            'Sr_no': 'Sr_no',
            'Book_name':'Book_name',
            'Publication':'Publication',
            'Semester':'Semester',
            'Edition':'Edition',
        }

        def __init__(self,*args,**kwargs):
            super(book,self).__init__(*args,**kwargs)
            self.fields['Book_name'].empty_label="Select"

class pdfs(forms.ModelForm):

    class Meta:
        model =  pdf
        fields=('No','Description','File')
        labels={
            'No': 'No',
            'Description':'Description',
            'File':'File',
        }

        def __init__(self,*args,**kwargs):
            super(pdf,self).__init__(*args,**kwargs)
            self.fields['Description'].empty_label="Select"