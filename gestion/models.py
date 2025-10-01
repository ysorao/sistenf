from django.db import models


class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre} ({self.correo})"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    acudiente = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField()
    historia_clinica = models.TextField()
    def __str__(self):
        return self.nombre

class EstadoTurno(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoTurno, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class NotaEnfermeria(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Reporte(models.Model):
    tipo = models.CharField(max_length=50)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    generado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class ConsentimientoInformado(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='consentimientos/')

