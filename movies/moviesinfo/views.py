from django.shortcuts import render
from .models import Users
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            if Users.objects.get(username=request.data.get('username')):
                return Response({'message': 'username exists', 'data': 'username is already exists try new username'}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            serializer= UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'error','data':serializer.errors},status=500)

    def patch(self,request,username):
        result = Users.objects.get(username=username)
        Regser = UserSerializer(result,data=request.data,partial=True)
        if Regser.is_valid():
            Regser.save()
            return Response({'status':'success','data':Regser.data},status=200)
        else:
            return Response({'status':'failed','data':Regser.errors},status=404)

    def delete(self,request,username):
        result = Users.objects.filter(username=username)
        try:
            result.delete()
            return Response({'status':'deleted','data':'deleted successfully'},status=200)
        except:
            return Response({'status':'failed','data':'username is referenced as foreign key in invoice so delete username in invoice first'},status=404)

class LoginView(APIView):
    def post(self,request):
        username= request.data.get('username')
        password= request.data.get('password')
        try:
            user= Users.objects.get(username= username, password=password)
            # return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
           # return redirect('social:begin', 'google-oauth2')
            return render(request, 'login.html')
        except Users.DoesNotExist:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
