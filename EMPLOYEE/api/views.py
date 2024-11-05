from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from EMPLOYEE.models import Department, Position, Employee
from EMPLOYEE.api.serializers import DepartmentSerializer, PositionGetSerializer, PositionPostSerializer, EmployeeGetSerializer, EmployeePostSerializer


class BaseUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    def update(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response ({"message" : "No permit to change the data"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response ({"message" : "No permit to delete the data"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class BasePostView(ListCreateAPIView):

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"message" : "No permit too add the data"}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)


# Views for Department model 
class DepartmentListCreateView(BasePostView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentUpdateDestroy(BaseUpdateDestroyView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    

# Views for Position model
class PositionListCreateView(BasePostView):
    serializer_class = PositionGetSerializer
    queryset = Position.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = PositionPostSerializer
        return self.serializer_class
    
class PositionUpdateDestroy(BaseUpdateDestroyView):
    serializer_class = PositionPostSerializer
    queryset = Position.objects.all()

    

# Views for Employee model
class EmployeeListCreateView(BasePostView):
    serializer_class = EmployeeGetSerializer
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = EmployeePostSerializer
        return self.serializer_class
    
class EmployeeUpdateDestroy(BaseUpdateDestroyView):
    serializer_class = EmployeePostSerializer
    queryset = Employee.objects.all()

            

