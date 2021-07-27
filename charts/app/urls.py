from django.urls import path
from . import views
urlpatterns = [
    path('',views.showForm,name="form"),
    path('chart/',views.showChart,name="chart")
]
