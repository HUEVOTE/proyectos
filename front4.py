from django.db import models

modelos

class Categoria(models.Model):
  nombre = models.CharField(max_length=255)

class Producto(models.Model):
  nombre = models.CharField(max_length=255)
  descripcion = models.TextField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  imagen = models.ImageField(upload_to="imagenes/", blank=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Carrito(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  cantidad = models.IntegerField(default=1)


vistasrom django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria, Producto, Carrito

def inicio(request):
  categorias = Categoria.objects.all()
  productos = Producto.objects.all()
  return render(request, "inicio.html", {"categorias": categorias, "productos": productos})

@login_required
def agregar_al_carrito(request, producto_id):
  producto = Producto.objects.get(pk=producto_id)
  carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
  carrito_item, creado = Carrito.objects.get_or_create(carrito=carrito, producto=producto)
  if creado:
    carrito_item.cantidad += 1
    carrito_item.save()
  return redirect("carrito")

@login_required
def carrito(request):
  carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
  carrito_items = Carrito.objects.filter(carrito=carrito)
  total = sum([item.producto.precio * item.cantidad for item in carrito_items])
  return render(request, "carrito.html", {"carrito_items": carrito_i


from django.urls import path

urlpatterns = [
  path("", inicio, name="inicio"),
  path("agregar-al-carrito/<int:producto_id>", agregar_al_carrito, name="agregar_al_carrito"),
  path("carrito/", carrito, name="carrito"),

