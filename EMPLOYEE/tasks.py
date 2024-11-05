from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail

from EMPLOYEE.models import Employee
from management import settings


@shared_task
def login_reminder():
    amount_of_nonlogin_days = timezone.now() - timedelta(days=2)
    non_activemployees = Employee.objects.filter(last_login__lt=amount_of_nonlogin_days)

    login_url = 'http://127.0.0.1:8000/auth/token/'

    for employee in non_activemployees:
        send_mail(
            'Dear Employee',
            f'This email is a notification that you have not logged in system for more than 2 days. Please proceed to Login page: {login_url}',
            settings.EMAIL_HOST_USER,
            [employee.email]
        )