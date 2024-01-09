from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('list/',views.list),
    path('update/',views.Update_Task,name='update'),
    path('delete/<int:id>',views.Delete_Task,name='delete')
]