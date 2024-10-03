from django.conf.urls import url
from.import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^ createaccount',views.createaccount,name='createaccount'),
    url(r'^ saveaccount',views.saveaccount,name='saveaccount'),
    url(r'^ login',views.login,name='login'),
    url(r'^ logcode',views.logcode,name='logcode'),
    url(r'^ depositamt',views.depositamt,name='depositamt'),
    url(r'^ withdrawamt',views.withdrawamt,name='withdrawamt'),

]