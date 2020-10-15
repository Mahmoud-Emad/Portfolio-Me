
from django.urls import path

from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from project import settings



urlpatterns = [
    
    path('',views.main,name="home"),
    path('about-me',views.Aboutme,name="aboutme"),
    path('Service-Skills',views.Service,name="Service"),
    path('thanks-quzz',views.Thanks,name="thanks"),
    path('Test-Me',views.TestMeViwe,name="test-me"),
    path('Project-all',views.Project,name="Project"),
    path('project-one<slug>',views.Project_Ditail,name="Project_Ditail"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)