from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FunnelStatus, Student, StatusLog
from .serializers import FunnelStatusSerializer, StudentSerializer, StatusLogSerializer
from rest_framework.pagination import PageNumberPagination

def student_list(request):

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse({'students': serializer.data})


def create_student(request):
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

class FunnelStatusViewSet(viewsets.ModelViewSet):
    queryset = FunnelStatus.objects.all().order_by('order')
    serializer_class = FunnelStatusSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        student = self.get_object()
        new_status_id = request.data.get('new_status_id')
        try:
            new_status = FunnelStatus.objects.get(id=new_status_id)
        except FunnelStatus.DoesNotExist:
            return Response({'error': 'Invalid status ID'}, status=status.HTTP_400_BAD_REQUEST)

        old_status = student.current_status
        student.current_status = new_status
        student.save()

        StatusLog.objects.create(student=student, from_status=old_status, to_status=new_status)

        return Response(StudentSerializer(student).data)

class StatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusLog.objects.all().order_by('-timestamp')
    serializer_class = StatusLogSerializer
    pagination_class = PageNumberPagination  # Enable pagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # Paginate queryset
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)



