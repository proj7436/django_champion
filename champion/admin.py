from django.contrib import admin
from .models import Champion, InfoMatch, Notification
# Register your models here.


admin.site.register(Champion)
admin.site.register(InfoMatch)
admin.site.register(Notification)