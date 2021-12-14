document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM loaded');
    const image = document.querySelectorAll('#smallImage');
    console.log(image);
        image.forEach((image) => {
            image.addEventListener('click', function () {
                // Get the expanded image
                const expandImg = document.getElementById("expandedImage");
                // Use the same src in the expanded image as the image being clicked on from the grid
                expandImg.src = image.src;
            });
        });
});