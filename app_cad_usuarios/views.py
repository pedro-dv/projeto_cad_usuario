from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages


# (request) é um parametro do django, que te permite acessar os dados q estao dentro daquela pagina.
# (render) renderiza a pagina

def home(request):
    return render(request, 'usuarios/home.html') # endereço que futuramente irei criar dentro do app.


def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        if nome and idade:
            # Verifica se o usuário já existe
            if Usuario.objects.filter(nome=nome, idade=idade).exists():
                messages.error(request, 'Usuário já existe.')
            else:
                novo_usuario = Usuario(nome=nome, idade=idade)
                novo_usuario.save()
                messages.success(request, 'Usuário cadastrado com sucesso.')

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # retornar  os dasdos para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)




def delete_usuario(request, id_usuario):
    try:
        usuario = Usuario.objects.get(id_usuario=id_usuario)
        usuario.delete()
    except Usuario.DoesNotExist:
        pass
    return redirect('listagem_usuarios')


