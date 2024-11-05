from django.urls import path

from EMPLOYEE.api.views import DepartmentListCreateView, DepartmentUpdateDestroy, PositionListCreateView, PositionUpdateDestroy, EmployeeListCreateView, EmployeeUpdateDestroy

urlpatterns = [
    path('department/', DepartmentListCreateView.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentUpdateDestroy.as_view(), name='update_department'),
    path('position/', PositionListCreateView.as_view(), name='position'),
    path('position/<int:pk>/', PositionUpdateDestroy.as_view(), name='position_update'),
    path('employee/',EmployeeListCreateView.as_view(), name='employee'),
    path('employee/<int:pk>/', EmployeeUpdateDestroy.as_view(), name='employee_update'),
]