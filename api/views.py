from django.shortcuts import render

# Create your views here.


from api.serializers import UserSerializer,TaskSerializer

from rest_framework.generics import CreateAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView

from api.models import Task

from rest_framework import authentication,permissions

from rest_framework import status,response


class SignUpView(CreateAPIView):

    serializer_class=UserSerializer


class TaskListCreatView(ListCreateAPIView):

    serializer_class=TaskSerializer

    queryset=Task.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by("-created_date")
    


class TaskUpdateDestroyView(UpdateAPIView,DestroyAPIView):

    serializer_class=TaskSerializer

    queryset=Task.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]


    def update(self, request, *args, **kwargs):
        
        id=kwargs.get("pk")

        Task.objects.filter(id=id).update(status=True)

        return response.Response(data={"message":"updated"},status=status.HTTP_200_OK)







    


    


