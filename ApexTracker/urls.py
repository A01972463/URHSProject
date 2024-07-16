from django.urls import path
from . import views

app_name = 'ApexTracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.input, name='input'),
    path('report/', views.report, name='report'),
    path('settings/', views.settings, name='settings'),
    path('settings/newstudent', views.new_student, name='new'),
    path('settings/editstudent', views.edit_student, name='edit'),
    # path('settings/quickdisplay', views.quick, name='quick'),
]
