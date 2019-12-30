from django.urls import path
from .views import *
#from .views1 import *
urlpatterns=[
    path('create_student',createStudent,name='student-create'),
    path('',index,name='home'),
    path('update_student/<int:id>',updateStudent,name='student-update')
]