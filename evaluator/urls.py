from django.urls import path
from .views import *

app_name = 'evaluator'

urlpatterns = [
    path('', ClassList.as_view(), name='class_list'),
    path('students/', StudentList.as_view(), ),
    path('upload/', AssignmentUpload.as_view(), ),
    path('result/', EvaluationResult.as_view(), ),
    path('logout/', Logout.as_view(), ),
    path('class/', ClassDetail.as_view(),)
]
