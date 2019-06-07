from django_filters.rest_framework import DjangoFilterBackend
from drfaddons import permissions
from rest_framework import generics


class SchoolView(generics.ListAPIView):
    from .models import School
    from .serializers import SchoolSerializer

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')


class StudentView(generics.ListAPIView):
    from .models import Student
    from .serializers import StudentSerializer

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'school')
