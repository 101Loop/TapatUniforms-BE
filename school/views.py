from django_filters.rest_framework import DjangoFilterBackend
from drfaddons import generics

# ToDo: Fix Signature expired Issue
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from manager.permissions import IsManager

from .filters import IsManagerFilterBackend
from .models import School, Student


class SchoolView(generics.OwnerListAPIView):
    from .serializers import SchoolSerializer

    permission_classes = (IsManager,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    filter_fields = ("id", "name")


# ToDo: Only retrieve students linked to specific school
class StudentView(ListCreateAPIView):
    from .serializers import StudentSerializer

    queryset = Student.objects.all()
    permission_classes = (IsManager,)
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by_id=self.request.user.id)


class StudentRetrieveView(RetrieveAPIView):
    from .models import Student
    from .serializers import StudentReadOnlySerializer

    permission_classes = (IsManager,)
    queryset = Student.objects.all()
    serializer_class = StudentReadOnlySerializer
    filter_backends = (DjangoFilterBackend, IsManagerFilterBackend)
