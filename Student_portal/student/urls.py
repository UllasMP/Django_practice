from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('create/',views.create, name = 'create'),
    path('display/',views.display, name = 'display'),
    path('update/<int:student_id>/',views.update,name = 'update'),
    path('delete/<int:student_id>/',views.delete,name = 'delete')
]