document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM loaded');
    const editButton = document.querySelectorAll('#edit');
    let content = document.querySelectorAll('.content');
    editButton.forEach(element => {
        element.addEventListener('click', function () {
            console.log('edit button clicked');
        });
    });
});