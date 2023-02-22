from django.urls import path
from .views import home_page, upload_kata_file, MovesetTableFilterView, TechniqueTableView, KataTableView

app_name = 'KataDB'

urlpatterns = [
    path('', home_page, name='homepage'),
    path('upload-kata/', upload_kata_file, name='upload-kata-csvfile'),
    path('move-table/', MovesetTableFilterView.as_view(), name='kata-moveset-table'),
    path('tech-table/', TechniqueTableView.as_view(), name='tech-table'),
    path('kata-table/', KataTableView.as_view(), name='kata-table'),
]
