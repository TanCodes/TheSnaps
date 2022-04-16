// show image in modal
function showModalWithImage(imageUrl){
    $('#image-modal').modal('show')
    $('#image-show').attr('src',`/media/${imageUrl}`)
}

 // copy image link
(function() {
    const imageInfo = {};
    window.addEventListener('click', function (event) {

    var currentElement = event.target;
    if (currentElement.tagName === 'IMG') {
    imageInfo.source = currentElement.src;
    document.getElementById("img-urll").href = imageInfo.source;
    document.getElementById("img-urll-2").href = imageInfo.source;
    }
});
})();