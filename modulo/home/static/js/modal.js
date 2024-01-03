// Agrega un evento de clic a todas las imágenes con la clase "imagen-modal"
var imagenes = document.getElementsByClassName("imagen-modal");

for (var i = 0; i < imagenes.length; i++) {
  imagenes[i].addEventListener("click", function() {
    mostrarModal(this.src);
  });
}

// Función para mostrar la modal
function mostrarModal(src) {
  var modal = document.createElement("div");
  modal.className = "modal";

  var img = document.createElement("img");
  img.className = "modal-img";
  img.src = src;

  // Cierra la modal al hacer clic fuera de la imagen
  modal.onclick = function() {
    modal.style.display = "none";
  };

  modal.appendChild(img);
  document.body.appendChild(modal);

  // Muestra la modal
  modal.style.display = "block";
}