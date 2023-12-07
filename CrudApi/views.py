# views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import logintable
from .serializers import UserSerializer
from .serializers import studentdata
from rest_framework.views import APIView 
 
from .models import student
@api_view(['POST'])
def home(request):
    if request.method == 'POST':
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def see(req):
     return render(req,'crud.html')
 


@api_view(['POST'])
def studentview(req):
    if req.method=='POST':
        serial=studentdata(data=req.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
 
 

class StudentListView(APIView):
    def get(self, request, format=None):
        students = student.objects.all()
        serializer = studentdata(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
#delete for API
#http://127.0.0.1:8000/api/students/10/
class StudentDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            student_instance = student.objects.get(pk=pk)
            student_instance.delete()
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.generics import UpdateAPIView

# for updating content through drf 

class StudentUpdateView(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = studentdata

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
def show(req):
    return render(req,'firstpage.html')