from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from appIMDb.models import Pelicula

def registro(request):
    """Registro para un nuevo usuario."""

    if request.method != 'POST':
        # Muestra el formulario de registro en blanco.
        form = UserCreationForm()
    else:
        # Procesa el formulario llenado.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            nuevoUsuario = form.save()
            # Loggea al usuario y lo redirecciona a la pagina principal
            login(request, nuevoUsuario)
            return redirect('appIMDb:index')

    # Recarga la  pagina y muestra un formulario en blanco, o un formulario
    # que no sea valido.
    context = {'form': form}
    return render(request, 'registration/registro.html', context)

@login_required
def marcarFav(request, pelicula_id):
    """Usuario marca una pelicula como de sus favoritas."""

    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    if pelicula.favoritos.filter(id=request.user.id).exists():
        # Elimina la pelicula de las favoritas del usuario
        pelicula.favoritos.remove(request.user)
    else:
        pelicula.favoritos.add(request.user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])