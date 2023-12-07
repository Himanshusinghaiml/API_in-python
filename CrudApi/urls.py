from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.show),
    path('home/', views.home, name='home'),
    path('see/',views.see,name='see'),
    path('studentdata/',views.studentview,name="studentdata"),
    path('api/stu/', views.StudentListView.as_view(),name='student-list'),
    path('api/students/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('api/students/<int:pk>/update/',views.StudentUpdateView.as_view(), name='student-update'),
]
