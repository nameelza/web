document.addEventListener('DOMContentLoaded', function () {
    const image = document.querySelectorAll('#smallImage');
        image.forEach((image) => {
            image.addEventListener('click', function () {
                // Get the expanded image
                const expandImg = document.getElementById("expandedImage");
                // Use the same src in the expanded image as the image being clicked on from the grid
                expandImg.src = image.src;
            });
        });
});