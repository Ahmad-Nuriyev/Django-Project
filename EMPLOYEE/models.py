from django.db import models

from django.contrib.auth.models import User

class Date (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department (Date):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"

    def __str__(self):
        return self.name

class Position (Date):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    department = models.ForeignKey (Department, on_delete=models.CASCADE, related_name="position")

    class Meta:
        verbose_name_plural = "Positions"
        verbose_name = "Position"

    def __str__(self):
        return self.name

class Employee (Date):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.ForeignKey (Department, on_delete=models.CASCADE, related_name="employee")
    position = models.ForeignKey (Position, on_delete=models.CASCADE, related_name="position")
    status = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name = "Employee" 

    def __str__(self):
        return f"{self.name} {self.surname}"
    