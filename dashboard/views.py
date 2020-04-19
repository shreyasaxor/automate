from django.shortcuts import render
# Create your views here.
from django.views import View
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .exception import IncorrectAuthCredentials, IncorrectData
from .serializer import LoginSerializer


class Test(View):
    template_name='Flowchart_.html'

    def get(self,request,*args,**kwargs):

        return render(request,template_name =self.template_name)

test =Test.as_view()


class Login(View):
    template_name='loginpage.html'
    def get(self,request,*args,**kwargs):
        return render(request,template_name =self.template_name)



login =Login.as_view()




class AuthApi(APIView):

    def post(self,request,*args,**kwargs):
        """ post method to authenticate the users provided email and password """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data['username'])
            user = authenticate(username=serializer.data['username'], password=request.data['password'])
        else:
            raise IncorrectData(detail=serializer.errors,code=400)
        if not user:
            raise IncorrectAuthCredentials(detail="Incorrect authentication credentials", code=401)
        return Response({'Auth':True}, status=status.HTTP_200_OK)

auth = AuthApi.as_view()