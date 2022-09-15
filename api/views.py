
from .models import Task
from .models import User
from .serializers import TaskSerializer,UserSerializer
from rest_framework.decorators import APIView,api_view,permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
from django.http import Http404
from rest_framework.status  import *
from django.contrib.auth import logout,authenticate,login
from rest_framework import permissions,serializers



class TaskList(APIView): 
    authentication_classes =[BasicAuthentication]    
    permission_classes = [IsAuthenticated]          #Restrict unauthenticated user
    
    def get(self , request):                    #GET all tasks 
        print(request.user)
        # tasks = Task.objects.all()
        tasks = Task.objects.all().filter(user=request.user)            #GET all tasks of particular user
        serializer = TaskSerializer(tasks , many=True)                  #converting data format
        return Response(serializer.data)                                #Send data 
    
    def post(self , request):                                           #Create new task 

        
        serializer = TaskSerializer(data = request.data)                #take data convert into python understandable to JSON
        if serializer.is_valid() :
            serializer.save(user=request.user)                                           #save data  instance
            return Response(serializer.data) 
        return Response(status=HTTP_400_BAD_REQUEST)                    #if data is not in valid format return 400 error


class IsOwner(permissions.BasePermission):                              #custom permission to access particular tasks
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user                                 #check for is given user is owner of object or not 

class TaskDetails(APIView):                                             #acesss single object
    authentication_classes =[BasicAuthentication]                       
    permission_classes = [IsOwner]                                      #custom permissions

    def get_object(self , pk):                                          #function to get object 

        try:
            return Task.objects.get(id=pk)                              
        except:
            raise Http404                                               #If object is not found raise 404 error
        
    def get(self , request , pk):  
        task = self.get_object(pk)                                      #get object which id == pk
        if task.user != request.user:                                   #check logged user is owner or not of object
            return Response(status=HTTP_403_FORBIDDEN)
        serializer = TaskSerializer(task)                               
        print(serializer)                                     #get particular object
        return Response(serializer.data)
    
    def put(self , request , pk):                                       #update object data 
        task = self.get_object(pk)
        serializer = TaskSerializer(instance=task , data = request.data)    
        if serializer.is_valid() :                                      
            serializer.save()
            return Response(serializer.data) 
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self , request , pk):                                    #delete object
        task = self.get_object(pk)
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)





class UserRegister(APIView):                                            #user registeration
    def post(self,request):                                                 
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(status=HTTP_400_BAD_REQUEST)


# class UserLogin(APIView):                                            #user registeration
#     def post(self,request):   

#         user = authenticate(username="qwer1234@gmail.com", password="qwer@1234")
#         if user is not None:
#             login(request, user)                                      
#         return Response(status=HTTP_200_OK)


class UserLogout(APIView):                                              #user logout
    def get(self,request,format=None):
        logout(request)
        return Response(status=HTTP_200_OK)
