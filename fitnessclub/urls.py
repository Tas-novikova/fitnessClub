from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('', views.index, name='home'),
    #path('enter', views.enter, name='enter'),
    #path('register', views.register, name='register'),
    path('services', views.services, name='services'),
    path('<int:pk>', views.ServicesDetailView.as_view(), name='services-detail'),
    path('price', views.price, name='price'),
    path('timetable', views.timetable, name='timetable'),
    path('trainers', views.trainers, name='trainers'),
    path('photos', views.photos, name='photos'),
    path('contacts', views.contacts, name='contacts'),
    path('gym', views.gym, name='gym'),
    path('bodySculpt', views.bodySculpt, name='bodySculpt'),
    path('functionalTraining', views.functionalTraining, name='functionalTraining'),
    path('lowerBody', views.lowerBody, name='lowerBody'),
    path('upperBody', views.upperBody, name='upperBody'),
    path('pilates', views.pilates, name='pilates'),
    path('stepAerobics', views.stepAerobics, name='stepAerobics'),
    path('stretching', views.stretching, name='stretching'),
    path('tabsStretching', views.tabsStretching, name='tabsStretching'),
    path('freeLesson', views.freeLesson, name='freeLesson'),
    path('checkCard', views.checkCard, name='checkCard'),
    path('statistic', views.statistic, name='statistic'),
    #path('tableFreeLesson', views.tableFreeLesson, name='tableFreeLesson'),

]
