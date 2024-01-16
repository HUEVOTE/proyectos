
modelos
ffrom django.db import models


class Usuario(models.Model):
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  contrasena = models.CharField(max_length=255)

  def __str__(self):
    return self.nombre + " " + self.apellido

class Cuenta(models.Model):
  numero_cuenta = models.CharField(max_length=255, unique=True)
  saldo = models.DecimalField(max_digits=10, decimal_places=2)
  tipo_cuenta = models.CharField(max_length=255)

  def __str__(self):
    return self.numero_cuenta


vists

from django.contrib.auth.forms import AuthenticationForm

def inicio_sesion(request):
  if request.user.is_authenticated:
    return redirect("inicio")

  form = AuthenticationForm(request.POST or None)
  if request.method == "POST" and form.is_valid():
    user = form.cleaned_data["username"]
    password = form.cleaned_data["password"]
    user = authenticate(username=user, password=password)
    if user is not None and user.is_active:
      login(request, user)
      return redirect("inicio")
    else:
      form.add_error(None, "Usuario o contraseña incorrectos")

  return render(request, "inicio_sesion.html", {"form": form})

plantillas

{% extends "base.html" %}

{% block contenido %}
  <h1>Inicio de sesión</h1>

  <form action="{% url 'inicio_sesion' %}" method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Usuario">
    <input type="password" name="password" placeholder="Contraseña">
    <input type="submit" value="Iniciar sesión">
  </form>
{% endblock %}