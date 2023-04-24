from django.urls import path
from .views import home_page, upload_kata_file, MovesetTableFilterView, TechniqueTableView, KataTableView, StanceTableView, TechniqueCreateFormView, TechniqueUpdateFormView

app_name = 'KataDB'

urlpatterns = [
    path('', home_page, name='homepage'),
    path('upload-kata/', upload_kata_file, name='upload-kata-csvfile'),
    path('move-table/', MovesetTableFilterView.as_view(), name='kata-moveset-table'),
    path('tech-table/', TechniqueTableView.as_view(), name='tech-table'),
    path('kata-table/', KataTableView.as_view(), name='kata-table'),
    path('stance-table/', StanceTableView.as_view(), name='stance-table'),
    path('tech-create/', TechniqueCreateFormView.as_view(), name='tech-create'),
    path('tech-update/<int:pk>/,', TechniqueUpdateFormView.as_view(), name='tech-update'),
]
