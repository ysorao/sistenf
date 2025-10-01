
from django.shortcuts import render, redirect
from .models import Turno, Usuario, NotaEnfermeria, Paciente, EstadoTurno
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(correo=correo, password=password, estado=True)
            request.session['usuario_id'] = user.id
            request.session['usuario_rol'] = user.rol.nombre

            if user.rol.nombre == 'cuidadora':
                return redirect('dashboard_cuidadora')
            elif user.rol.nombre == 'coordinador':
                return redirect('dashboard_coordinador')
            elif user.rol.nombre == 'admin':
                return redirect('dashboard_admin')
            else:
                messages.error(request, 'Rol no reconocido.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'login.html')

def dash_cuidadora(request):
    usuario_id = request.session.get('usuario_id')
    turnos = Turno.objects.filter(usuario_asignado_id=usuario_id)
    usuario = Usuario.objects.get(id=usuario_id)

    return render(request, 'dashboard_cuidadora.html', {
        'turnos': turnos,
        'usuario': usuario
    })

def dash_coordinador(request):
    return render(request,'dashboard_coordinador.html')

def dash_admin(request):
    return render(request,'dashboard_admin.html')

def logout_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(correo=correo, password=password, estado=True)
            request.session['usuario_id'] = user.id
            request.session['usuario_rol'] = user.rol.nombre  # Guardamos el nombre del rol (str)

            if user.rol.nombre == 'cuidadora':
                return redirect('dashboard_cuidadora')
            elif user.rol.nombre == 'coordinador':
                return redirect('dashboard_coordinador')
            elif user.rol.nombre == 'Enfermera':
                return redirect('dashboard_cuidadora')
            elif user.rol.nombre == 'admin':
                return redirect('dashboard_admin')
            else:
                messages.error(request, 'Rol no reconocido.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'login.html')

def registrar_nota(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        paciente_id = request.POST.get('paciente')
        responsable_id = request.session.get('usuario_id')

        paciente = Paciente.objects.get(id=paciente_id)
        responsable = Usuario.objects.get(id=responsable_id)

        NotaEnfermeria.objects.create(
            contenido=contenido,
            paciente=paciente,
            responsable=responsable
        )

        return redirect('dashboard_cuidadora')

    pacientes = Paciente.objects.all()
    return render(request, 'registrar_nota.html', {'pacientes': pacientes})

def cambiar_estado_turno(request, turno_id, nuevo_estado):
    turno = get_object_or_404(Turno, id=turno_id)

    if request.session.get('usuario_id') != turno.usuario_asignado_id:
        return HttpResponse('No autorizado.', status=403)

    estado = get_object_or_404(EstadoTurno, nombre=nuevo_estado)
    turno.estado = estado
    turno.save()

    return redirect('dashboard_cuidadora')


