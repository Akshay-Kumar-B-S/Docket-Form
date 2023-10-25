from django.urls import path
from .views import create_docket

urlpatterns = [
    path('create/', create_docket, name='create_docket'),
    # Add more URLs as needed
]
