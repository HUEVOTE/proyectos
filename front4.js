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
Utiliza el código con precaución. Más informa




function eliminarDelCarrito(boton) {
  boton.parentNode.remove();
}

function mostrarTotalCarrito() {
  var total = 0;
  var productosCarrito = document.querySelectorAll("#carrito li");
  for (var i = 0; i < productosCarrito.length; i++) {
    var precio = parseFloat(productosCarrito[i].querySelector("p").textContent.replace("Precio:", ""));
    total += precio;
  }
  document.getElementById("total").textContent = "Total: " + total.toFixed(2) + "€";
}