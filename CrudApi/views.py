# views.py
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import logintable
from .serializers import UserSerializer
from .serializers import studentdata,himanshuserializer
from rest_framework.views import APIView 

from .models import student,himanshu  

@api_view(['POST','GET','DELETE'])
def crudfun(req):
    if req.method =='POST':
        serial=himanshuserializer(data=req.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif req.method =='GET':
        datahimanshu=himanshu.objects.all()
        serial=himanshuserializer(datahimanshu,many=True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    elif req.method == 'DELETE':
        count = himanshu.objects.all().delete()
        # return Response({'message ww' : '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        return Response({f" deleted succesfully {count[0]} "},status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def crudfunid(req, pk):
    # Retrieve the object with the given primary key (pk) or return 404 if not found
    instance = get_object_or_404(himanshu, pk=pk)

    if req.method == 'GET':
        # Serialize and return the data
        serializer = himanshuserializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif req.method == 'PUT':
        # Update the instance with the new data
        serializer = himanshuserializer(instance, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        # Delete the instance
        instance.delete()
        return Response({'message': 'Object deleted successfully!'},status=status.HTTP_204_NO_CONTENT)
 


 
 
# class StudentDeleteView(APIView):
#     def delete(self, request, pk, format=None):
#         try:
#             student_instance = student.objects.get(pk=pk)
#             student_instance.delete()
#             return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         except student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

 
def show(req):
    return render(req,'firstpage.html')