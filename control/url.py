from django.contrib import admin
from django.urls import path
from control.views import home, weighing

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("weighing/", weighing, name="weighing"),
]
