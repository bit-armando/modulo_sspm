var video = document.getElementById('webcam');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var openCameraButton = document.getElementById('openCamera');
var takePhotoButton = document.getElementById('takePhoto');

var stream = null;

video.style.display = 'none';
canvas.style.display = 'none';

openCameraButton.addEventListener('click', function() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        var constraints = { video: true };
        navigator.mediaDevices.getUserMedia(constraints)
            .then(function (mediaStream) {
                video.style.display = 'block';
                video.srcObject = mediaStream;
                stream = mediaStream;
                takePhotoButton.disabled = false; 
            })
            .catch(function (error) {
                console.error('Error al acceder a la cámara: ', error);
            });
    } else {
        console.error('La API de MediaDevices no está soportada en este navegador.');
    }
});

takePhotoButton.addEventListener('click', function() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    if (stream) {
        stream.getTracks().forEach(function(track) {
            track.stop(); 
            video.style.display = 'none';
            canvas.style.display = 'block';
        });
    }
});


var imageData = canvas.toDataURL('image/png');
fetch('registro_entrada/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
        'image': imageData,
    }),
})