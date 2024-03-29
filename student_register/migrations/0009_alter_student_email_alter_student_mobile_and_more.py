# Generated by Django 4.1 on 2022-09-09 15:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0008_alter_student_email_alter_student_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
