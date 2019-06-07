from django_filters.rest_framework import DjangoFilterBackend
from drfaddons import generics

# ToDo: Fix Signature expired Issue


class SchoolView(generics.OwnerListAPIView):
    from .models import School
    from .serializers import SchoolSerializer

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')


class StudentView(generics.OwnerListAPIView):
    from .models import Student
    from .serializers import StudentSerializer

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'school')
