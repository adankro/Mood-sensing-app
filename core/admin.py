

from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.apps import apps


from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
 	 
#     # Text to put at the end of each page's <title>.
    AdminSite.site_header = 'Mood Face Recognition APP'
#     # Text to put in each page's <h1> (and above login form).
    AdminSite.site_title = 'MoodFace App admin'


admin_site = MyAdminSite()

# Register your models here.

app = apps.get_app_config('core')
for model_name, model in app.models.items():
    admin.site.register(model)

#myModels=[UserProfile,Mood,DailyStats]
#admin_site.register(myModels)
