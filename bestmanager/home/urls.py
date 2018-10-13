from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'prelims/$',views.questions,name="questions"),
    url(r'logout/$',views.logoutUser,name="logoutUser"),
    url(r'$',views.createUser,name="createUser"),
]
