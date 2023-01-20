from django.urls import path
from .views import home_page, upload_kata_file

app_name = 'KataDB'
urlpatterns = [
    path('', home_page, name='homepage'),
    path('upload-kata/', upload_kata_file, name='upload-kata-csvfile')
]
