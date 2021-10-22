from django.contrib import admin
#from.models import EmailModel
# Register your models here.

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('to', 'from_email', 'bcc', 'reply_to', 'subject', 'message', 'attachment')
admin.site.register(EmailModel, EmailModelAdmin)