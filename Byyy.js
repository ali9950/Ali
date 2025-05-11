function addImage() {
  const input = document.getElementById('imageInput');
  const gallery = document.getElementById('gallery');

  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const img = document.createElement('img');
      img.src = e.target.result;
      gallery.appendChild(img);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

function deleteImages() {
  document.getElementById('gallery').innerHTML = '';
}