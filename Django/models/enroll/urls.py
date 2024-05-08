from django.urls import path
from enroll import views
urlpatterns = [
    path('stu/',views.studentinfo),
    path('registration/', views.showformdata),
    path('success/', views.thankyou),
]
