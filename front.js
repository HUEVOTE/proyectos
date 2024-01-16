function buscar() {
  var texto = document.getElementById("texto").value;
  var productos = document.getElementsByClassName("producto");
  for (var i = 0; i < productos.length; i++) {
    if (productos[i].textContent.toLowerCase().indexOf(texto.toLowerCase()) > -1) {
      productos[i].style.display = "block";
    } else {
      productos[i].style.display = "none";