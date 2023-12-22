from django.urls import path
from CrudApi import views
 

urlpatterns = [
    path('',views.show,name='homepage'),
    
    # path('api/students/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
    # path('api/students/<int:pk>/update/',views.StudentUpdateView.as_view(), name='student-update'),
    
    path('crudfun/',views.crudfun,name='crudfun'),
    path('crudfun/<int:pk>/',views.crudfunid, name='crudfunid'),
     
]
