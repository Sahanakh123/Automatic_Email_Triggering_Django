# Generated by Django 4.2.5 on 2024-02-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfiles', '0004_alter_student_first_name_alter_student_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
