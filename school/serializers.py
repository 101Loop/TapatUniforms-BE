from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import School

        model = School
        fields = ('name',)
        read_only_fields = fields


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('id_no', 'name', 'school')
        read_only_fields = fields
