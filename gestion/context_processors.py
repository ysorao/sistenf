from .models import Usuario

def usuario_logueado(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            return {'usuario': usuario}
        except Usuario.DoesNotExist:
            pass
    return {'usuario': None}
