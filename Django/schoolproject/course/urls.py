from course import views
from django.urls import path
urlpatterns = [
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
]