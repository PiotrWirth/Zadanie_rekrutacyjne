from django.urls import path
from . import views

app_name ='picture'

urlpatterns = [
    path('upload/',views.picture_upload,name='upload'),
    path('tier/',views.tier,name='tier'),
]