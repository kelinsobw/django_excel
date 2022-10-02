from django.contrib import admin
from django.urls import path
from control.views import home, weighing, cabinet_weight, error_weidth, plus, cab_plus

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("error_weidth", error_weidth, name="error_weidth"),
    path("weighing/", weighing, name="weighing"),
    path("weighing/<str:cabinet>", cabinet_weight, name="cabinet_weight"),
    path('weighing/<str:cabinet>/<str:master>', cabinet_weight, name="cabinet_weight"),
    path("plus/", plus, name="plus"),
    path("plus/<str:p_choice_room>", cab_plus, name="cab_plus"),
]
