from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='periodo_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='periodo_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.periodo
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='asignatura_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='asignatura_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='profesor_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='profesor_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='estudiante_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='estudiante_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='nota_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='nota_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Nota {self.id}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)

class DetalleNota(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    recuperacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observacion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='detalle_nota_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='detalle_nota_updated', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Detalle de Nota {self.id}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
            super().save(*args, **kwargs)
