from django.urls import path
from .views import home_page, download_file


app_name = 'committers'
urlpatterns = [
    path('', home_page, name='committers_home_page'),
    path('download/', download_file, name='download_file')
]
