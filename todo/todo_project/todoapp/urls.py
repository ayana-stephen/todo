
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.add,name='add'),
   # path('details', views.details, name='details'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('cbvadd/',views.TaskListview.as_view(),name='cbvadd'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),
]
