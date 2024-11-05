from rest_framework import serializers

from EMPLOYEE.models import Department, Position, Employee


# Department serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name',]


# Position serializers
class PositionGetSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')
    class Meta:
        model = Position
        fields = ['id', 'name', 'salary', 'department',]

class PositionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'salary', 'department',]



# Employee serializers
class EmployeeGetSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')
    position = serializers.CharField(source='position.name')
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'email', 'department', 'position', 'status',]


class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'email', 'department', 'position', 'status',]
