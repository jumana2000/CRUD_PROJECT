from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:dataid>/',views.update,name='update'),
    path('delete/<int:dataid>/',views.delete,name='delete')   
]
