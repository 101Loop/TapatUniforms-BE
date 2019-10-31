from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import School

        model = School
        fields = ("id", "name", "address", "city_name")
        read_only_fields = fields


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = (
            "id",
            "student_id",
            "name",
            "standard",
            "section",
            "gender",
            "father_name",
            "email",
            "mobile",
            "school",
        )


class StudentReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = (
            "student_id",
            "name",
            "standard",
            "section",
            "father_name",
            "gender",
            "school",
            "email",
            "mobile",
        )
        read_only_fields = fields
