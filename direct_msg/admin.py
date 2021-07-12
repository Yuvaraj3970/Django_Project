from django.contrib import admin
from django.urls.conf import include
from direct_msg.models import Message

# Register your models here.

admin.site.register(Message)