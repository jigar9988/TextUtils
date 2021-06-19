from django.contrib import admin
from django.urls import path
from textutils import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("output",views.output,name="output"),
]
