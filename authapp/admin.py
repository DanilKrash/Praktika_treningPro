from django.contrib import admin

from authapp.models import Contact, Trainer, Attendance, Sport, Profile

admin.site.register(Contact)
admin.site.register(Trainer)
admin.site.register(Attendance)
admin.site.register(Sport)
admin.site.register(Profile)
