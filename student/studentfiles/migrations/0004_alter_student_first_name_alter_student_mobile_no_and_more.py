# Generated by Django 4.2.5 on 2024-02-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfiles', '0003_alter_student_dob_alter_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=399, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_no',
            field=models.CharField(max_length=399, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents_contact_no',
            field=models.CharField(max_length=399, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='usn',
            field=models.CharField(max_length=399, null=True, unique=True),
        ),
    ]
