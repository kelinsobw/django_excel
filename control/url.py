from django.contrib import admin
from django.urls import path
from control.views import home, weighing, cabinet_weight, save_res

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("weighing/", weighing, name="weighing"),
    path("weighing/<str:cabinet>", cabinet_weight, name="cabinet_weight"),
    path("weighing/<str:slug>/save_res/", save_res, name="save_res"),
    path("weighing/save_res/<str:slug>", save_res, name="save_res"),
    path('weighing/<str:cabinet>/<str:master>', cabinet_weight, name="cabinet_weight"),

]
