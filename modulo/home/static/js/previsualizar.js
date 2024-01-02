document.getElementById('imagen').addEventListener('change', function(e) {
    var reader = new FileReader();
    reader.onload = function() {
        document.getElementById('preview').src = reader.result;
        document.getElementById('preview').style.display = 'block';
    };
    reader.readAsDataURL(e.target.files[0]);
});