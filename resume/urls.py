from django.urls import path
from . import views

urlpatterns = [
    path('resume/',views.resume),
    path('<int:id>/',views.cv,name="cv")
]

#path('<int:id>/',views.cv,name="cv")