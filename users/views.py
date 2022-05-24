from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
