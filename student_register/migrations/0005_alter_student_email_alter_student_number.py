# Generated by Django 4.1 on 2022-09-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0004_alter_student_email_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.IntegerField(),
        ),
    ]
