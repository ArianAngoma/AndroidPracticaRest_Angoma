from django.db import models


# Create your models here.
class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    motivo = models.TextField(null=True)
    imagen = models.FileField(upload_to='storage/images/', max_length=250, null=True)

    class Meta:
        db_table = "Solicitud"

    def __str__(self):
        return self.nombre