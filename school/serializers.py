from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import School

        model = School
        fields = ('name', 'address', 'lat', 'longitude')
        read_only_fields = fields


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('id_no', 'name', 'school', 'email', 'mobile')
        read_only_fields = fields
