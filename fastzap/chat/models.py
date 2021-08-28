from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField("Nome", max_length=100, null=False, blank=False)
    phone = models.CharField("Telefone", max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Attendance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=False)
    organization = models.CharField("Organização", max_length=100, null=False, blank=False)
    status = models.CharField("Status", max_length=100, null=False, blank=False)

    def __str__(self):
        return self.organization

    class Meta:
            ordering = ['organization']

class Message(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING, null=False)
    text = models.TextField("Texto", max_length=100, null=True, blank=True)
    file = models.FileField(upload_to ='uploads/', null=True, blank=True)
    type = models.CharField("Tipo", max_length=100, null=False, blank=False)
    status = models.CharField("Status", max_length=100, null=False, blank=False)

    def __str__(self):
        return self.attendance

    class Meta:
        ordering = ['attendance']

