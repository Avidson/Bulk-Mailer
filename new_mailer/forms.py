from django import forms 
from django.core.files.uploadedfile import SimpleUploadedFile
import ckeditor
import PIL as Image
from ckeditor.widgets import CKEditorWidget
from django_quill.fields import QuillFormField
#from .models import EmailModel
from django.forms import ModelForm
from multi_email_field.forms import MultiEmailField 



#class EmailForm(forms.ModelForm):
 #   class Meta:
  #      model = EmailModel
   #     fields = ['to', 'from_email','bcc', 'reply_to', 'subject', 'message', 'attachment' ]


class EmailForm(forms.Form):
    to = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'size' : '90',
        'placeholder' : 'To'
    }))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'size' : '90',
        'placeholder' : 'From Email',
        
    }))
    bcc = MultiEmailField(widget=forms.TextInput(attrs={
        'size' : '90',
        'placeholder' : 'Bcc',
        'row' :4   }))
    reply_to = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'size' : '90',
        'placeholder' : 'Reply to this address(s)'
    }))
    
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'size' : '90',
        'placeholder' : 'Subject'
    }))
    message = QuillFormField()
    #attachment = forms.FileField(required=False)

