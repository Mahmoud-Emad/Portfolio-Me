from django.contrib import admin
from main.models import TestMe,ProjectsModel,Comments,ContactModel

# Register your models here.
admin.site.register(TestMe)
admin.site.register(ProjectsModel)
admin.site.register(Comments)
admin.site.register(ContactModel)
