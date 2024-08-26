from django.db import models

# Create your models here.
from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tanggal_terbit = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

def __str__(self):
    return self.judul
