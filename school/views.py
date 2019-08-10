from django_filters.rest_framework import DjangoFilterBackend
from drfaddons import generics
# ToDo: Fix Signature expired Issue
from rest_framework.generics import RetrieveAPIView, ListAPIView

from manager.permissions import IsStaff


class SchoolView(generics.OwnerListAPIView):
    from .models import School
    from .serializers import SchoolSerializer

    permission_classes = (IsStaff,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')


# ToDo: Only retrieve students linked to specific school
class StudentView(ListAPIView):
    from .models import Student
    from .serializers import StudentSerializer
    
    permission_classes = (IsStaff,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveView(RetrieveAPIView):
    from .models import Student
    from .serializers import StudentReadOnlySerializer

    permission_classes = (IsStaff,)
    queryset = Student.objects.all()
    serializer_class = StudentReadOnlySerializer
