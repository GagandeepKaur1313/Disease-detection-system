from django.contrib import admin
from diseaseapp.models import doctors
from diseaseapp.models import blogs
from diseaseapp.models import review
from diseaseapp.models import contactus
from diseaseapp.models import userregister
from diseaseapp.models import helpus

# Register your models here.
'''
admin.site.register(person)
'''
admin.site.register(doctors)
admin.site.register(blogs)
admin.site.register(review)
admin.site.register(contactus)
admin.site.register(userregister)
admin.site.register(helpus)