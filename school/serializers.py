from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import School

        model = School
        fields = ('name', 'address', 'latitude', 'longitude')
        read_only_fields = fields


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('student_id', 'name', 'standard', 'section', 'father_name',
                  'gender', 'school', 'email', 'mobile')


class StudentReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('student_id', 'name', 'standard', 'section', 'father_name',
                  'gender', 'school', 'email', 'mobile')
        read_only_fields = fields
