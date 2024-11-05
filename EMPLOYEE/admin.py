from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from EMPLOYEE.models import Department, Position, Employee

@admin.register(Department)
class DepartmentTranslateAdmin(TranslationAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    list_display_links = ["id", "name",]


@admin.register(Position)
class PositionTranslateAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'salary', 'department', 'created_at', 'updated_at']
    list_display_links = ["id", "name",]
    list_editable = ['salary', 'department']
    list_filter = ['name', 'salary', 'department']
    search_fields = ['name', 'department', 'salary']

# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ["name", "created_at", "updated_at"]
    

# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ['name', 'salary', 'department', 'created_at', 'updated_at']
#     list_editable = ['salary', 'department']
#     list_filter = ['name', 'salary', 'department']
#     search_fields = ['name', 'department', 'salary']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'department', 'position', 'status', 'created_at', 'last_login']
    list_display_links = ['name', 'surname', 'status']
    list_editable = ['department', 'position']
    list_filter = ['name', 'department', 'position', 'status']
    search_fields = ['name', 'department', 'position', 'status']

