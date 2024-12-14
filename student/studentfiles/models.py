from django.db import models


class Student(models.Model):
    usn = models.CharField(max_length=399, unique=True, null=True, verbose_name="Student USN")
    first_name = models.CharField(max_length=399, null=True, verbose_name="Student First Name")
    last_name = models.CharField(max_length=399, blank=True, null=True, verbose_name="Student Last Name")
    mobile_no = models.CharField(max_length=399, null=True, verbose_name="Mobile No")
    email = models.EmailField(max_length=399, blank=True, null=True, verbose_name="Email ID")
    parents_contact_no = models.CharField(max_length=399, null=True, verbose_name="Parents Contact No")
    dob = models.DateField(blank=True, null=True, verbose_name="D.O.B")
    exam_fees_paid=models.CharField(max_length=399, null=True, verbose_name="Exam Fess Paid")
    last_date=models.DateField(blank=True, null=True, verbose_name="Last Date")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.usn}"



