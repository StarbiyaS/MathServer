from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofsquareprism/',views.squareprismarea,name="areaofsquareprism"),
    path('',views.squareprismarea,name="areaofsquareprism")
]
