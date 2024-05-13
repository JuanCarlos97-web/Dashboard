document.getElementById('mostrarImagen').addEventListener('click', function() {
    // Obtener la URL de la imagen desde los datos del script
    var imageUrl = document.currentScript.getAttribute('data-image-url');

    // Mostrar la imagen en el elemento img
    document.getElementById('imagenGenerada').src = imageUrl;
});