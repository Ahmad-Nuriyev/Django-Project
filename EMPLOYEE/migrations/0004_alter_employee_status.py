# Generated by Django 5.1.2 on 2024-10-27 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMPLOYEE', '0003_alter_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.BooleanField(),
        ),
    ]
