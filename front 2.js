function buscar() {
  var texto = document.getElementById("texto").value;
  var productos = document.getElementsByClassName("producto");
  for (var i = 0; i < productos.length; i++) {
    if (productos[i].textContent.toLowerCase().indexOf(texto.toLowerCase()) > -1) {
      productos[i].style.display = "block";
    } else {
      productos[i].style.display = "none";
    }
  }
}

function agregarAlCarrito(producto) {
  var carrito = document.getElementById("carrito");
  var productoNuevo = document.createElement("li");
  productoNuevo.innerHTML = `
    <img src="<span class="math-inline">\{producto\.imagen\}" alt\="</span>{producto.nombre}">
    <h3>${producto.nombre}</h3>
    <p>Precio: ${producto.precio}</p>
    <button type="button" onclick="eliminarDelCarrito(this)">Eliminar</