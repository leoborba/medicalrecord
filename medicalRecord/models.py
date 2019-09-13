from django.db import models

class PatientForm(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateField(default=None, blank=True, null=True)
    collection = models.DateField(default=None, blank=True, null=True)
    delivery = models.DateField(default=None, blank=True, null=True)
    doctor = models.CharField(max_length=255)
    formId = models.CharField(max_length=255)