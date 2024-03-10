from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Userserializer
from django.contrib.auth.models import User


@api_view(['GET'])
def demo(request):
    a ={
        "Get" : "get/",
        "Create" : "create/",
        "Delete" : "put/",
        "Update": "update/",
        "single user": "get/<email>"
    }
    return Response(a)

@api_view(['GET'])
def user(request):
    u = User.objects.all()
    serializer = Userserializer(u, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, email):
    u = User.objects.get(username= email)
    serializer = Userserializer(u, many=False)
    return Response(serializer.data)

@api_view(['GET','POST'])
def Posts(request):
    serializer = Userserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response('User Added')


@api_view(['GET','POST'])
def Update(request,id):
    user = User.objects.get(id = id)
    serializer = Userserializer(instance=user , data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response("User Updated")

@api_view(['DELETE'])
def Delete(request,id):
    user = User.objects.get(id = id)
    if user == None:
        return Response("No user found")

    user.delete()

    u = User.objects.all()
    serializer = Userserializer(u, many=True)

    return Response(serializer.data)




