from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required



def home(request):  #comentariosForms
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comentario = form.cleaned_data['comentario']
            obj = Comentario(nombre=nombre, comentario=comentario)
            obj.save()
            #Configurar Correo
            #asunto = form.cleaned_data['nombre']
            #mensaje = form.cleaned_data['comentario']
            #direccion = "entregafinal2022@yahoo.com"
            #destinatario = ["pameyari2529@gmail.com"]

            #send_mail(asunto,mensaje,direccion,destinatario)

            form = ComentarioForm()
            mensaje = "Gracias por tu comentario"
            return render(request,"bienvenida.html", {"articulos":articulos, "mensaje":mensaje,"form":form})
    form = ComentarioForm()
    return render(request, "bienvenida.html", {"articulos":articulos, "form":form})

@login_required
def entrada(request):
    if request.method == "POST":

        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            articulos = Entrada.objects.all()
            return render(request, "bienvenida.html", {"articulos": articulos})
    else:
        form = EntradaForm(initial={"autor":request.user})

    return render(request, "entradaForm.html", {"form":form})


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu = request.POST['username']
            clave = request.POST['password']
            usuario = authenticate(username = usu, password = clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'bienvenida.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'loginForm.html', {'form':form, 'mensaje': 'Usuario o clave incorrecta'})
        else:
            return render(request, 'loginForm.html', {'form':form, 'mensaje':f"FORMULARIO INVALIDO"})
    else:
        form = AuthenticationForm()
    return render(request, 'loginForm.html', {'form':form})

def registrate(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # es igual a form.cleaned_data.get('username')
            form.save()
            # u = User.objects.get(username=username)
            # permission = Permission.objects.get(codename='view_personal')
            # u.user_permissions.add(permission)
            return render(request, "registro.html", {"mensaje":f"Usuario creado: { username }"})
    else:
        form = UserRegisterForm()

    return render(request, "registroForm.html", {"form":form})


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            try:
                avatarViejo=Avatar.objects.get(user=request.user)
                if(avatarViejo.imagen):
                    avatarViejo.delete()
            except:
                pass
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'agregarAvatar.html', {'formulario':formulario, 'usuario':request.user})


@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'bienvenida', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})




def Articulos(request):
    comentar=Comentario.objects.all()
    nombre=Comentario.nombre
    return render(request,"articulos.html",{"comentar":comentar})
    
def inicio(request):
    return render(request,"bienvenida.html")

