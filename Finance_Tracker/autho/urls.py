from django.urls import path
from .view import sign
from .view import login_view
from .view import logout_view
from .views import demo,user,detail

urlpatterns = [
    path('sign-up/', sign),
    path('login/', login_view),
    path('logout/', logout_view),
    path('test/', demo),
    path('test/get/', user),
    path('test/get/<str:email>', detail),
]
