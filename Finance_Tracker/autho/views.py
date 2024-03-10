from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


@api_view(['POST'])
def sign(request):
    if request.method == "POST":

        name = request.data.get('name')
        user = request.data.get('username')
        passwords = request.data.get('password')

        user_created = User.objects.create_user(user, "", passwords, first_name=name)
        if(user_created):
            return Response(f"Account created for {user}. Ready to go!")


@api_view(['POST'])
def login_view(request):

    if request.method == "POST":

            user = authenticate(username=request.data["username"], password=request.data["password"])

            if user is not None:
                login(request, user)
                return Response("Good guy come in")
            else:
                return Response("User doesn`t exist!")

            return Response("")


@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response("You are logged out!")
