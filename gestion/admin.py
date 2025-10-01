from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Usuario, Rol, Turno, Paciente, NotaEnfermeria, Reporte, ConsentimientoInformado, EstadoTurno

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'rol', 'estado')
    list_filter = ('rol', 'estado')
    search_fields = ('nombre', 'correo')

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora_inicio', 'hora_fin', 'usuario_asignado', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('usuario_asignado__nombre',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'edad')
    search_fields = ('nombre',)
    list_filter = ('edad',)

@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'paciente', 'responsable')
    list_filter = ('fecha',)
    search_fields = ('paciente__nombre', 'responsable__nombre')

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'fecha_generacion', 'generado_por')
    list_filter = ('tipo',)
    search_fields = ('tipo', 'generado_por__nombre')

@admin.register(ConsentimientoInformado)
class ConsentimientoInformadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'cuidador')
    search_fields = ('paciente__nombre', 'cuidador__nombre')

admin.site.register(EstadoTurno)
admin.site.register(Rol)

admin.site.site_header = "Administración SISTENF"
admin.site.site_title = "Sistenf Admin"
admin.site.index_title = "Panel de Administración"