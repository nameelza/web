document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = () => {
        const task = document.querySelector('#task').value;
        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#tasks').append(li);

        // Stop the form from submitting
        return false;
    }
});