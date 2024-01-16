modelos

from django.db import models

class Producto(models.Model):
  nombre = models.CharField(max_length=255)
  imagen = models.URLField()
  precio = models.FloatField()

  def __str__(self):
    return self.nombre

vistas
from django.shortcuts import render
from .models import Producto

def productos_lista(request):
  productos = Producto.objects.all()
  return render(request, "productos/lista.html", {"productos": productos})


plantillas

{% extends "base.html" %}

{% block contenido %}
  <h1>Lista de productos</h1>

  <ul>
    {% for producto in productos %}
      <li>
        <a href="{% url 'productos_detalle' producto.id %}">
          <img src="{{ producto.imagen }}" alt="{{ producto.nombre }}">
          <h3>{{ producto.nombre }}</h3>
          <p>Precio: {{ producto.precio }}</p>
        </a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}