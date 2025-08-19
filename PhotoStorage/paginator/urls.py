from django.urls import path
from . import views

urlpatterns = [
    path('' , views.pagination , name='paginator_page')
]