from django.urls import path
from .views import home_page

app_name = 'validator'
urlpatterns = [
    path('', home_page, name='validator_home_page')
]
